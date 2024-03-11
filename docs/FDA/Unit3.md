## Unit III: Inferential Statistics & Regression

### 1. Distribution

**Definition:**

- In statistics, a distribution refers to the pattern or spread of values within a dataset.
- It describes the frequencies or probabilities of different outcomes or observations occurring.
- Distributions can be visualized using histograms, probability density functions, or cumulative distribution functions.

**Types of Distributions:**

- **Normal Distribution:** A symmetrical distribution with a bell-shaped curve, characterized by its mean and standard deviation.
- **Uniform Distribution:** A distribution where all outcomes or values have equal probability.
- **Binomial Distribution:** A distribution representing the number of successes in a fixed number of independent Bernoulli trials.
- **Poisson Distribution:** A distribution representing the number of events occurring in a fixed interval of time or space, given a constant rate.

**Use Cases:**

- Understanding the distribution of data is essential for analyzing its characteristics, identifying outliers, and selecting appropriate statistical methods.
- Distributions help in modeling and simulating real-world phenomena, such as stock prices, population growth, and exam scores.

### 2. Normal Distribution

**Definition:**

- The Normal Distribution, also known as the Gaussian distribution or bell curve, is a symmetric probability distribution characterized by its mean and standard deviation.
- It is defined by its probability density function, which has a bell-shaped curve with its peak at the mean.

**Properties:**

- **Symmetry:** The distribution is symmetric around its mean, with half of the data points lying on either side.
- **Central Limit Theorem:** Many natural phenomena tend to follow a normal distribution due to the central limit theorem, which states that the distribution of sample means approaches a normal distribution as the sample size increases.
- **68-95-99.7 Rule:** Approximately 68% of the data falls within one standard deviation of the mean, 95% falls within two standard deviations, and 99.7% falls within three standard deviations.

**Use Cases:**

- Normal distribution is commonly used in statistics and probability theory due to its mathematical tractability and wide applicability.
- It serves as a model for various natural phenomena, such as heights, weights, test scores, and errors in measurements.

### 3. Standard Normal Distribution

**Definition:**

- The Standard Normal Distribution is a specific case of the Normal Distribution with a mean of 0 and a standard deviation of 1.
- It is represented by the z-score, which measures the number of standard deviations a data point is from the mean.

**Properties:**

- **Mean and Standard Deviation:** The mean of the standard normal distribution is 0, and the standard deviation is 1.
- **Z-Score:** The z-score of a data point is calculated as the difference between the data point and the mean, divided by the standard deviation.
- **Standardization:** Converting data to the standard normal distribution by subtracting the mean and dividing by the standard deviation is known as standardization or z-score normalization.

**Use Cases:**

- Standard Normal Distribution facilitates comparisons and calculations involving different datasets by standardizing them onto a common scale.
- It is widely used in hypothesis testing, statistical inference, and probability calculations.

### 4. Central Limit Theorem (CLT)

**Definition:** The Central Limit Theorem (CLT) states that, regardless of the distribution of the population, the sampling distribution of the sample mean tends to be approximately normally distributed as the sample size increases, provided that the sample size is sufficiently large.

**Explanation:**

- The CLT is a crucial concept in statistics, especially in inferential statistics, as it allows us to make inferences about population parameters using sample statistics.
- According to the CLT, even if the population distribution is not normal, the distribution of the sample means approaches a normal distribution as the sample size increases.
- This theorem is applicable to various sampling scenarios, including random sampling and sampling from populations with unknown or non-normal distributions.

**Implications:**

- The CLT enables statisticians and data analysts to use the properties of the normal distribution for making inferences about population parameters, such as the population mean or variance.
- It justifies the use of parametric statistical tests, such as t-tests and ANOVA, which rely on assumptions of normality, even when the underlying population distribution is not normal.

### 5. Standard Error

**Definition:** The standard error is a measure of the variability or precision of an estimator (e.g., sample mean or sample proportion) in estimating a population parameter.

**Explanation:**

- The standard error quantifies the extent to which the sample statistic (e.g., sample mean) is expected to deviate from the population parameter (e.g., population mean).
- It is calculated as the standard deviation of the sampling distribution of the estimator.
- For example, the standard error of the sample mean (\( \sigma_{\bar{x}} \)) is calculated as the population standard deviation (\( \sigma \)) divided by the square root of the sample size (\( n \)).

**Implications:**

- A smaller standard error indicates that the sample statistic is likely to be closer to the population parameter, suggesting higher precision in estimation.
- The standard error is used to calculate confidence intervals and determine the margin of error in estimating population parameters from sample statistics.

### 6. Estimators and Estimates

**Definition:**

