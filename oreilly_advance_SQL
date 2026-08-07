import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/sample_data/us_retail_sales.csv')

df['sales_year'] = pd.to_datetime(df['sales_month']).dt.year
new_df =(
 df.query("kind_of_business in ['Book stores','Sporting goods stores']")
.groupby(['sales_year','kind_of_business'])['sales'].sum().reset_index()
.rename(columns = {'sales': 'sum_sales'}))
pivot_df = new_df.pivot(index = 'sales_year', columns = 'kind_of_business', values = 'sum_sales')

pivot_df.plot(kind='line')
show()
