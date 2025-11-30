# practice lab: Selecting data in Dataframe (HOL practice placed in script.py)
# practice with pandas library 

import pandas as pd

x = {'Name': ['Rose', 'Jane', 'John','Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Arquitect Group', 'Software Group', 'Design Team', 'Infrastructure'], 'Salary': [10000, 80000, 50000, 60000]}

df = pd.DataFrame(x)

print(df)
print(type(df))

print('----------------')
z = df[['Department', 'Salary', 'ID']] # retreiving the Dept, Salary, ID columns and assign it to the variable z
print(z)
print('----------------')

# --- Using loc() and iloc()
print(f"USING '.iloc[] and loc[]'")
print(df.iloc[0, 0]) # access the value of the first row and the first col
print(f"{df.iloc[0, 2]} <-- Value first row and the third columnd of 'df'")
print(f"{df.loc[1, 'Name']} <-- Value of the column using the name of the column")

print('----------------')
# --- using set_index()
# -- creating a new dataframe named 'df2' and assign 'df' to it. Let's use the 'Name' column as
# -- an index column using the method  set_index()

df2 = df

df2 = df2.set_index("Name")
print(f"USING set_index():")
print(f"displaying the first 5 rows of new database, new index is name")
print(df2.head())

print('----------------')
# -- slicing 

print(f"USING SLICING with '.iloc[] and loc[]'")
print(f" .iloc[] getting row from the 0, 1, and the column 0-1-2 here:")
print(df.iloc[0:2, 0:3])
print(f"---")
print(f".loc[] getting row fro 0-1-2  and from ID---to---Department column")
print(df.loc[0:2, 'ID' : 'Department'])

