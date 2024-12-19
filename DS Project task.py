import pandas as pd
import matplotlib.pyplot as plt

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


# Data Analyzer Class
class DataAnalyzer:
    """Performs data analysis tasks such as summarization and unique counts."""

    def __init__(self, dataframe):
        self.df = dataframe

    def summary_statistics(self, output_file="Summary_statistics.csv"):
        """Generates summary statistics and saves to a CSV file."""
        summary_stats = self.df.describe()
        summary_stats.to_csv(output_file)
        print(f"Summary statistics saved to '{output_file}'.") #check the file in the Document folder

    def unique_counts(self):
        """Calculates unique counts for specific columns."""
        print("Unique Counts:")
        for col in ['Product_Category', 'Sub_Category', 'Product']:
            if col in self.df.columns:
                print(f"{col}: {self.df[col].nunique()}")


# Data Visualizer Class
class DataVisualizer:

    def __init__(self, dataframe):
        self.df = dataframe

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
        print(f"Histogram saved as '{output_file}'.")  #check in the Document folder
        plt.show()
class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def revenue_profit(self, start_month, start_year, end_month, end_year, output_file="revenue_profit.png"):

        filtered_df = self.df[
            (self.df['Date'] >= pd.Timestamp(year=start_year, month=start_month, day=1)) &
            (self.df['Date'] <= pd.Timestamp(year=end_year, month=end_month, day=1))
        ]
        
        plt.figure(figsize=(10, 6))
        plt.plot(filtered_df['Date'], filtered_df['Revenue'], label='Revenue', marker='o')
        plt.plot(filtered_df['Date'], filtered_df['Profit'], label='Profit', marker='o')
        plt.title('Revenue and Profit Trends')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.legend()
        plt.grid()
        plt.savefig(output_file)
        plt.close()

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
        print(f"Gender distribution chart saved as '{output_file}'.")  #check in the Document folder 
        plt.show()

    def revenue_profit_trends(self, start_month, start_year, end_month, end_year, output_file="revenue_profit.png"):
        
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
        print(f"Revenue and profit trends chart saved as '{output_file}'.")  #check in the Document folder
        plt.show()


# Main Execution
if __name__ == "__main__":
    # Load data
    file_path = input("C:/EntansTask/sales_data.xlsx")
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
