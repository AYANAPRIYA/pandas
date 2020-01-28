
import pandas as pd
df = pd.read_csv('Desktop/pandas/survey_results_public.csv')
df.shape
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
schema_df = pd.read_csv('Desktop/pandas/survey_results_schema.csv')
schema_df
df.head(10)
#df.columns
#df["Hobbyist"].value_counts()
#df.loc[0:5, 'Hobbyist':'Student']
#schema_df.sort_index(inplace= True)

#schema_df
highsalary = (df['ConvertedComp'] > 70000)
df.loc[highsalary, ["Country", 'LanguageWorkedWith']]