- An estimator is a statistic or rule used to estimate a population parameter based on sample data.
- An estimate is the specific value obtained from the sample data when using an estimator to estimate the population parameter.

**Explanation:**

- Estimators are functions of sample data that produce estimates of population parameters. For example, the sample mean (\( \bar{x} \)) is an estimator of the population mean (\( \mu \)).
- Estimators can be point estimators, providing a single value as an estimate, or interval estimators, providing a range of values (confidence interval) as an estimate.
- Estimates are obtained by applying estimators to sample data. For instance, if we compute the sample mean of a dataset, the resulting value is the estimate of the population mean.

**Implications:**

- The choice of estimator can affect the accuracy and precision of estimation. Some estimators may be unbiased but have higher variability (e.g., sample standard deviation), while others may have lower variability but biased (e.g., biased estimator for variance).
- Estimators are evaluated based on their properties, such as unbiasedness, efficiency, and consistency, to ensure reliable estimation of population parameters from sample data.
- Estimates obtained from sample data are used to make inferences and draw conclusions about the population, providing valuable insights for decision-making and hypothesis testing.

### 7. Confidence Interval

**Definition:**

- A confidence interval is a range of values derived from sample data that is likely to contain the true population parameter with a certain level of confidence.
- It provides a measure of the uncertainty associated with estimating population parameters from sample statistics.

**Explanation:**

- Confidence intervals are constructed around point estimates (e.g., sample mean or sample proportion) and are based on the variability of the sampling distribution of the estimator.
- The level of confidence (often denoted as \(1 - \alpha\)) indicates the probability that the confidence interval contains the true population parameter.
- The width of the confidence interval is influenced by the level of confidence and the variability of the estimator, quantified by the standard error.
- Common confidence levels include 90%, 95%, and 99%, corresponding to \(1 - \alpha\) values of 0.90, 0.95, and 0.99, respectively.

**Implications:**

- Confidence intervals provide a range of plausible values for the population parameter, allowing analysts to quantify the uncertainty associated with estimation.
- A narrower confidence interval indicates higher precision in estimation, while a wider interval suggests greater uncertainty.
- Confidence intervals are commonly used in hypothesis testing to assess the significance of observed differences and make inferences about population parameters.

### 8. Student's t Distribution

**Definition:**

- The Student's t distribution (or t distribution) is a probability distribution that is symmetric and bell-shaped, similar to the normal distribution.
- It is used in statistical inference for estimating population parameters, particularly when the sample size is small or the population standard deviation is unknown.

**Explanation:**

- The t distribution is characterized by a single parameter known as the degrees of freedom (df), which depends on the sample size.
- As the sample size increases, the t distribution approaches the standard normal distribution (z distribution).
- The t distribution has heavier tails compared to the normal distribution, making it more robust against the influence of outliers and small sample sizes.

**Implications:**

- The t distribution is commonly used in calculating confidence intervals for estimating population parameters, such as the population mean.
- In hypothesis testing, the t distribution is used to determine critical values and calculate test statistics for testing hypotheses about population parameters.
- The appropriate degrees of freedom for the t distribution depend on the sample size and are crucial for accurate estimation and inference.

### 9. Margin of Error

**Definition:**

- The margin of error is a measure of the uncertainty or variability associated with estimating a population parameter from sample data.
- It represents the maximum likely difference between the point estimate and the true population parameter.

**Explanation:**

- The margin of error is calculated based on the standard error of the estimator and the desired level of confidence for the confidence interval.
- It is typically expressed as a percentage of the point estimate or as an absolute value.
- A smaller margin of error indicates higher precision in estimation, while a larger margin of error suggests greater uncertainty.

**Implications:**

- The margin of error provides a measure of the reliability of estimates obtained from sample data.
- It helps decision-makers assess the precision of estimation and make informed judgments about the reliability of survey results or research findings.
- Minimizing the margin of error requires increasing the sample size or reducing the variability of the estimator, such as by improving measurement accuracy or increasing data quality.

### 10. Introduction to Regression

**Definition:**
Regression analysis is a statistical method used to model the relationship between a dependent variable (response variable) and one or more independent variables (predictor variables). It aims to predict the value of the dependent variable based on the values of the independent variables.

**Explanation:**

- The relationship between the variables is modeled using a mathematical equation, often represented as a straight line in the case of linear regression.
- The regression equation describes how changes in the independent variables are associated with changes in the dependent variable.
- Regression analysis is used for prediction, hypothesis testing, and understanding the relationship between variables.

**Applications:**

- Predicting sales based on advertising spending.
- Estimating housing prices based on factors like square footage, number of bedrooms, and location.
- Analyzing the impact of education, experience, and other factors on income.

### 11. Simple Linear Regression

