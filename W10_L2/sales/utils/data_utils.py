# function for load_data
# function for clean_data

import os
import pandas as pd

def load_data(filepath:str) -> pd.DataFrame:
    return pd.read_csv(filepath,parse_dates=['Date'])

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df['Revenue'] = df['Units'] = df['Price']
    df['Month'] = df['Date'].dt.to_period('M')
    return df

# def save_results(df: pd.DataFrame, by_product: pd.Series,
#                  by_region: pd.Series, by_month: pd.Series,
#                  output_dir: str = 'output') -> None:
#     os.makedirs(output_dir, exist_ok=True)

#     #Summary
#     pd.DataFrame([{
#         'Metric': 'Total Revenue ($)',
#         'Value': round(df['Revenue'].sum(), 2),
#     }, {
#         'Metric': 'Total Units Sold',
#         'Value': int(df['Units'].sum(), 2),
#     }]).to_csv(os.path.join(output_dir, 'summary.csv'), index=False)

#     #Revenue by product
#     by_product.reset_index().rename(
#         columns={'Product': 'Product', 'Revenue': 'Revenue ($)'}
#     ).to_csv(os.path.join(output_dir, 'revenue_by_product.csv', index=False))

#     #Revenue by region
#     by_product.reset_index().rename(
#         columns={'Region': 'Region', 'Revenue': 'Revenue ($)'}
#     ).to_csv(os.path.join(output_dir, 'revenue_by_region.csv', index=False))

#     #Revenue by month
#     by_month_df = by_month.reset_index()
#     by_month_df['Month'] = by_month_df['Month'].astype(str)
#     by_month_df.rename(columns={'Revenue':'Revenue ($)'}, inplace=True)
#     by_month_df.to_csv(os.path.join(output_dir,'revenue_by_month.csv', index=False))

#     print(f'Results saved to '{output_dir}/'folder.')

def save_results(df: pd.DataFrame, by_product: pd.Series,
                 by_region: pd.Series, by_month: pd.Series,
                 output_dir: str = 'output') -> None:

    os.makedirs(output_dir, exist_ok=True)

    # Summary
    pd.DataFrame([{
        'Metric': 'Total Revenue ($)',
        'Value': round(df['Revenue'].sum(), 2),
    }, {
        'Metric': 'Total Units Sold',
        'Value': int(df['Units'].sum()),
    }]).to_csv(os.path.join(output_dir, 'summary.csv'), index=False)

    # Revenue by product
    by_product.reset_index().rename(
        columns={'Product': 'Product', 'Revenue': 'Revenue ($)'}
    ).to_csv(os.path.join(output_dir, 'revenue_by_product.csv'), index=False)

    # Revenue by region
    by_region.reset_index().rename(
        columns={'Region': 'Region', 'Revenue': 'Revenue ($)'}
    ).to_csv(os.path.join(output_dir, 'revenue_by_region.csv'), index=False)

    # Revenue by month
    by_month_df = by_month.reset_index()
    by_month_df['Month'] = by_month_df['Month'].astype(str)
    by_month_df.rename(columns={'Revenue': 'Revenue ($)'}, inplace=True)
    by_month_df.to_csv(os.path.join(output_dir, 'revenue_by_month.csv'), index=False)

    print(f"Results saved to '{output_dir}/' folder.")