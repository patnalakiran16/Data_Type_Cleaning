Data Type Cleaning Using Python and Pandas

Project Overview

This project focuses on identifying incorrect data types in an employee dataset and converting them into appropriate data types using Python and Pandas.

Correct data types are important for performing accurate data analysis and mathematical operations.

Objective

- Identify incorrect data types in a dataset.
- Convert columns into appropriate data types.
- Understand the importance of data types in data analysis.
- Verify the data types after conversion.

Tools and Technologies

- Python
- Pandas
- Jupyter Notebook

Dataset Description

The project uses a sample Employee Dataset containing the following columns:

Column Name| Description
Name| Employee name
Age| Employee age
Salary| Employee salary
Joining_Date| Employee joining date
Experience| Years of experience

Implementation

Step 1: Create the Dataset

Create an employee dataset using a Python dictionary and convert it into a Pandas DataFrame.

Step 2: Check Original Data Types

Use "df.dtypes" to identify the existing data types of each column.

Step 3: Convert Data Types

- Use "pd.to_numeric()" to convert Age and Salary into numeric values.
- Use "pd.to_datetime()" to convert Joining_Date into datetime format.

Step 4: Verify Data Types

Check the corrected data types using "df.dtypes".

Step 5: Save the Cleaned Dataset

Use "df.to_csv()" to save the cleaned data into a CSV file.

Before Data Cleaning

Column| Original Data Type
Name| object
Age| object
Salary| object
Joining_Date| object
Experience| float64

After Data Cleaning

Column| Corrected Data Type
Name| object
Age| int64
Salary| int64
Joining_Date| datetime64
Experience| float64

Output

The employee dataset is successfully cleaned, and all columns have appropriate data types.

The cleaned dataset is saved as:

"cleaned_employee_data.csv"

Key Learnings

- Understanding different data types in Pandas.
- Identifying incorrect data types.
- Converting string values into numeric values.
- Working with datetime data.
- Saving cleaned datasets as CSV files.

Conclusion

Through this task, I learned how to identify and correct data types in a dataset using Python and Pandas. This process helps improve data quality and makes further data analysis easier and more accurate.

Author

Patnala Kiran

Python Internship – VEDA TECHNOLOGY