**Definition:**
Simple linear regression is a regression model that examines the linear relationship between two variables: a single independent variable (X) and a single dependent variable (Y).

**Explanation:**

- In simple linear regression, the relationship between the independent variable (X) and the dependent variable (Y) is represented by a straight line.
- The regression equation for simple linear regression is of the form: Y = β0​ + β1 ​X + ϵ, where:

- Y is the dependent variable.
- X is the independent variable.
- β0​ is the intercept (the value of Y when X=0).
- β1​ is the slope (the change in Y for a one-unit change in X).
- ϵ represents the error term, which accounts for the variability in Y that is not explained by X.
- The goal of simple linear regression is to estimate the values of β0​ and β1​ that best fit the observed data points.

**Applications:**

- Predicting student's test scores based on study hours.
- Estimating the relationship between temperature and ice cream sales.
- Analyzing the association between advertising expenditure and sales revenue.

### 12. Multiple Linear Regression

**Definition:**
Multiple linear regression is an extension of simple linear regression that examines the linear relationship between a dependent variable and two or more independent variables.

**Explanation:**

- - In multiple linear regression, the regression equation is of the form: Y = β0​ + β1 ​X1 ​+ β2 ​X2 ​+…+ βn ​Xn ​+ ϵ, where:
  - Y is the dependent variable.
  - X1​,X2​,…,Xn​ are the independent variables.
  - β0​ is the intercept.
  - β1​,β2​,…,βn​ are the slopes associated with each independent variable.
  - ϵ represents the error term.
- The goal of multiple linear regression is to estimate the values of the coefficients (β0​,β1​,…,βn​) that best fit the observed data points.

**Applications:**

- Predicting house prices based on factors such as square footage, number of bedrooms, and location.
- Estimating crop yield based on factors like temperature, rainfall, and soil nutrients.
- Analyzing the impact of multiple marketing channels on sales revenue.

### 13. Key Concepts in Linear Regression

- **Fitting the Model:** In linear regression, the model parameters (coefficients) are estimated using techniques like ordinary least squares (OLS) regression.
- **Assessing Model Fit:** The goodness-of-fit of the regression model can be assessed using metrics like the coefficient of determination (\(R^2\)), which measures the proportion of variance in the dependent variable explained by the independent variables.
- **Interpreting Coefficients:** The coefficients in the regression equation provide insights into the strength and direction of the relationship between the variables. A positive coefficient indicates a positive relationship, while a negative coefficient indicates a negative relationship.

### 14. Correlation vs. Regression

| Correlation | Regression |
|--|--|
|‘Correlation’, as the name says, it determines the interconnection or a co-relationship between the variables.  |‘Regression’ explains how an independent variable is numerically associated with the dependent variable.  |
|In Correlation, both the independent and dependent values have no difference.|However, in Regression, both the dependent and independent variables are different.|
|The primary objective of Correlation is to find out a quantitative/numerical value expressing the association between the values.|Regression’s main purpose is to calculate the values of a random variable based on the values of a fixed variable.|
|Correlation stipulates the degree to which both variables can move together.|However, regression specifies the effect of the change in the unit in the known variable(p) on the evaluated variable (q).|
|Correlation helps to constitute the connection between the two variables.|Regression helps in estimating a variable’s value based on another given value.|

### 15. SST (Sum of Squares Total)

**Definition:**

- SST represents the total sum of squares, which quantifies the total variability in the dependent variable (Y) around its mean.

**Explanation:**

- SST is calculated by summing the squared differences between each observed value of Y and the mean of Y.
- Mathematically, SST can be expressed as: \(SST = sum (Yi - bar{Y})^2\), where \(Yi\) represents each observed value of Y, and \(bar{Y}\) represents the mean of Y.
- SST captures the total variation in the dependent variable Y, regardless of whether it is explained by the regression model or not.

### 16. SSR (Sum of Squares Regression)

**Definition:**

- SSR represents the sum of squares due to regression, which quantifies the variability in the dependent variable (Y) explained by the regression model.

**Explanation:**

- SSR is calculated by summing the squared differences between the predicted values of Y (obtained from the regression model) and the mean of Y.
- Mathematically, SSR can be expressed as: \(SSR = sum (hat{Y}i - bar{Y})^2\), where \(hat{Y}_i\) represents each predicted value of Y obtained from the regression model, and \(bar{Y}\) represents the mean of Y.
- SSR captures the portion of variation in the dependent variable Y that is explained by the independent variables in the regression model.

### 17. SSE (Sum of Squares Error)

**Definition:**

- SSE represents the sum of squares of residuals or errors, which quantifies the unexplained variability in the dependent variable (Y) by the regression model.

**Explanation:**

