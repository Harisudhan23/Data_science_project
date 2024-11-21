import pandas as pd
import matplotlib.pyplot as plt

# Data Preprocessor Class
class DataPreprocessor:
    """Handles data cleaning and preprocessing tasks."""

    def __init__(self, dataframe):
        self.df = dataframe

    def check_null_values(self):
        """Checks for null values in the DataFrame."""
        print("Null Values:\n", self.df.isnull().sum())

    def check_duplicates(self):
        """Checks for duplicate columns."""
        print("Duplicate Columns:", self.df.columns.duplicated())

    def check_datatypes(self):
        """Prints the data types of each column."""
        print("Column Data Types:")
        for col in self.df.columns:
            print(f"{col}: {self.df.dtypes[col]}")


# Data Analyzer Class
class DataAnalyzer:
    """Performs data analysis tasks such as summarization and unique counts."""

    def __init__(self, dataframe):
        self.df = dataframe

    def summary_statistics(self, output_file="Summary_statistics.csv"):
        """Generates summary statistics and saves to a CSV file."""
        summary_stats = self.df.describe()
        summary_stats.to_csv(output_file)
        print(f"Summary statistics saved to '{output_file}'.")

    def unique_counts(self):
        """Calculates unique counts for specific columns."""
        print("Unique Counts:")
        for col in ['Product_Category', 'Sub_Category', 'Product']:
            if col in self.df.columns:
                print(f"{col}: {self.df[col].nunique()}")


# Data Visualizer Class
class DataVisualizer:
    """Handles data visualization tasks such as plotting histograms and charts."""

    def __init__(self, dataframe):
        self.df = dataframe

    def plot_histogram(self, column, bins=50, output_file="histogram.png"):
        """Plots a histogram for the given column."""
        if column not in self.df.columns:
            print(f"Column '{column}' not found.")
            return
        plt.figure(figsize=(8, 6))
        plt.hist(self.df[column], bins=bins, color='skyblue', edgecolor='black')
        plt.title(f'{column} Distribution')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.savefig(output_file)
        print(f"Histogram saved as '{output_file}'.")
        plt.show()

    def gender_distribution(self, output_file="gender_distribution.png"):
        """Plots the gender distribution as a pie chart."""
        if "Customer_Gender" not in self.df.columns:
            print("Column 'Customer_Gender' not found.")
            return
        gender_counts = self.df['Customer_Gender'].value_counts()
        plt.figure(figsize=(8, 6))
        gender_counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'yellow'], startangle=90)
        plt.title('Gender Distribution')
        plt.ylabel("")
        plt.savefig(output_file)
        print(f"Gender distribution chart saved as '{output_file}'.")
        plt.show()

    def revenue_profit_trends(self, start_month, start_year, end_month, end_year, output_file="revenue_profit.png"):
        """Plots revenue and profit trends over time."""
        if 'Date' not in self.df.columns or 'Revenue' not in self.df.columns or 'Profit' not in self.df.columns:
            print("Required columns ('Date', 'Revenue', 'Profit') not found.")
            return

        self.df['YearMonth'] = pd.to_datetime(self.df['Date']).dt.to_period('M')
        start_date = f"{start_year}-{start_month:02d}"
        end_date = f"{end_year}-{end_month:02d}"

        filtered_df = self.df[(self.df['YearMonth'] >= start_date) & (self.df['YearMonth'] <= end_date)]
        if filtered_df.empty:
            print(f"No data found for the range {start_date} to {end_date}.")
            return

        trends = filtered_df.groupby('YearMonth')[['Revenue', 'Profit']].sum()
        plt.figure(figsize=(10, 6))
        trends.plot(marker='o')
        plt.title(f"Revenue and Profit Trends ({start_date} to {end_date})")
        plt.xlabel("Month")
        plt.ylabel("Amount")
        plt.grid(True)
        plt.savefig(output_file)
        print(f"Revenue and profit trends chart saved as '{output_file}'.")
        plt.show()


# Main Execution
if __name__ == "__main__":
    # Load data
    file_path = input("Enter the path to the sales data file: ")
    df = pd.read_excel(file_path)

    # Instantiate and use the classes
    preprocessor = DataPreprocessor(df)
    preprocessor.check_null_values()
    preprocessor.check_duplicates()
    preprocessor.check_datatypes()

    analyzer = DataAnalyzer(df)
    analyzer.summary_statistics()
    analyzer.unique_counts()

    visualizer = DataVisualizer(df)
    visualizer.plot_histogram(column="Customer_Age", output_file="customer_age_histogram.png")
    visualizer.gender_distribution()

    start_month = int(input("Enter start month (1-12): "))
    start_year = int(input("Enter start year: "))
    end_month = int(input("Enter end month (1-12): "))
    end_year = int(input("Enter end year: "))
    visualizer.revenue_profit_trends(start_month, start_year, end_month, end_year)
