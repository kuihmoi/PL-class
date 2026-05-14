from utils.data_utils import load_data, clean_data, save_results
from utils.stats_utils import revenue_by_product, revenue_by_month, revenue_by_region
from plotter import plot_bar_chart, plot_line_chart


def main():
    df = load_data('data/sales.csv')
    df = clean_data(df)

    print("=== Sales Summary ===")
    print(f"Total Revenue: ${df['Revenue'].sum():,.0f}")
    print(f"Total Units Sold: {df['Units'].sum():,}")
    print()

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

    plot_bar_chart(
        by_product,
        title="Revenue by Product (Q1 2024)",
        xlabel="Product",
        ylabel="Revenue ($)"
    )

    by_month = revenue_by_month(df)
    save_results(df, by_product, by_region, by_month)

    plot_line_chart(
        by_month,
        title="Monthly Revenue Trend (Q1 2024)",
        xlabel="Month",
        ylabel="Revenue ($)"
    )

if __name__ == "__main__":
    main()