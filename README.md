
# AI FRAUD DETECTION IN PROCUREMENT

 


## Table of Contents

1. [Business Understanding](#business-understanding)
   - [Overview](#overview)
   - [Goal](#goal)
   - [Objectives](#objectives)
   - [Stakeholders](#stakeholders)

2. [Data Understanding](#data-understanding)

3. [Data Preparation](#data-preparation)

4. [Modeling](#modeling)

5. [Conclusion](#conclusion)

6. [Recommendations](#recommendations)

7. [Next Steps](#next-steps)

8. [Deployment](#deployment)
    

9. [Libraries and Tools Used](#libraries-and-tools-used)

10. [License](#license)

11. [Contributing Members](#contributing-members)

12. [Contacts](#contacts)

13. [Repository Structure](#repository-structure)

## Business Understanding

**Overview**
>Procurement fraud is a persistent challenge across sectors, impacting both financial integrity and public trust. Fraud schemes like
bribery, bid rigging, and collusion exploit weaknesses in procurement processes, resulting in inflated costs, resource misallocation,
and compromised service quality. Traditional fraud detection methods, reliant on manual checks and set rules, are often insufficient
due to the evolving nature of fraud schemes. Here, Artificial Intelligence (AI) provides a solution by offering real-time, scalable,
and data-driven insights into procurement practices. AI-powered fraud detection can analyze massive datasets, identify anomalous
patterns, and predict potential fraudulent activities. This project leverages machine learning models to create an
intelligent procurement fraud detection system designed to identify collusive behaviors, inflated invoicing, and other red flags in
procurement transactions. The goal is to support governance efforts, optimize resource use, and foster transparency in public and
private sector procurement.
 

**Goal**
To design and implement an AI-powered fraud detection system for procurement, enhancing fraud identification accuracy and
promoting transparency in financial transactions.
 

**Objectives**
1. To detect anomalous bidding patterns, vendor collusion, and inflated pricing in procurement data.
2. To reduce false positives in fraud detection, ensuring high precision.
3. To establish a transparent reporting system for fraud investigations.
4. To ensure compliance with data protection standards and reduce model bias.
5. To integrate the fraud detection system into existing procurement platforms for government and enterprise use.

## Stakeholders
1. Procurement Officers: Responsible for overseeing purchasing processes, they benefit from AI insights to detect potential fraud early.
2. Compliance and Audit Departments: These teams ensure that procurement activities adhere to legal and ethical standards and would rely on the system for enhanced fraud detection capabilities.
3. Senior Management and Executives: Decision-makers in both public and private sectors, such as CEOs, CFOs, or Directors of Procurement, would support and rely on the project for safeguarding organizational resources.
4. Regulatory Authorities: Government bodies and anti-fraud agencies are interested in upholding fair procurement practices and preventing fraud across industries.
5. IT and Data Science Teams: These teams implement, maintain, and refine the AI system, ensuring its integration with other systems and adapting it to emerging fraud patterns.
6. Vendors and Suppliers: While indirectly affected, vendors would be stakeholders as the system may help in establishing trustworthiness and compliance standards in procurement.

## Data Understanding

The data is from government website [Link Here](https://www.tenders.go.ke/)
## Data Preparation

The data processing step involved analyzing and cleaning published contracts from the government website. A DataUnderstanding class was created to examine the dataset revealing missing values and discrepancies as well as a large number of apparent duplicates most of which were false positives due to partial similarities.
 
 ## Modeling
In our model evaluation process, we tested both Random Forest and and other deep learning models, focusing on recall and accuracy to determine which model generalizes best to unseen data.

**Recall:**

The Random Forest model achieved the highest recall on the training set (1.0000) and a strong recall on the test set (0.8368). However, BiLSTM outperformed it on the test set with a recall of 0.9150, indicating better retention of true positives in unseen data.
BiLSTM also had excellent recall on the training set (0.9886) and demonstrated its robustness with a high recall score of 0.9150 on the test set.
Conclusion: BiLSTM had the best generalization in terms of recall on the test set.
**Accuracy:**

The Random Forest model achieved perfect accuracy on the training set (1.0000) and a high accuracy of 0.9823 on the test set.
BiLSTM performed slightly better, with an accuracy of 0.9984 on the training set and 0.9858 on the test set.
Conclusion: BiLSTM outperformed Random Forest slightly in terms of test set accuracy.
 

## Conclusion
Given both recall and accuracy metrics on the test set, the BiLSTM model stands out as the best-performing model. Its strong performance on the test set suggests better generalization, making it the most reliable choice for accurately predicting on new data.
  

## Recommendations
1. Track model performance metrics over time
2. Set up alerts for performance degradation
3. Regularly tune and retrain your machine learning models to maintain high accuracy, especially as new data trends emerge.

## Next steps
1. Incorporate Related Social Media Platforms: Expand data collection to other platforms (like Facebook or Instagram) if applicable. This broadens the dataset and captures a wider public sentiment.
2. Establish Partnerships with Health Agencies: Partner with health organizations that could benefit from timely disease information, enhancing the project's real-world impact.
3. Develop Clear Data Retention Policies: Define how long data will be stored, particularly sensitive information like location, to ensure ethical data handling.
4. Integrate Disease Forecasting Models: For longer-term insights, experiment with time-series forecasting models, such as ARIMA, Prophet, or LSTM, to predict future trends based on historical data.

 
### Deployment
 

### Installation 
To run the application locally, follow the following steps:

**Clone the repository**

**https:**
```
https://github.com/ProcureGuardAI/Fraud-Detection-Machine-Learning.git
```
**ssh:**
```
git@github.com:ProcureGuardAI/Fraud-Detection-Machine-Learning.git
```
**Navigate to the project directory**

```
cd Fraud-Detection-Machine-Learning.git
```
**Create a virtual environment**

```
python -m venv procure
```
**Activate the virtual environment**

**Windows:**
```
cd procure\Scripts
```
**MacOS/Linux:**
```
source activate
```
**Install dependencies**
```
pip install -r requirements.txt
```
 

## 🔗 Libraries and Tools Used
![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![tensorflow](https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=blue)
![keras](https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![nltk](https://img.shields.io/badge/NLTK-154f3c?style=for-the-badge&logo=python&logoColor=white)
![scikitlearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)


## License
MIT License

## Contributing members
- [Ivy Atieng](https://github.com/Atieng) 
- [Clency Christine](https://github.com/clencyc)
- [James Njoroge](https://github.com/devjamesnjoroge)
- [Movirne Odhiambo]()
 

  
## Contacts
 

Kindly don't hesitate to reach out to the team if you have any questions.

## Repository Structure

```
 Ai Procurement Fraud Detection/
│
└── Deployment/public
    ├── .images
    ├── Models
    ├── data
    ├── Data Report.docx
    ├── LICENCE
    ├── README.md
    ├── diseases.ipynb
    ├── presentation.pdf
    ├── requirements.txt 
```



