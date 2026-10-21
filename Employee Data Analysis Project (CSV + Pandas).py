# Employee Data Analysis Project
import pandas as pd

# Load dataset (replace with actual file path)
df = pd.read_csv("employee.csv")

# 1. Average salary
print("Average Salary:", df["Salary"].mean())

# 2. Department count
print("Department Count:\n", df["Department"].value_counts())

# 3. Filter employees above salary threshold
threshold = 50000
high_salary = df[df["Salary"] > threshold]
print("Employees with salary above", threshold, ":\n", high_salary)

# 4. Export results to new CSV
high_salary.to_csv("high_salary_employees.csv", index=False)
print("Filtered data saved to high_salary_employees.csv")
