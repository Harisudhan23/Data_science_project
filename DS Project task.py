import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os

# Data Preprocessor Class
class DataPreprocessor:

    def __init__(self, dataframe):
        self.df = dataframe

    def check_null_values(self):
        print("Null Values:\n", self.df.isnull().sum())

    def check_duplicates(self):
        print("Duplicate Columns:", self.df.columns.duplicated())

    def check_datatypes(self):
        print("Column Data Types:")
        for col in self.df.columns:
            print(f"{col}: {self.df.dtypes[col]}")

    def save_as_pickle(self, output_file: str):
        """Save DataFrame as a pickle file."""
        if self.df is not None:
            self.df.to_pickle(output_file)
            print(f"Data saved as pickle at {output_file}")
        else:
            print("No data to save!")

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
    def __init__(self, df):
        self.df = df

    def revenue_profit_trends(self, start_month, start_year, end_month, end_year, output_file="revenue_profit.png"):
        if 'Date' not in self.df.columns or 'Revenue' not in self.df.columns or 'Profit' not in self.df.columns:
            print("Required columns ('Date', 'Revenue', 'Profit') not found.")
            return
        
        start_date = pd.Timestamp(start_year, start_month, 1)
        end_date = pd.Timestamp(end_year, end_month, 1)
        filtered_df = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]

        if filtered_df.empty:
            print(f"No data found for the range {start_date} to {end_date}.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.plot(filtered_df['Date'], filtered_df['Revenue'], label='Revenue', marker='o')
        plt.plot(filtered_df['Date'], filtered_df['Profit'], label='Profit', marker='o')
        plt.title('Revenue and Profit Trends')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.legend()
        plt.grid()
        plt.savefig(output_file)
        print(f"Chart saved as '{output_file}'.")
        plt.show()

    def gender_distribution(self, output_file="gender_distribution.png"):
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

    def plot_histogram(self, column, bins=50, output_file="histogram.png"):
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
    def profit_margin(self, output_file="profit_margin_scatter.png"):
        
        if 'Product' not in self.df.columns or 'Revenue' not in self.df.columns or 'Profit' not in self.df.columns:
            print("Columns 'Product', 'Revenue', or 'Profit' not found in the dataset.")
            return

        self.df['Profit_Margin'] = self.df['Profit'] / self.df['Revenue']

        product_profit_margin = self.df.groupby('Product')['Profit_Margin'].mean()

        plt.figure(figsize=(10, 6))
        plt.scatter(product_profit_margin.index, product_profit_margin.values, color='blue', alpha=0.7)
        plt.title("Average Profit Margin Per Product")
        plt.xlabel("Product")
        plt.ylabel("Average Profit Margin")
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.savefig(output_file)
        print(f"Profit margin scatter plot saved as '{output_file}'.")
        plt.show()
        
    def sub_category_performance(self, metric="Profit", output_file="sub_category_performance.png"):
        if 'Product_Category' not in self.df.columns or 'Sub_Category' not in self.df.columns or metric not in self.df.columns:
            print(f"Columns 'Product_Category', 'Sub_Category', or '{metric}' not found in the dataset.")
            return

        grouped_data = self.df.groupby(['Product_Category', 'Sub_Category'])[metric].sum().unstack()

        plt.figure(figsize=(12, 8))
        grouped_data.plot(kind='bar', stacked=True, colormap='tab20c', edgecolor='black')
        plt.title(f"{metric} by Sub-Category within Product Categories")
        plt.xlabel("Product Category")
        plt.ylabel(metric)
        plt.xticks(rotation=45)
        plt.legend(title="Sub_Category", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(output_file)
        print(f"Stacked bar chart saved as '{output_file}'.")
        plt.show()

        best_performance = self.df.groupby(['Product_Category', 'Sub_Category'])[metric].sum().groupby(level=0).idxmax()
        print(f"Best-performing Sub-Category by {metric} in each Product Category:")
        for category, sub_category in best_performance.items():
            total = self.df.groupby(['Product_Category', 'Sub_Category'])[metric].sum()[sub_category]
            print(f"  {category}: {sub_category[1]} with a total of {total}")

    def save_figure_as_pickle(self, fig, pickle_file):
        """Save a matplotlib figure as a pickle file."""
        with open(pickle_file, 'wb') as f:
            pickle.dump(fig, f)
        print(f"Figure saved as pickle: {pickle_file}")

    def load_figure_from_pickle(self, pickle_file):
        """Load a matplotlib figure from a pickle file."""
        with open(pickle_file, 'rb') as f:
            fig = pickle.load(f)
        fig.show()
        print(f"Figure loaded from pickle: {pickle_file}")

# Main Execution
if __name__ == "__main__":
    # Load data
    file_path = input("C:/EntansTask/sales.data.xlsx ").strip()
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        exit()

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
    visualizer.sub_category_performance(metric="Profit")
    visualizer.sub_category_performance(metric="Revenue", output_file="sub_category_revenue.png")

    # Save a figure as pickle
    fig = plt.figure()
    plt.hist(df["Customer_Age"], bins=30, color="skyblue", edgecolor="black")
    visualizer.save_figure_as_pickle(fig, "customer_age_histogram.pkl")

    # Load and display the saved pickle figure
    visualizer.load_figure_from_pickle("customer_age_histogram.pkl")
