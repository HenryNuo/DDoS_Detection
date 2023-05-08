# Evaluation of Models Detecting and Mitigating DDoS Flow Using SDN System
The problem area:
Keywords: SDN, ML, Security, DDos

DDoS attacks have always been a major threat to the network system. DDoS attacks work by overwhelming a network with a large amount of traffic. With the rise of the Software Defined Network (SDN), there are new opportunities for us to interrupt DDoS attacks in a distributed manner during the transmission of network traffic instead of centralized processing at the end of flow, which helps reduce the chance of network congestion or even failures.

**Related work:**
[1] The research group made a huge contribution in creating datasets for the training purpose, and they examined the recognizing efficiency of multiple ML models, but they didn’t build up a network to evaluate if the model can simulate DDoS defending in SDN.
[2] This paper gives a comprehensive evaluation of different ML models recognizing DDoS flow and tested their DDoSdetection system inside a small networking environment, but this environment is too small in scale to reflect true attacking situations in real life.
[3] Instead of examining using SDN for defending DDoS attacks, researchers conduct a multi-aspect evaluation of the security vulnerabilities including receiving DDoS attacks, which is an important perspective we need to pay attention to.
Goal of the project:
Develop a Machine-learning-based DDoS Intrusion Detection System inside a large scale simulated SDN with hundreds of nodes, then evaluate the efficiency of the interrupting DDoS attack flow and the effect of networking utilization by this system under attack.

**Work distribution:**
(1) Set up a virtual network by technologies like Mininet 
(2) Develop machine learning models for detecting DDoS attacks 
(3) Evaluate the effectiveness of the model and effect on the SDN network. 

**References:**
[1] A. Chetouane, K. Karoui, and G. Nemri, “An intelligent ML-based IDS framework for ddos detection in the SDN environment,” Advances in Mobile Computing and Multimedia Intelligence, pp. 18–31, 2022. https://link.springer.com/chapter/10.1007/978-3-031-20436-4_2
[2] A. Ahmad, E. Harjula, M. Ylianttila and I. Ahmad, "Evaluation of Machine Learning Techniques for Security in SDN," 2020 IEEE Globecom Workshops (GC Wkshps, Taipei, Taiwan, 2020, pp. 1-6, doi: 10.1109/GCWkshps50303.2020.9367477. https://ieeexplore.ieee.org/document/9367477
[3] O. Rahman, M. A. G. Quraishi and C. -H. Lung, "DDoS Attacks Detection and Mitigation in SDN Using Machine Learning," 2019 IEEE World Congress on Services (SERVICES), Milan, Italy, 2019, pp. 184-189, doi: 10.1109/SERVICES.2019.00051. https://ieeexplore.ieee.org/document/8817237
   
