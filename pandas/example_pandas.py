import pandas as pd

df = pd.read_csv('salaries.csv')

describe = df.describe()
print(describe)
#
print(df["Salary"])