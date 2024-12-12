
## Categorical data for Cunningham
Your new assignment requires you to build one multiple regression model. For this analysis, Randall Cunningham would like you to use Python. Your previous assignment required you to build a regression model using numerical data. This new assignment requires you to utilize categorical variables as independent variables. Once again, use [calihospital.txt](/data/calihostpital.txt).

The following are the requirements of your project:
* Use the following variables as independent variables and create dummy variables for all of them: (4 pts.)
  * `Teaching`
  * `DonorType`
  * `Gender`
  * `PositionTitle`
  * `Compensation`
  * `TypeControl`
* Bin the variable `AvlBeds` and create a categorical variable. (2 pts.)
* Use both `Operating Income` and `Operating Revenue` as dependent variables, and build two separate models (2 pts.)

Interpret your findings for these models.

  1. Which model performs better and which variables are included and others are not (1 pt.)

  The `OperRev` model performed better on the measure of adjusted R-squared, which is my typical initial evaluation metric for a model. The `OperInc` model had an adjusted R-squared value of .39, while the OperRev model had an adjusted R-squared value of .73. The `OperInc` model explained approximately 40% of the variability in the Operating Income values - likely we did not include the correct values for properly predicting this, namely that it did not include the variables that are most indicative of income such as `InOperExp` and `NetPatRev`. The `OperRev` model explained approximately 73% of the variability in the values of the Operating Revenue of the hospitals. This is surprisingly good given that neither model that included any of the income, revenue, or expense variables in the data. The `OperRev` model also had an F-statistic of 15.54, with a p-value of <0.0001, indicating that the model achieved statistical significance given a threshold of 0.05. The `OperInc` model also achieved significance, however the p-value was larger and the model had less explanatory value. The models had the same input variables (`Teaching`, `DonorType`, `Gender`, `PositionTitle`, `Compensation`, `TypeControl` and `AvlBeds`). 

2. Provide the interpretation of your variables and whether the results make sense (1 pt.)

  * `OperInc` Model significant variables: 
    * `Small/Rural` - The operating income decreases by 1.4e+07 dollars when a hospital is classified as `Teaching` type Small/Rural. 
    * `Charity` 0.02 - The operating income decreases by 1.4e+07 dollars when a hospital is classified as `DonorType` type Charity.
    * `Comp_46_100k` - The operating income increases by 1.476e+07 dollars when an employee is classified as making between $46,000 and $99,999. 
    * `City/County` - The operating income decreases by 1.242e+08 dollars when a hospital has a `TypeControl` value of City/County. 
    * `District` - The operating income increases by 3.264e+07 dollars when a hospital has a `TypeControl` value of District.  
    * `Non Profit`  - Finally, the operating income increases by 4.244e+07 dollars when a hospital has a `TypeControl` value of Non Profit.  

    Ultimately, `TypeControl` of Non Profit appeared to have the largest impact on the operating income, given that its coefficient was so large. `TypeControl` of City/County had the smallest impact when compared to the other variables that achieved statistical significance of p-values smaller than 0.05.

  * `OperRev` model significant variables:
    * `Teaching` - When the value of the `Teaching` was Teaching, operating revenue increased by 2.107e+08	dollars. 
    * `Small_Rural`	- When the value of the `Teaching` was Small/Rural, operating revenue decreased by 1.013e+08	dollars. 
    * `Charity`	- When the value of the `DonorType` was Charity, operating revenue decreased by 1.013e+08	dollars. 
    * `Alumni` - When the value of the `DonorType` was Alumni, operating revenue increased by 2.107e+08	dollars. 
    * `M`	- When the value of the `Gender` was Male, operating revenue increased by 8.3e+07	dollars. 
    * `F` -	When the value of the `Gender` was Female, operating revenue increased by 2.645e+07	dollars. 
    * `Safety_Inspection_Member` -	When the value of the `PositionTitle` was Safety Inspection Member, operating revenue increased by 8.722e+07	dollars. 
    * `comp_23k_45k` -	When the value of the `Compensation` was between $23,000 and $45,000, operating revenue increased by 8.722e+07	dollars. 
    * `City_County`	-	When the value of the `TypeControl` was City/County, operating revenue decreased by 1.912e+08	dollars.
    * `Non_Profit` -	When the value of the `TypeControl` was Non Profit, operating revenue increased by 1.22e+08	dollars. 	
    * `beds_10_19` -	When the value of the `AvlBeds` was between 10 and 19 beds, operating revenue decreased by 2.648e+08	dollars. 
    * `beds_600_1000`	-	When the value of the `AvlBeds` was between 600 and 999 beds, operating revenue increased by 5.003e+08	dollars. 	1.09e+08	4.588	0.000	2.81e+08	

The results of the variables for these models are logical - things that indicate larger hospitals (e.g., more beds, not run by a city) generally resulted in increases to the operating revenue and operating income. Things that would be associated with smaller hospitals (typically smaller hospitals generate less money because their volumes are smaller), such as having less than 20 beds or being run by a non-profit resulted in decreases to operating revenue and operating income. 