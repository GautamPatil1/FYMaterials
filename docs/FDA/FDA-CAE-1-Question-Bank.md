# Foundation of Data Analytics CAE 1 Question Bank Solution

## 1.Differentiate data analysis and data analytics

- **Data Analysis:** Data analysis is the process of inspecting, cleaning, transforming, and modeling data to extract useful information, infer conclusions, and support decision-making. It involves techniques like data mining, statistical analysis, and machine learning.

- **Data Analytics:** Data analytics is a broader term that encompasses the entire process of examining data sets to draw conclusions about the information they contain. It involves not only the analysis of data but also the application of statistical and mathematical techniques to derive insights, trends, and patterns. Data analytics often includes processes such as data visualization, predictive modeling, and optimization.

| S.No. | Data Analytics | Data Analysis |
| --- | --- | --- |
| 1. | It is described as a traditional form or generic form of analytics. | It is described as a particularized form of analytics. |
| 2. | It includes several stages like the collection of data and then the inspection of business data is done. | To process data, firstly raw data is defined in a meaningful manner, then data cleaning and conversion are done to get meaningful information from raw data. |
| 3. | It supports decision making by analyzing enterprise data. | It analyzes the data by focusing on insights into business data. |
| 4. | It uses various tools to process data such as Tableau, Python, Excel, etc. | It uses different tools to analyze data such as Rapid Miner, Open Refine, Node XL, KNIME, etc. |
| 5. | Descriptive analysis cannot be performed on this. | A Descriptive analysis can be performed on this. |
| 6. | One can find anonymous relations with the help of this. | One cannot find anonymous relations with the help of this. |
| 7. | It does not deal with inferential analysis. | It supports inferential analysis. |

## 2.Explain data visualization and infographics

- **Data Visualization:** Data visualization is the graphical representation of data and information. It uses visual elements like charts, graphs, and maps to make complex datasets more understandable and accessible. Data visualization helps in identifying trends, patterns, and outliers in data, facilitating better decision-making and communication.
- **Infographics:** Infographics are a specific type of data visualization that combines images, charts, and text to convey complex information in a visually appealing and easy-to-understand format. Infographics are often used to present statistical data, research findings, or educational content in a concise and engaging manner.

## 3.Describe types of Data analytics with examples

- **Descriptive Analytics:** Descriptive analytics focuses on summarizing historical data to understand what has happened in the past. It includes techniques such as data aggregation, data mining, and reporting. For example, generating a report on monthly sales figures for a retail store.
- **Predictive Analytics:** Predictive analytics involves using historical data to make predictions about future events or trends. It uses techniques like regression analysis, time series forecasting, and machine learning algorithms. For example, predicting customer churn based on past behavior and demographic data.
- **Prescriptive Analytics:** Prescriptive analytics aims to recommend actions or decisions based on predictive models and optimization techniques. It helps in determining the best course of action to achieve a specific outcome. For example, recommending personalized marketing strategies based on customer segmentation and predictive models.

## 4.Describe the concept of Central Tendency Measures and its role in measuring data dispersion

- **Central Tendency Measures:** Central tendency measures are statistical measures that represent the center or average value of a dataset. The commonly used measures of central tendency are the mean, median, and mode. The mean is the arithmetic average of all the values, the median is the middle value when the data is sorted, and the mode is the value that appears most frequently.
- **Role in Measuring Data Dispersion:** Central tendency measures provide a summary of the typical or central value of a dataset. However, they do not provide information about the spread or variability of the data points around the central value. To measure data dispersion, additional statistical measures such as variance, standard deviation, and range are used. These measures quantify the spread of data points around the central value, providing insights into the variability of the dataset.

## 5.Calculate the mean, median, and mode for the following ungrouped datasets

### Ages of students in a college: [19, 21, 20, 22, 23, 19, 20, 22, 21, 19]

- **Mean:** (19 + 21 + 20 + 22 + 23 + 19 + 20 + 22 + 21 + 19) / 10 = 206 / 10 = 20.6
- **Median:** Since the dataset has 10 values, the median is the average of the 5th and 6th values when sorted. Sorted dataset: [19, 19, 19, 20, 20, 21, 21, 22, 22, 23]. Median = (20 + 21) / 2 = 20.5
- **Mode:** The mode is the value that appears most frequently. In this case, both 19, 20, 21, and 22 appear twice, making them the modes of the dataset.

### Number of daily customers for a store: [50, 48, 45, 52, 48, 50, 45]

