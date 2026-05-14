import sys

from utils.data_utils import load_data, clean_data, save_results
from utils.stats_utils import (
    SalesDataError,
    revenue_by_product, 
    revenue_by_month, 
    revenue_by_region
)
from plotter import plot_bar_chart, plot_line_chart


# def main():
#     df = load_data('sales/data/sales.csv')
#     df = clean_data(df)

#     print("=== Sales Summary ===")
#     print(f"Total Revenue: ${df['Revenue'].sum():,.0f}")
#     print(f"Total Units Sold: {df['Units'].sum():,}")
#     print()

#     by_product = revenue_by_product(df)
#     print("Revenue by Product:")
#     for product, revenue in by_product.items():
#         print(f"  {product}: ${revenue:,.0f}")
#     print()

#     by_region = revenue_by_region(df)
#     print("Revenue by Region:")
#     for region, revenue in by_region.items():
#         print(f"  {region}: ${revenue:,.0f}")
#     print()

#     plot_bar_chart(
#         by_product,
#         title="Revenue by Product (Q1 2024)",
#         xlabel="Product",
#         ylabel="Revenue ($)"
#     )

#     by_month = revenue_by_month(df)
#     save_results(df, by_product, by_region, by_month)

#     plot_line_chart(
#         by_month,
#         title="Monthly Revenue Trend (Q1 2024)",
#         xlabel="Month",
#         ylabel="Revenue ($)"
#     )

DATA_FILE = 'sales/data/sales.csv'

def main() -> None:
    # use 'try-except' blocks to handle 'FileNotFoundError' and general exception while leading a sales data file.
    try:
        df = load_data(DATA_FILE)
    except FileNotFoundError:
        print(f"Error: The file '{DATA_FILE}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while loading data: {e}")
        sys.exit(1)

    # use 'try-except' block to handle 'KeyError' and 'ValueError' during data cleaning.
    try:
        df = clean_data(df)
    except (KeyError, ValueError) as e:
        print(f"Error: data cleaning failed - {e}")
        sys.exit(1)

    print("Sales Summary")
    print(f"Total Revenue: ${df['Revenue'].sum():,.0f}")
    print(f"Total Units Sold: {df['Units'].sum():,}")
    print()

    # use 'try-except' block to handle 'SalesDataError' while computing and displaying sales statistics by product, region and month.
    try:
        by_product = revenue_by_product(df)
        print("Revenue by Product:")
        for product, revenue in by_product.items():
            print(f"  {product}: ${revenue:,.0f}")
        print()

        by_region = revenue_by_region(df)
        print("Revenue by Region:")
        for region, revenue in by_region.items():
            print(f"  {region}: ${revenue:,.0f}")
        print()

        by_month = revenue_by_month(df)
    except SalesDataError as e:
        print(f"Warning: could not compute all statistics - {e}")
        sys.exit(1)

    # use 'try-except' block to handle 'PermissionError' and 'OSError' when saving the results to a file.
    try:
        save_results(df, by_product, by_region, by_month)
    except PermissionError as e:
        print(
            f"Warning: Could not save results - permission denied: {e.filename}"
        )
    except OSError as e:
        print(f"Warning: Could not save results - {e.strerror}")

    # use 'try-except' block to handle exceptions that may occur during plotting, such as 'ImportError' if the plotting library is not available
    try:
        plot_bar_chart(
            by_product,
            title="Revenue by Product (Q1 2024)",
            xlabel="Product",
            ylabel="Revenue ($)"
        )

        plot_line_chart(
            by_month,
            title="Monthly Revenue Trend (Q1 2024)",
            xlabel="Month",
            ylabel="Revenue ($)"
        )
    except Exception as e:
        print(f"Warning: charts skipped -{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()