- SSE is calculated by summing the squared differences between each observed value of Y and its corresponding predicted value obtained from the regression model.
- Mathematically, SSE can be expressed as: \(SSE = sum (Yi - hat{Y}_i)^2\), where \(Yi\) represents each observed value of Y, and \(hat{Y}i\) represents the predicted value of Y obtained from the regression model.
- SSE captures the portion of variation in the dependent variable Y that is not explained by the independent variables in the regression model.

### 18. R-Squared (Coefficient of Determination)

**Definition:**

- R-squared (often denoted as \(R^2\)) is a statistical measure that represents the proportion of variation in the dependent variable (Y) explained by the independent variables in the regression model.

**Explanation:**

- R-squared is calculated as the ratio of SSR to SST: \(R^2 = {SSR}/{SST}\).
- It ranges from 0 to 1, where 0 indicates that the regression model explains none of the variability in the dependent variable, and 1 indicates that the regression model explains all of the variability.
- R-squared provides insights into the goodness-of-fit of the regression model, with higher values indicating a better fit.

### 19. Adjusted R-Squared

**Definition:**

- Adjusted R-squared is a modified version of R-squared that accounts for the number of independent variables in the regression model.

**Explanation:**

- Adjusted R-squared penalizes the addition of unnecessary independent variables to the model, preventing overfitting.
- It is calculated using the formula: \(Adjusted R^2  = 1 - {(1 - R^2)(n - 1)}/{n - p - 1}\), where \(n\) is the number of observations and \(p\) is the number of independent variables in the model.
- Adjusted R-squared adjusts for the degrees of freedom in the regression model, providing a more reliable measure of the model's goodness-of-fit, especially when comparing models with different numbers of independent variables.

### Key Insights

- SST, SSR, and SSE are components used to assess the overall variability and goodness-of-fit of the regression model.
- R-squared quantifies the proportion of variability in the dependent variable explained by the regression model, while Adjusted R-squared provides a more conservative measure that adjusts for model complexity.

### 20. Multiple Linear Regression

**Definition:**
Multiple Linear Regression is a statistical technique used to model the linear relationship between a dependent variable (Y) and two or more independent variables (X₁, X₂, ..., Xₙ).

**Explanation:**

- The multiple linear regression equation is represented as:
  \[ Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε \]
  Where:
  - \(Y\) is the dependent variable.
  - \(X₁, X₂, ..., Xₙ\) are the independent variables.
  - \(β₀, β₁, β₂, ..., βₙ\) are the coefficients (intercept and slopes) representing the relationship between the independent variables and the dependent variable.
  - \(ε\) is the error term, representing the unexplained variation in the dependent variable.

**Applications:**

- MLR is widely used in various fields, such as economics, finance, marketing, and social sciences, to analyze the impact of multiple factors on an outcome of interest.
- Examples include predicting house prices based on factors like square footage, number of bedrooms, and location; analyzing the effect of advertising expenditure, pricing strategies, and customer demographics on sales revenue; and assessing the relationship between education level, experience, and income.

### 21. Significance of p-value

In statistical hypothesis testing, the p-value is a measure of the strength of evidence against the null hypothesis. In the context of MLR, the significance of the p-value associated with each coefficient (slope) provides insights into the importance of the corresponding independent variable in explaining the variation in the dependent variable.

**Explanation:**

- In MLR, each coefficient (\(β₁, β₂, ..., βₙ\)) represents the change in the dependent variable for a one-unit change in the corresponding independent variable, holding other variables constant.
- The null hypothesis (\(H₀\)) states that there is no relationship between the independent variable and the dependent variable (i.e., the coefficient is equal to zero).
- The p-value associated with each coefficient indicates the probability of observing the estimated coefficient value (or a more extreme value) if the null hypothesis is true.
- A small p-value (typically less than a predetermined significance level, such as 0.05) suggests strong evidence against the null hypothesis, indicating that the independent variable is significantly related to the dependent variable.
- Conversely, a large p-value suggests weak evidence against the null hypothesis, indicating that the independent variable may not be statistically significant in explaining the variation in the dependent variable.

**Interpretation:**

- If the p-value associated with a coefficient is less than the significance level (e.g., 0.05), the coefficient is considered statistically significant, and the corresponding independent variable is considered to have a significant effect on the dependent variable.
- If the p-value is greater than the significance level, the coefficient is not considered statistically significant, and the corresponding independent variable may not have a significant effect on the dependent variable.

**Implications:**

- Assessing the significance of p-values helps in identifying the most influential predictors in the regression model and understanding the strength of the relationship between the independent variables and the dependent variable.
- It aids in model selection, variable selection, and interpretation of regression results, guiding decision-making in various applications.