- **Mean:** (50 + 48 + 45 + 52 + 48 + 50 + 45) / 7 = 338 / 7 ≈ 48.29
- **Median:** Since the dataset has 7 values, the median is the 4th value when sorted. Sorted dataset: [45, 45, 48, 48, 50, 50, 52]. Median = 48
- **Mode:** The mode is the value that appears most frequently. In this case, both 45, 48, 50 appear twice, making them the modes of the dataset.

## 6. To determine the mean, median, and mode for the given grouped dataset of income levels, we'll follow these steps

1. Calculate the midpoint for each income range.
2. Multiply the midpoint of each range by its frequency to find the "weighted" value.
3. Calculate the total weighted value and the total frequency.
4. Use the formula for the mean to calculate the average income.
5. Find the median by determining the cumulative frequency and identifying the middle interval.
6. Identify the mode by determining the income range with the highest frequency.

Let's proceed with the calculations:

1. **Calculate Midpoints:**
    - Midpoint of 30-39: (30 + 39) / 2 = 34.5
    - Midpoint of 40-49: (40 + 49) / 2 = 44.5
    - Midpoint of 50-59: (50 + 59) / 2 = 54.5
    - Midpoint of 60-69: (60 + 69) / 2 = 64.5
2. **Calculate Weighted Values:**
    - Weighted value for 30-39: 7 \* 34.5 = 241.5
    - Weighted value for 40-49: 12 \* 44.5 = 534
    - Weighted value for 50-59: 8 \* 54.5 = 436
    - Weighted value for 60-69: 5 \* 64.5 = 322.5
3. **Calculate Totals:**
    - Total weighted value = 241.5 + 534 + 436 + 322.5 = 1534
    - Total frequency = 7 + 12 + 8 + 5 = 32
4. **Calculate Mean:**
    - Mean = Total weighted value / Total frequency = 1534 / 32 ≈ 47.94
5. **Calculate Median:**
    - To find the median, we need to identify the cumulative frequency.
    - Cumulative Frequency: 7, 7 + 12 = 19, 19 + 8 = 27, 27 + 5 = 32
    - Since the median falls within the interval 40-49, we interpolate using the formula: Median = Lower limit of median class + (N/2 - CF) \* Width of class / Frequency of median class = 40 + (16 - 7) \* 10 / 12 ≈ 40 + (9 \* 10 / 12) ≈ 40 + 7.5 ≈ 47.5
6. **Calculate Mode:**
    - The mode is the income range with the highest frequency, which is the range 40-49.

Therefore, for the given grouped dataset:

- Mean ≈ $47,940
- Median ≈ $47,500
- Mode: $40,000 - $49,999

## 7. Investigate the relationship between Mean, Median, Mode

- Mean, median, and mode are measures of central tendency.
- In symmetrical distributions, mean, median, and mode tend to be close to each other and may coincide.
- In skewed distributions, they might differ. For instance, in positively skewed data, the mean is typically larger than the median, which, in turn, is larger than the mode.
- Understanding their relationship helps grasp the distribution's shape and central tendency.

## 8. Describe measures of variation of a dataset: quartiles, variance, range

- **Quartiles:** Divide data into quarters. First quartile (Q1) is the 25th percentile, median (Q2) is the 50th percentile, and third quartile (Q3) is the 75th percentile.
- **Variance:** Measures how data points vary from the mean. Calculated by summing the squared differences between each data point and the mean, then dividing by the number of data points.
- **Range:** The difference between the maximum and minimum values in a dataset. Simple but sensitive to outliers.

## 9. Calculate the variance and range for the study hours dataset

- Calculate the mean: (10 + 12 + 8 + 15 + 14 + 11 + 17 + 20 + 5 + 22 + 19) / 11 = 14.
- Variance: Calculate the squared differences between each data point and the mean, then find the average.
- Range: The difference between the maximum (22) and minimum (5) values.

## 10. Calculate the variance, range, and quartiles for the website traffic data

To calculate the variance, range, and quartiles for the website traffic data, let's first organize the data:

Website Traffic Data: \[32, 35, 30, 28, 45, 38, 42, 27, 33, 50, 48, 29, 31, 40, 36, 41, 49, 47, 52, 26, 44\]

Now, let's proceed with the calculations:

1. **Variance:**
    - Variance measures the spread or dispersion of the dataset around its mean.
    - Formula: Variance\=1�∑�\=1�(��−�ˉ)2Variance\=n1​∑i\=1n​(xi​−xˉ)2, where xi​ are the individual data points, x is the mean, and n is the number of data points.
    - First, calculate the mean:

![Mean](mean.png)

- Now, calculate the squared differences between each data point and the mean, then find their average:

![Variance](variance.png)

