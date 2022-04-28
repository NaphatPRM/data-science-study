# Statistics Write Up

## Part 1: Regression

All questions in this section pertain to the `bike-sharing.csv` dataset.

#### 1. (5 points)
**Question**:
Interpret the co-efficient for `weathersit` according to simple linear regression. Using plain English, what does this coefficient mean? (one or two sentences should be sufficient)

**Answer**:
Correlation coefficient indicates how much of the change in the dependent variable can be explained by change in the independent variable.

#### 2. (9 points)
**Question**:
Compare the co-efficient on `weathersit` in a simple regression model (only one independent variable) and the coefficient in the multiple regression model that includes all variables.
- Did the coefficient go up or down?
- Why do you think this is the case?
 
**Answer**:
See rubric.

#### 3. (9 points)
**Question**:
Which variable would you say is the "most important" for predicting bike usage? Defend your choice.

**Answer**:
Multiple answers work - see rubric.

#### 4. (9 ponts)
**Question**:
- In plain English, what is R-squared value?
- What does the R-squared value imply about multiple linear regression models when compared to simple linear regression models?
- Does higher R-squared value always mean that a model is better? Why? How should you best utilize R-squared to examine the goodness of fit for your linear model?

**Answer**:
- The coefficient of determination, denoted R2 or r2 and pronounced "R squared", is the proportion of the variance in the dependent variable that is predictable from the independent variable(s).
- R-squared value increases as the number of variables in the model is increased (R2 is monotone increasing with the number of variables included—it will never decrease). 
The increase indicates a stronger relationship between the depedent variable and the independent variables used. 
- In our case, the higher R-squared value does not necessarily mean the multiple linear model is better, but the model does better fit the observations. In an overfitting condition, an incorrectly high value of R-squared is obtained, even when the model actually has a decreased ability to predict. 
Numbers like R-squared should never by itself be used to prove the goodness of fit. It should be used with multiple other statistical examination.

#### 5. (8 points)
**Question**:
Is there a difference between training and testing MSE? Why is comparing this important?

**Answer**:
Training MSE is calculated on the data that the model was fitted and testing MSE is on a different set of data. Comparing them is good because it shows how good the model is on general data, and can catch overfit models.

## Part 2: Statistical Tests

All questions in this section pertain to the `college-data.csv` dataset. For each of the scenarios below, you are expected to answer the following questions:
- What is your null hypothesis? What is your alternative hypothesis?
- What test do we use to answer this question? Why?
- Can we reject the null hypothesis? Why? Be sure to mention the numbers that are part of your reasoning.

We will use the significance level α = 0.05 for all the scenarios.

**Note**: We acknowledge that the binary framework of gender in this dataset does not remotely represent all the possible gender identities that people may have.

### Scenario One (12 points)
The mean height of U.S. adults ages 20 and older is about 66.5 inches (69.3 inches for males, 63.8 inches for females). In our sample data, we have a sample of 435 college students from a single college. We want to determine whether the mean height of students at this college is significantly different than the mean height of U.S. adults ages 20 and older.

**Answer**:
- One sample t-test.
- The calculated test value is 5.810. Since p < 0.001, we reject the null hypothesis that the mean height of students at this college is equal to the hypothesized population mean of 66.5 inches and conclude that the mean height is significantly different than 66.5 inches.
- The average height of students at this college is about 1.5 inches taller than the U.S. adult population average (95% CI [1.013, 2.050]). 

### Scenario Two (12 points)
In our sample data, students reported their typical time to run a mile, and whether or not they were an athlete. We want to know whether the average time to run a mile is different for athletes versus non-athletes.

**Answer**:
- Independent two-sample t-test. 
- There was a significant difference in mean mile time between non-athletes and athletes t_(315.846) = 15.047, p < 0.001.
- The average mile time for athletes was 2 minutes and 14 seconds faster than the average mile time for non-athletes.

### Scenario Three (12 points)
The students in the sample completed all 4 placement tests for four subject areas - English, Reading, Math, and Writing - when they enrolled in the university. The scores are out of 100 points, and are present in the dataset. We want to test if there was a significant difference between the average of the English test scores and that of the Math test scores.

**Answer**:
- Paired sample t-test.
- There was a significant average difference between English and Math scores t_(397) = 36.313, p < 0.001.
- On average, English scores were 17.3 points higher than Math scores (95% CI [16.36, 18.23]).

### Scenario Four (12 points)
In the sample data, the students also reported their class rank, as well as whether they live on campus. We want to test if there is a relationship between one's class rank and whether they live on campus.

**Answer**:
- Chi-square test as a goodness of fit test.
- Since the p-value is less than our chosen significance level 0.05, we can reject the null hypothesis, and conclude that there is an association between class rank and whether or not students live on-campus.
- There was a significant association between class rank and living on campus Χ2(1) = 138.9, p < .001.

