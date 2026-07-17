import pandas as pd
def main():
    employee = {
        "Department": ["mca", "cse", "eee","ce","bca"],
        "Employee Name": ["riya","kenya","gaya","elisa","rony"],
        "Salary": [35000, 50000, 45000, 40000, 55000]
    }

    df = pd.DataFrame(employee)

    print("Employee Details:")
    print(df)

    avg_salary = df.groupby("Department")["Salary"].mean()

    print("\nAverage Salary of Employees in Each Department:")
    print(avg_salary)

if __name__ == "__main__":
    main()