2. **Range:**

    - Range is the difference between the maximum and minimum values in the dataset.
    - Range = Maximum value - Minimum value.
    - Maximum value = 52, Minimum value = 26.
    - Range = 52 - 26 = 26.

3. **Quartiles:**

    - Quartiles divide the dataset into four equal parts.
    - We will use the Excel function to find quartiles.
    - Excel Function: `QUARTILE.INC(array, quart)`, where `array` is the dataset and `quart` is the quartile number (1 for Q1, 2 for Q2, and 3 for Q3).
    - Quartile 1 (Q1) = 31
    - Quartile 2 (Q2, Median) = 36
    - Quartile 3 (Q3) = 42

So, summarizing the calculations:

- Variance ≈ 18.83
- Range = 26
- Quartiles: Q1 = 31, Q2 = 36, Q3 = 42

## 11. Describe the importance of Data preparation for Data Analytics

- Data preparation involves cleaning, transforming, and organizing data.
- It ensures data quality, reliability, and consistency.
- Properly prepared data leads to accurate analysis and meaningful insights.
- Data preparation reduces errors, biases, and ensures compatibility with analysis techniques.

## 12. Summarize the benefits of data Preparation

1. **Improved Data Quality:**
    - Data preparation involves cleaning, filtering, and transforming raw data to ensure its accuracy, completeness, and consistency. By identifying and correcting errors, removing duplicates, and handling missing values, data preparation enhances the overall quality of the dataset.

2. **Enhanced Analysis Accuracy:**
    - High-quality data leads to more accurate analysis and reliable insights. Properly prepared data reduces the risk of errors, biases, and misinterpretations in analysis results, enabling data analysts to make informed decisions based on trustworthy information.

3. **Increased Efficiency:**
    - Data preparation streamlines the analysis process by organizing and structuring data in a format suitable for analysis. By removing unnecessary information, aggregating data, and standardizing formats, data preparation simplifies data manipulation tasks and saves time during analysis.

4. **Facilitated Data Integration:**
    - Data preparation involves integrating data from multiple sources into a unified dataset. By combining data from disparate sources and standardizing data formats, data preparation enables seamless integration and ensures compatibility between different datasets, making it easier to perform comprehensive analysis.

5. **Effective Data Exploration:**
    - Well-prepared data sets the foundation for thorough data exploration and discovery. By organizing data into meaningful categories, identifying relevant variables, and structuring data for analysis, data preparation empowers data analysts to explore trends, patterns, and relationships within the data more effectively.

6. **Optimized Model Performance:**
    - In machine learning and predictive modeling, the quality of the training data significantly impacts model performance. Properly prepared data, free from noise, inconsistencies, and outliers, helps build more accurate and robust models, leading to better predictive performance and generalization to new data.

7. **Improved Decision-Making:**
    - Reliable data preparation ensures that decision-makers have access to accurate, timely, and relevant information for making informed decisions. By providing trustworthy insights derived from high-quality data, data preparation contributes to better decision-making outcomes and helps organizations achieve their strategic objectives.

8. **Compliance and Risk Management:**
    - Data preparation plays a crucial role in ensuring compliance with regulatory requirements and mitigating risks associated with data governance. By adhering to data privacy regulations, maintaining data integrity, and implementing data security measures, data preparation helps organizations minimize legal and reputational risks associated with data handling.

## 13. Analyse the Data Preparation process and list down the steps

Data Preparation involves several steps:

1. **Data Collection:** Gather data from various sources.
2. **Data Cleaning:** Identify and correct errors, missing values, and inconsistencies.
3. **Data Transformation:** Convert data into a suitable format for analysis.
4. **Data Integration:** Combine data from different sources into a single dataset.
5. **Data Reduction:** Reduce the dataset size while retaining important information.
6. **Data Formatting:** Standardize data formats and structures.
7. **Data Enrichment:** Enhance data by adding additional attributes or information.
8. **Data Validation:** Ensure data accuracy and reliability.

## 14. Create website table using Scope and Span attribute

The scope attribute defines the set of data cells a header cell applies to. The span attribute specifies the number of columns or rows a cell should span.

Example:

```html
<table border="1">
    <tr>     
        <th scope="col">Month</th>
        <th scope="col">Sales</th>     
        <th scope="col">Profit</th>   
    </tr>   
    
    <tr>     
        <td scope="row">January</td>     
        <td>$1000</td>     
        <td rowspan="2">$200</td>   
    </tr>   

    <tr>     
        <td scope="row">February</td>     
        <td>$1500</td>   
    </tr> 
</table>
```

