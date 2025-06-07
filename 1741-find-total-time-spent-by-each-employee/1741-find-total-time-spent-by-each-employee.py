import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.rename(columns={'event_day':'day'})
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(by=['emp_id', 'day'], as_index=False).sum()
    
    return employees[['day', 'emp_id', 'total_time']]