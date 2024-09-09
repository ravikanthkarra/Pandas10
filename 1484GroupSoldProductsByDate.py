import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = activities.groupby(['sell_date'])
    df1 = grouped.agg(
        num_sold = ('product','nunique'),
        products = ( 'product',lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    # print(df1)
    return df1