### Scenario Five (12 points)
In the sample dataset, respondents were asked their gender and whether or not they were a cigarette smoker. There were three answer choices: Nonsmoker, Past smoker, and Current smoker. We want to test the relationship between smoking behavior (nonsmoker, current smoker, or past smoker) and gender (male or female).

**Answer**:
- Chi-square test of independence.
- Since the p-value is greater than our chosen significance level 0.05, we do not reject the null hypothesis. Rather, we conclude that there is not enough evidence to suggest an association between gender and smoking.
- No association was found between gender and smoking behavior Χ2(2)> = 3.171, p = 0.205.



## Part 3: Socially Responsible Computing
#### 1. (6 points)
**Question**:
Consider the bike-sharing.csv dataset you ran statistical tests on in this assignment.

a.) What factors might be influencing the bike-sharing.csv data that are not being shown in the dataset? List at least 3 possible factors. The factors could be additional variables or factors that are not quantifiable.
**Answer**:
There are at least three possible factors, which is
- Station placement isn’t equitable and follows patterns of existing infrastructure.
- Station use differs by neighborhood.
- Other general biases such as selection bias.

b.) List one category for which it could be helpful to separate the bike-sharing.csv data into groups before analyzing it. 
This category may or may not be represented in the existing dataset. Describe a context (project, question, goals, etc.) for which separating the data by that category is important and explain why separating the data is the right choice for that context.
**Answer**:
- The area category (such as neighbourhood, would be better if the percentage of race/high low income). This category will help analyzing the causation of bike usage and the area they are in. The information about the area could tell about the 
density of people compared to an area (this could judge whether using the bicycle is possible or not). The race and income
will also tell about the popularity amoung race (and with enough information, could analyze the distribution of advertisement
of the bike sharing system), and also the prevention of "selection bias".

#### 2. (5 points)
**Question**:
Explain what you learnt in your own words. How do you see this being an issue with any projects you will be working on in the future.
**Answer**: 
This could be an issue if we consider the situation with more than one cluster of people/objects in the experiment.
Even though we have the same trends among the population, you could have the wrong causalities if we consider both 
group sesimultaneously. For example (based on the video), if the money makes people and cat more sad, but cats are
happier and richer than human, the resul of the graph could make a positive correlation between having a money and
being happy, which is contradicted. 

This could be a problem on the project when there is a potential clustering within the data. For example our group Cheerios,
we consider the amount od sugar/sugat-substitute in the cereals. Therefore, there is a possibility that cereals could be categorized based on the main ingredients and the target of consumers, leading to some misleading correlation such as
(possibly) "the more advertizing of "heart-healthy" on the label, the more "sugar-substitute" occurs on the products.
However, there is the cluster between the products with the grains in it and it's not, with both having
the inverse proportion between "heart-healthy" advertising and the amount of sugar-substitute, but grain also
contain the sugar-substitute in general.

#### 3. (7 points)
**Question**:
a.) State the statistical results (in terms of p-values) supporting the claim that “Democrats are bad for the economy”, describing the terms you used to get this result.
**Answer**:
Based on my experiment, I found that the result as follows make the paper publishable :
- Consider only the Governor for the Democrats, and define economy just by GDP with p-value 0.01
- Consider only the Senator for the Democrats, and define economy just by GDP with p-values 0.02
- Consider more than ont type (two/three/four out of President, Governor, Senators, and Representative) compared with any
measure such as selecting all will be able to publish on ony GDP (negative on 0.01 P-value). The other three measures
aer either unpublishable or support that "Democrats are good for the economy"
employment has a p-values of 0.01)

b.) State the statistical results (in terms of p-values) supporting the claim that “Republicans are bad for the economy”, describing the terms used.
**Answer**:
- Consider only Governors and using the GDP as the sole definition of the economy with the p-values of 0.01
- Consider only Representative and using the GDP as the sole definition of the economy with the p-values of 0.01
- Consider everyone in the Republicans and using the GDP as the sole definition of the economy with the p-values 0.01
- Consider only President and using the inflation as the sole definition of the economy with the p-values 0.01

c.) Write a short reflection about your above experiments. Whether specific to the data or broadly applicable to statistical analysis of all kinds, what should you avoid or emphasize if you present or publish the results of such an analysis?
**Answer**:
Based on the data I get from the experiment, I think that the population included and the definition of the main
hypothesis shoud be mentioned/defined so that people will not confused or misinterpret. For example in this case,
if we consider only GDP and either Governors or Representatives, the claim that “Republicans are bad for the economy” will
be supported (with p-values less than 0.01). However, if we use either Governors or Representatives on the employment 
measure, this information would be the counter of the claim “Republicans are bad for the economy” instead such that it makes the result in the different direction.