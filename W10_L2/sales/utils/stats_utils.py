#functions to calculate revenue (price x unit)

import pandas as pd

def revenue_by_product(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

def revenue_by_month(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Product')['Revenue'].sum()

def revenue_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)