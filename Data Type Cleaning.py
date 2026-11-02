import pandas as pd

# Step 1: Create an employee dataset
data = {
    "Name": ["Kiran", "Ravi", "Priya", "Suresh", "Anu"],
    "Age": ["23", "25", "22", "24", "21"],
    "Salary": ["30000", "45000", "35000", "40000", "32000"],
    "Joining_Date": ["2024-01-10", "2023-05-15", "2024-03-20",
                     "2022-08-12", "2023-11-05"],
    "Experience": [1.5, 3.0, 2.0, 4.5, 1.0]
}

df = pd.DataFrame(data)

# Step 2: Display original dataset
print("Original Dataset:")
print(df)

# Step 3: Check original data types
print("\nOriginal Data Types:")
print(df.dtypes)

# Step 4: Convert Age and Salary into numeric types
df["Age"] = pd.to_numeric(df["Age"])
df["Salary"] = pd.to_numeric(df["Salary"])

# Step 5: Convert Joining_Date into datetime format
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

# Step 6: Check corrected data types
print("\nCorrected Data Types:")
print(df.dtypes)

# Step 7: Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Step 8: Save cleaned dataset
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nData type cleaning completed successfully!")
