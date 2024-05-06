# Exploratory Data Analysis (EDA) pipeline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load .csv file
df = pd.read_csv('file-path/file-name.csv')

# Data insights
print(df)

# Check the number of observations (rows) and features (columns) in the dataset
print(df.shape)

# To understand more about the data.
print(df.info())

# Print the columns names
print("These are the names of the columns:", df.columns)

# To detect outliers in the dataset
# Points beyond the “whiskers” of the box plot can be considered potential outliers.
sns.boxplot(x=df['column-name'], color="lightgreen")
plt.show()

#