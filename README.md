# A Multi-Approach Generalized Framework for Automated Solution Suggestion of Support Tickets
An open source python-based framework for generating resolution actions recommendation for Ticket Support Systems

Nowadays, customer support systems are one of the key factors in maintaining any big company's reputation and success. These systems are capable of handling a large number of tickets systemically and provides a mechanism to track/logs the communication between customer and support agents. Companies invest huge amounts of money in training support agents and deploying customer care services for their products and services. Support agents are responsible for handling different customer queries and implementing required actions to solve a particular issue or problem raised by the service/product user. In a bigger picture, customer support systems could receive a large amount of ticket/issue raised depending upon the number of users and services being offered. Customer care service gets directly affected due to the high volume of tickets and a limited number of support agents. Therefore, providing support agents with the recommendations about the possible resolution actions for a new ticket would be helpful and can save a lot of time. This research is focused on the development of an end to end framework for suggesting resolution actions rather than recommending free form resolution text against a newly raised ticket. To develop such a system, the pipeline is broadly divided into four components that are data preprocessing, actions extractor, resolution predictor, and evaluation. In actions extractor module, we have proposed a technique to identify and extract actionable phrases from resolution text. For resolution predictor, we have proposed two different pipelines that are called as 'Information Retrieval' and 'Deep Learning' based methods. The information retrieval method is based on a ticket similarity search to find the most relevant historical tickets which then leads to corresponding resolution actions. On the other hand, deep learning methods make use of actions extractor module directly and implemented in a way to directly predict resolution actions. To compare and evaluate the mentioned methods on the same ground, we also proposed an actions evaluation scheme/criterion which uses BertScore and METEOR score jointly to compute the score against actual and predicted actions for a particular test ticket. The analysis and experiments are performed on the real-world IBM ticket dataset. Overall, we observed that deep learning techniques outperformed information retrieval-based methods and achieved better performance and scores comparatively.

## Download Pretrained Weights form here
Custom Models: https://github.com/SyedShahzaib790/A-Multi-Approach-Generalized-Framework-for-Automated-Solution-Suggestion-of-Support-Tickets/tree/master/custom_models

Pretrained Models: https://github.com/SyedShahzaib790/A-Multi-Approach-Generalized-Framework-for-Automated-Solution-Suggestion-of-Support-Tickets/tree/master/pretrained_models

## Overall Framework Architecture
![Framework Architecture](https://raw.githubusercontent.com/SyedShahzaib790/A-Multi-Approach-Generalized-Framework-for-Automated-Solution-Suggestion-of-Support-Tickets/master/Framework%20Architecure_2%20(1).jpg)

## System Evaluation Algorithms

### Similarity Search Model
![Similarity Search Approach](https://raw.githubusercontent.com/SyedShahzaib790/A-Multi-Approach-Generalized-Framework-for-Automated-Solution-Suggestion-of-Support-Tickets/master/Algo1.png)

### End to End Model Model
![End-to-End Approach] (https://raw.githubusercontent.com/SyedShahzaib790/A-Multi-Approach-Generalized-Framework-for-Automated-Solution-Suggestion-of-Support-Tickets/master/Algo2.png)
