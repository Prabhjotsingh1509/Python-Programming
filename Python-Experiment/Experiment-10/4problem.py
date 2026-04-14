# Write a Pandas program to get the powers of an array values element-wise.  
# Note: First array elements raised to powers from second array 
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]} 
# Expected Output: 
# X Y Z 
# 0 78 84 86 
# 1 85 94 97 
# 2 96 89 96 
# 3 80 83 72 
# 4 86 86 83 

import pandas as pd

data = {
    'X':[7,5,9,8,8],
    'Y':[8,9,8,8,8],
    'Z':[8,9,9,7,8]
}
df= pd.DataFrame(data)
print(df)

# result = df['X']**df['Y']
a= pd.Series([7,5,9,8,8])
b=pd.Series([8,9,8,8,8])

result= a**b
print(result)