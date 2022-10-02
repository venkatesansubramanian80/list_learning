import pandas as pd

df_data = pd.DataFrame(data=[[1,'Mr. X', 'HR', 10000, 8000, 6000, 4000],
                             [2,'Mr. Y', 'Data Scientist', 100000, 80000, 60000, 40000],
                             [3,'Mr. Z', 'Architect', 12000, 100000, 80000, 60000]], columns=['id', 'employee_name','designation','salary','salary_2021', 'salary_2020', 'salary_2019'])
print(df_data)
df_salary = df_data[['employee_name','salary','salary_2021', 'salary_2020', 'salary_2019']]
df_salary.index = df_salary['employee_name']
df_salary = df_salary[['salary','salary_2021', 'salary_2020', 'salary_2019']]
print(df_salary.mean(axis=0))
print(df_salary.mean(axis=1))
print(df_data[df_data['salary'] >= 12000])