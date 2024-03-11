## Unit II: Data Preparation & Identification of trends in data analytics ##

### A. Data Preparation

**1. Importing Data:**

- **From CSV, Excel, etc.:** Data can be imported from various file formats such as CSV (Comma-Separated Values), Excel spreadsheets, JSON (JavaScript Object Notation), XML (eXtensible Markup Language), and more. Importing data from these formats involves reading the files into software tools or programming environments like Python, R, or SQL.
- **From Website Tables:** Data can be extracted from tables on websites using web scraping techniques. Web scraping involves parsing the HTML structure of web pages to extract data from specific elements, such as tables, and then converting it into a structured format for further analysis.
- **From Database Tables:** Data stored in relational databases (e.g., MySQL, PostgreSQL, SQLite) can be imported into data analytics tools or programming environments using database connectivity libraries or SQL queries. This involves establishing a connection to the database and querying the required tables to retrieve the data.

**2. Data Cleaning:**

- **Handling Missing Values:** Missing values in the dataset need to be addressed by either imputing them with appropriate values (e.g., mean, median, mode) or removing the rows or columns containing missing values, depending on the context.
- **Dealing with Duplicates:** Duplicate data entries need to be identified and either removed or consolidated to ensure data quality. Duplicate records can distort analysis results and lead to incorrect conclusions.
- **Standardizing Data Formats:** Data from different sources may have inconsistent formats or representations. Standardizing data formats ensures uniformity and consistency across the dataset, making it easier to analyze and interpret.
- **Correcting Errors:** Data cleaning involves identifying and correcting errors or inconsistencies in the dataset, such as typographical errors, incorrect data entries, or outliers.

**3. Data Transformation:**

- **Feature Engineering:** Feature engineering involves creating new features or variables from existing ones to improve model performance or capture relevant information. This may include transformations such as scaling, normalization, or encoding categorical variables.
- **Aggregation:** Aggregating data involves summarizing multiple data points into a single value, such as calculating totals, averages, or counts for specific groups or categories within the dataset.
- **Pivoting:** Pivoting transforms data from a long format to a wide format (or vice versa) by reorganizing rows and columns. It involves reshaping the dataset to facilitate analysis or visualization.
- **Data Merging:** Data from multiple sources may need to be combined or merged to perform comprehensive analysis. This involves joining datasets based on common keys or identifiers to create a unified dataset.

**4. Data Quality Assurance:**

- **Validation:** Data validation involves ensuring that the imported data meets predefined quality standards and criteria. It includes checks for data completeness, consistency, accuracy, and integrity.
- **Data Profiling:** Data profiling involves analyzing the structure, content, and quality of the dataset to identify patterns, anomalies, and outliers. It helps in understanding the characteristics of the data and assessing its suitability for analysis.
- **Data Cleansing:** Data cleansing refers to the process of detecting and correcting errors, inconsistencies, or discrepancies in the dataset to improve its quality and reliability. It involves various techniques such as deduplication, outlier detection, and error correction.

**5. Documentation and Metadata Management:**

- **Documenting Data Sources:** Documenting the sources of data, including file names, URLs, database tables, and extraction methods, is essential for traceability and reproducibility of analysis results.
- **Metadata Management:** Managing metadata, such as data definitions, data types, and data lineage, helps in understanding the context and semantics of the dataset. Metadata provides valuable information about the structure, meaning, and usage of the data.

### B. Extraction of Values from a String Using Text Functions

**1. LEFT Function:**

- **Definition:** The LEFT function extracts a specified number of characters from the left side of a string.
- **Syntax:** LEFT(text, num_chars)
  - `text`: The string from which characters are to be extracted.
  - `num_chars`: The number of characters to extract from the left side of the string.
- **Example:**
  - `=LEFT("Hello World", 5)` returns "Hello".
- **Use Case:** Extracting prefixes or initials from strings, such as extracting the first name from a full name.

**2. RIGHT Function:**

- **Definition:** The RIGHT function extracts a specified number of characters from the right side of a string.
- **Syntax:** RIGHT(text, num_chars)
  - `text`: The string from which characters are to be extracted.
  - `num_chars`: The number of characters to extract from the right side of the string.
- **Example:**
  - `=RIGHT("Hello World", 5)` returns "World".
- **Use Case:** Extracting suffixes or file extensions from strings, such as extracting the file type from a file name.

**3. LEN Function:**

- **Definition:** The LEN function returns the number of characters in a string.
- **Syntax:** LEN(text)
  - `text`: The string whose length is to be calculated.
- **Example:**
  - `=LEN("Hello World")` returns 11.
- **Use Case:** Determining the length of strings for validation or truncation purposes.

**4. MID Function:**

- **Definition:** The MID function extracts a substring from a string, starting from a specified position and extending for a specified number of characters.
- **Syntax:** MID(text, start_num, num_chars)
  - `text`: The string from which characters are to be extracted.
  - `start_num`: The position in the string from which extraction starts (counting from 1).
  - `num_chars`: The number of characters to extract.
- **Example:**
  - `=MID("Hello World", 7, 5)` returns "World".
- **Use Case:** Extracting substrings from strings based on specific positions, such as extracting the last name from a full name.

**5. FIND Function:**

- **Definition:** The FIND function returns the starting position of one text string within another text string. It is case-sensitive.
- **Syntax:** FIND(find_text, within_text, [start_num])
  - `find_text`: The text to find within `within_text`.
  - `within_text`: The text string in which `find_text` will be searched.
  - `start_num` (optional): The position in `within_text` to start searching (default is 1).
- **Example:**
  - `=FIND("World", "Hello World")` returns 7.
- **Use Case:** Locating the position of specific substrings within strings, such as finding the position of a keyword in a sentence.

**6. REPLACE Function:**

- **Definition:** The REPLACE function replaces part of a text string with a different text string.
- **Syntax:** REPLACE(old_text, start_num, num_chars, new_text)
  - `old_text`: The original text string.
  - `start_num`: The position in `old_text` at which to start replacing characters.
  - `num_chars`: The number of characters to replace.
  - `new_text`: The text string to replace the specified characters with.
- **Example:**
  - `=REPLACE("Hello World", 7, 5, "Universe")` returns "Hello Universe".
- **Use Case:** Modifying specific parts of strings, such as replacing outdated information in text fields.
