import pandas as pd  # import pandas library

# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 22, 19, 21],
    'Marks': [85, 90, 75, 88]
}

# Create a DataFrame (like an Excel table)
df = pd.DataFrame(data)

# Show the whole table
print("Full DataFrame:")
print(df)

# Show only one column
print("\nStudent Names:")
print(df['Name'])

# Show basic statistics (mean, min, max, etc.)
print("\nStatistics:")
print(df.describe())

# Filter rows where marks > 80
print("\nStudents who scored above 80:")
print(df[df['Marks'] > 80])
 
# for making csv file
df.to_csv('friend.csv')
df.to_csv('friends_index_false.csv', index=False)

#
print("\n top two rows")
print(df.head(2))

print("\ntwo bottom rows")
print(df.tail(2))