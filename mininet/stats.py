from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib import hub
from ryu.ofproto import ofproto_v1_3


class PortStatsCollector(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PortStatsCollector, self).__init__(*args, **kwargs)
        self.datapaths = {}
        self.monitor_thread = hub.spawn(self._monitor)
        self.lastTx = 0
        self.lastRx = 0
        self.lastPkt = 0

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        self.datapaths[datapath.id] = datapath

    def _request_port_stats(self, datapath):
        self.logger.info('send port stats request: %016x', datapath.id)
        ofp = datapath.ofproto
        ofp_parser = datapath.ofproto_parser

        req = ofp_parser.OFPPortStatsRequest(datapath, 0, ofp.OFPP_ANY)
        datapath.send_msg(req)
    
    def _request_flow_stats(self, datapath):
        self.logger.info('send flow stats request: %016x', datapath.id)
        ofp = datapath.ofproto
        ofp_parser = datapath.ofproto_parser

        match = ofp_parser.OFPMatch()
        req = ofp_parser.OFPFlowStatsRequest(datapath, 0, ofp.OFPTT_ALL, ofp.OFPP_ANY, ofp.OFPG_ANY, 0, 0, match)
        datapath.send_msg(req)

    def _monitor(self):
        while True:  
            # print(len(self.datapaths.values()))
            for dp in self.datapaths.values():
                self._request_port_stats(dp)
                self._request_flow_stats(dp)
            hub.sleep(10)

    @set_ev_cls(ofp_event.EventOFPPortStatsReply, MAIN_DISPATCHER)
    def port_stats_reply_handler(self, ev):
        body = ev.msg.body

        self.logger.info('datapath         '
                         'port     '
                         'rx-pkts  rx-bytes '
                         'tx-pkts  tx-bytes')
        self.logger.info('---------------- '
                         '-------- '
                         '-------- -------- '
                         '-------- --------')
        
        for stat in sorted(body, key=lambda stat: stat.port_no):
            self.logger.info('%016x %8x %8d %8d %8d %8d',
                             ev.msg.datapath.id, stat.port_no,
                             stat.rx_packets, stat.rx_bytes,
                             stat.tx_packets, stat.tx_bytes)
    
    @set_ev_cls(ofp_event.EventOFPFlowStatsReply, MAIN_DISPATCHER)
    def flow_stats_reply_handler(self, ev):
        body = ev.msg.body

        self.logger.info('datapath         '
                         'in-port  eth-dst         '
                         'out-port packets  bytes')
        self.logger.info('---------------- '
                         '-------- ----------------- '
                         '-------- -------- --------')
        for stat in sorted([flow for flow in body if flow.priority == 1],
                           key=lambda flow: (flow.match['in_port'],
                                             flow.match['eth_dst'])):
            self.logger.info('%016x %8x %17s %8x %8d %8d',
                             ev.msg.datapath.id,
                             stat.match['in_port'], stat.match['eth_dst'],
                             stat.instructions[0].actions[0].port,
                             stat.packet_count, stat.byte_count)

        flows = []
        for stat in ev.msg.body:
            flows.append('table_id=%s '
                        'duration_sec=%d duration_nsec=%d '
                        'priority=%d '
                        'idle_timeout=%d hard_timeout=%d flags=0x%04x '
                        'cookie=%d packet_count=%d byte_count=%d '
                        'match=%s instructions=%s' %
                        (stat.table_id,
                        stat.duration_sec, stat.duration_nsec,
                        stat.priority,
                        stat.idle_timeout, stat.hard_timeout, stat.flags,
                        stat.cookie, stat.packet_count, stat.byte_count,
                        stat.match, stat.instructions))
        self.logger.info('FlowStats: %d', len(flows))
