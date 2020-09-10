# telco-churn
Data Science Challenge: churn prediction

Results:
1. Liner Regression and Boosted Tree models both yeild results of approximately 78% accuracy.  

Insights:
1. Customer tenure, Contract, InternetService, and MonthlyCharges all predict churn to varying degrees. 
2. Customers with high tenure are have a low probability of churn. This could indicate customer loyalty or inertia. 
3. A Month-to-Month customer has a high probability of churn. Customers are unlikely to break their long term contracts. 
3. Customers using the Fiber Optic InternetService option are predicted to churn.
4. Customers with high monthly charges are less likely to churn. Higher monthly charges may correlate to more service subscriptions, leading to sticker customers.¶

Actionable Insights:
1. Promote one/year over month-to-month contracts. (Easy)
2. Improve the fiber optic internet service. (Hard)
3. Persude customers to increase their monthly charges. For example, by subscribing to more services. (Medium)
4. Do not let new customers sign up to a month-to-month fiber optic subscription. 

Improvements:
1. Combine addtional service features to calculate the number of subscriptions per customer.
2. Tune the decision tree further for higher accuracy.
3. Try other ML algorithms.