## 15. Outline ways to apply a Table Header, Body, and Footer in a website table? Give one example

**Header:** Use the `<thead>` element to define the header section.

**Body:** Use the `<tbody>` element to define the body section.

**Footer:** Use the `<tfoot>` element to define the footer section.

Example:

```html
<table border="1">
    <thead>     
       <tr>       
           <th>Column 1</th>       
           <th>Column 2</th>     
       </tr>   
    </thead>   
    <tbody>     
       <tr>       
           <td>Data 1</td>       
           <td>Data 2</td>     
       </tr>   
    </tbody>   
    <tfoot>     
       <tr>       
           <td>Total</td>       
           <td>Sum</td>     
       </tr>   
    </tfoot> 
</table>
```

## 16. Illustrate the difference between Table and Database Table

- **Table:** A table in HTML is used for organizing data in rows and columns within a web page.
- **Database Table:** A database table is a collection of related data organized in a tabular format within a relational database management system (RDBMS).

## 17. State the components of Database Table? Elaborate on each component

1. **Columns/Fields:**

    - Columns or fields are the vertical divisions within a database table.
    - Each column represents a specific attribute or characteristic of the data being stored.
    - For example, in a table storing information about employees, columns could include "EmployeeID", "FirstName", "LastName", "Email", "Department", etc.
    - Each column has a defined data type (such as integer, text, date, etc.) and constraints that define the type of data it can hold.

2. **Rows/Records:**
    - Rows or records are the horizontal divisions within a database table.
    - Each row represents a single instance or entry of data within the table.
    - For example, in a table storing employee information, each row represents a specific employee's details, such as their ID, name, email, etc.

3. **Primary Key:**
    - The primary key is a column or a set of columns that uniquely identifies each row in the table.
    - It ensures that each row in the table is unique and can be uniquely identified.
    - Typically, primary keys are used to enforce data integrity and establish relationships between tables in a relational database.
    - For example, in an "Employee" table, the "EmployeeID" column could serve as the primary key, ensuring that each employee has a unique identifier.

4. **Foreign Key:**
    - A foreign key is a column or a set of columns in a table that establishes a relationship with another table's primary key.
    - It enforces referential integrity by ensuring that values in the foreign key column match values in the primary key column of the related table.
    - Foreign keys are used to create relationships between tables, allowing for data consistency and integrity.
    - For example, in an "Orders" table, the "CustomerID" column could serve as a foreign key, linking each order to the corresponding customer in the "Customers" table.

5. **Constraints:**
    - Constraints are rules or conditions applied to columns in a database table to maintain data integrity and enforce business rules.
    - Common constraints include NOT NULL (ensures a column cannot contain NULL values), UNIQUE (ensures that all values in a column are unique), CHECK (ensures that values in a column meet specified conditions), etc.
    - Constraints help ensure data accuracy, consistency, and reliability by preventing invalid or inappropriate data from being inserted into the table.
    - For example, a constraint could be applied to a "DateOfBirth" column to ensure that the date entered is in the past and not in the future.

## 18. Mark the importance of dealing with duplicate data in data analysis

1. **Data Accuracy:** Duplicate data can skew analysis results and lead to inaccurate conclusions. For instance, if duplicate entries are included in calculations, they can artificially inflate counts, averages, or other statistical measures, leading to misleading insights.

2. **Data Quality:** Duplicate data degrades the overall quality of the dataset. It can introduce inconsistencies and errors, making the dataset less reliable for analysis. Cleaning up duplicates improves data quality and ensures that analysis is based on accurate and trustworthy information.

3. **Resource Optimization:** Analyzing duplicate data wastes computational resources and time. Processing redundant data not only slows down analysis but also increases storage requirements. Removing duplicates optimizes resource utilization, making analysis more efficient and cost-effective.

4. **Decision Making:** Data-driven decisions rely on the integrity and accuracy of the underlying data. Duplicate data can lead to incorrect decisions, resulting in poor outcomes for businesses or organizations. By eliminating duplicates, decision-makers can have confidence in the validity of the insights derived from the analysis.

5. **Model Performance:** In predictive modeling and machine learning, duplicate data can bias models and degrade their performance. Models trained on duplicated instances may overfit to the duplicated patterns, leading to poor generalization and predictive accuracy. Cleaning duplicates ensures that models are trained on diverse and representative data, improving their performance.

6. **Data Consistency:** Duplicate data can introduce inconsistencies in reporting and analysis. For example, duplicate customer records in a sales dataset may lead to discrepancies in revenue calculations or customer segmentation. Removing duplicates ensures data consistency across the organization and facilitates accurate reporting.

