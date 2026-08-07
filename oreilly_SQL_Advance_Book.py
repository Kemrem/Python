# Extract, query, group by and pivot then draw chart using matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/sample_data/us_retail_sales.csv')

df['sales_year'] = pd.to_datetime(df['sales_month']).dt.year
new_df =(
 df.query("kind_of_business in ['Book stores','Sporting goods stores'] and (sales_year > 2010 or sales_year < 1995)")
.groupby(['sales_year','kind_of_business'])['sales'].sum().reset_index()
.rename(columns = {'sales': 'sum_sales'})
.query("sum_sales > 10000")
)

pivot_df = new_df.pivot(index = 'sales_year', columns = 'kind_of_business', values = 'sum_sales')
display(pivot_df)
pivot_df.plot(kind='bar')

# Extract, query, group by and then draw chart using seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/sample_data/us_retail_sales.csv')

df['sales_year'] = pd.to_datetime(df['sales_month']).dt.year
new_df =(
 df.query("kind_of_business in ['Book stores','Sporting goods stores'] and (sales_year > 2010 or sales_year < 1995)")
.groupby(['sales_year','kind_of_business'])['sales'].sum().reset_index()
.rename(columns = {'sales': 'sum_sales'})
.query("sum_sales > 10000")
)

sns.barplot(data = new_df, x = 'sales_year', y = 'sum_sales', hue = 'kind_of_business')
