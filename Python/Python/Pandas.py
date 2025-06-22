import pandas as pd

df = pd.read_csv('output.csv')
# Display the DataFrame
df.loc[0, 'Name']
df[df['Age'] > 30]
print(df)

# Create data and save as csv file

# data = {
#     "Name": ['Alice', 'Bob', 'Charlie'],
#     "Age": [25, 30, 35],
#     "City": ['New York', 'Los Angeles', 'Chicago']
# }

# df = pd.DataFrame(data)
# print(df)
# # Display the DataFrame

# df.to_csv('output.csv', index=False)
# # Save the DataFrame to a CSV file