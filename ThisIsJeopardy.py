import pandas as pd
pd.set_option('display.max_colwidth', -1)

# Load data and investigate its contents
df = pd.read_csv('jeopardy.csv')
print(df.columns)
print(df['Show Number'].head())
print(df[' Air Date'].head())
print(df[' Round'].head())
print(df[' Category'].head())
print(df[' Value'].head())
print(df[' Question'].head())
print(df[' Answer'].head())

# fixed column names with pre-space error
df.rename(columns = {
  ' Air Date': 'Air Date',
  ' Round':'Round',
  ' Category':'Category',
  ' Value': 'Value',
  ' Question':'Question',
  ' Answer': 'Answer'
},inplace=True)
# Testing column names

print(df['Show Number'].head())
print(df['Air Date'].head())
print(df['Round'].head())
print(df['Category'].head())
print(df['Value'].head())
print(df['Question'].head())
print(df['Answer'].head())

# Function to filter
def filter_data(data,words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data['Question'].apply(filter)].reset_index()

# Calling the filter function
filtered = filter_data(df,['King','England'])
print(filtered)
print(df.Value)
# New column to hold the mean of values
df['float_value']= df['Value'].apply(lambda x: float(x[1:].replace(',','')) if x != 'None' else 0)
# Finding the mean of values 
mean_of_values = df['float_value'].mean()
print(mean_of_values)
# Average value of questions that contain the word king
filtered = filter_data(df, ["King"])
print(filtered["float_value"].mean())

# Function to return unique answers of the questions in a dataset
def get_answer_counts(data):
    return data["Answer"].value_counts()
print(get_answer_counts(filtered))

    