7. **Data Privacy and Security:** Duplicate data increases the risk of data breaches and privacy violations. Redundant copies of sensitive information provide more entry points for unauthorized access. By identifying and removing duplicates, organizations can mitigate security risks and protect sensitive data from unauthorized disclosure or misuse.

8. **Regulatory Compliance:** Many regulatory frameworks, such as GDPR (General Data Protection Regulation) and HIPAA (Health Insurance Portability and Accountability Act), require organizations to maintain accurate and up-to-date records while safeguarding individuals' privacy rights. Dealing with duplicate data is essential for compliance with these regulations.

## 19. Suggest alternative methods for overcoming data duplication

1. **Data Validation Rules:**
    - Implement data validation rules at the data entry stage to prevent the introduction of duplicate records. For example, require unique identifiers for each entry or enforce constraints to ensure data integrity.

2. **Use of Unique Identifiers:**
    - Assign unique identifiers to each record or entity in the dataset. These identifiers can be autogenerated or based on specific attributes that guarantee uniqueness. By using unique identifiers, duplicate records can be easily identified and managed.

3. **Data Matching Algorithms:**
    - Utilize data matching algorithms and fuzzy matching techniques to identify similar or identical records within the dataset. These algorithms compare attributes of different records and flag potential duplicates based on similarity thresholds.

4. **Probabilistic Record Linkage:**
    - Implement probabilistic record linkage techniques to identify and merge duplicate records across multiple datasets. These methods use statistical models to assess the likelihood of records representing the same entity and consolidate them accordingly.

5. **Manual Inspection and Cleaning:**
    - Conduct manual inspection and cleaning of the dataset to identify and resolve duplicate records. This approach involves human intervention to review and reconcile potentially duplicate entries based on domain knowledge and contextual information.

6. **Data Deduplication Software:**
    - Use specialized data deduplication software or tools designed to automatically detect and remove duplicate records from large datasets. These tools employ algorithms and heuristics to identify duplicate patterns and streamline the deduplication process.

7. **Regular Data Audits:**
    - Conduct regular data audits and quality checks to proactively identify and address duplicate records. Establishing a systematic process for data auditing helps ensure data cleanliness and consistency over time.

8. **Data Governance Policies:**
    - Implement data governance policies and procedures to govern the creation, maintenance, and deletion of data records. Clear guidelines and standards for data management help minimize the occurrence of duplicate data and ensure compliance with organizational requirements.

9. **Cross-Referencing with Master Data:**
    - Cross-reference dataset records with a master data repository or reference dataset containing unique and authoritative records. By comparing dataset entries against a central source of truth, duplicates can be easily identified and resolved.

10. **Regular Data Cleansing:**
    - Schedule regular data cleansing activities to identify and remove duplicate records from the dataset. Establishing routine data maintenance practices helps keep the dataset clean and free from redundancy.

## 20. Describe the procedure for removing Duplicate Values in Excel

1. **Select Data Range:**
    - Open the Excel spreadsheet containing the data from which you want to remove duplicates.
    - Select the range of cells or columns that contain the data from which you want to remove duplicates.

2. **Access Data Tools:**
    - Navigate to the "Data" tab on the Excel ribbon at the top of the window. This tab contains various data-related tools and commands.

3. **Initiate Remove Duplicates:**
    - In the "Data" tab, locate the "Data Tools" group.
    - Click on the "Remove Duplicates" button. This action will open the "Remove Duplicates" dialog box.

4. **Choose Columns:**
    - In the "Remove Duplicates" dialog box, Excel automatically selects all columns in your selected range.
    - If you only want to remove duplicates based on specific columns, uncheck the columns that you don't want to consider for duplicate removal.

5. **Confirm Removal:**
    - After selecting the appropriate columns, click the "OK" button. Excel will then analyze the selected range and identify duplicate values based on the chosen columns.

6. **Review Confirmation Dialog:**
    - A confirmation dialog box will appear, informing you about the number of duplicate values found and the number of unique values remaining after removal.
    - Review the information provided and click "OK" to proceed with removing duplicates.

7. **Completion Message:**
    - Once the removal process is complete, Excel will display a message indicating the number of duplicate values removed and the number of unique values remaining.
    - Click "OK" to close the message box and return to the Excel worksheet.

8. **Review Results:**
    - Excel will remove duplicate values from the selected range based on the criteria specified.
    - Review the data to ensure that duplicates have been successfully removed and that the remaining values meet your requirements.

9. **Save Changes:**
    - If you're satisfied with the removal of duplicates, remember to save your Excel spreadsheet to retain the changes.
