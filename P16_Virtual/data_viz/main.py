from utils.data_utils import load_csv_file, extract_column
from plotter import plot_histogram

def main():
    data = load_csv_file("data.csv")

    values = extract_column(data, 'value')

    plot_histogram(values, title='Distribution of Values', xlabel='value range',
                   ylabel='count', bins = 5, color = 'lightgreen')
    
if __name__ == "__main__":
    main()