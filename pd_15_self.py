import pandas as pd
df1 = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,85,None,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
df2 = pd.DataFrame({'W':[78,75,86,80,None],'X':[78,85,96,80,76], 'Y':[84,84,89,83,86],'Z':[86,97,96,72,83]});
print("Original DataFrames:")
print(df1)
print(df2)
print("\nCheck for equality of the dataframes:")

print(df1.eq(df2))

# 1. Aufgabe: check for not equal (ne)