import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def revenue_profit(self, start_month, start_year, end_month, end_year, output_file="revenue_profit.png"):
        # Filter data based on the date range
        filtered_df = self.df[
            (self.df['Date'] >= pd.Timestamp(year=start_year, month=start_month, day=1)) &
            (self.df['Date'] <= pd.Timestamp(year=end_year, month=end_month, day=1))
        ]
        
        # Plot Revenue and Profit trends
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

class TestDataTasks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create sample test DataFrame
        cls.df = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=5, freq='ME'),
            'Customer_Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
            'Revenue': [1000, 1500, 2000, 2500, 3000],
            'Profit': [200, 300, 400, 500, 600],
            'Product_Category': ['A', 'B', 'A', 'C', 'C'],
            'Sub_Category': ['A1', 'B1', 'A2', 'C1', 'C2'],
        })

    # Helper method to check if a file exists and delete it after verification
    def assertFileSaved(self, file_path):
        self.assertTrue(os.path.exists(file_path), f"File '{file_path}' was not saved.")
        os.remove(file_path)

    # Test Case 1: Verify datatypes of the DataFrame columns
    def test_column_datatypes(self):
        expected_types = {
            'Date': 'datetime64[ns]',
            'Customer_Gender': 'object',
            'Revenue': 'int64',
            'Profit': 'int64',
            'Product_Category': 'object',
            'Sub_Category': 'object',
        }
        for column, expected_type in expected_types.items():
            self.assertEqual(self.df[column].dtypes.name, expected_type, f"Column '{column}' has incorrect datatype")

    # Test Case 2: Validate column names
    def test_column_names(self):
        expected_columns = ['Date', 'Customer_Gender', 'Revenue', 'Profit', 'Product_Category', 'Sub_Category']
        self.assertListEqual(list(self.df.columns), expected_columns, "Column names do not match expected")

    # Test Case 3: Verify total number of rows
    def test_total_rows(self):
        expected_row_count = 5
        self.assertEqual(len(self.df), expected_row_count, "Row count does not match expected value")

    # Test Case 4: Test 'h' (Revenue and Profit trends)
    def test_revenue_profit_trends(self):
        visualizer = DataVisualizer(self.df)
        start_month, start_year, end_month, end_year = 1, 2023, 12, 2023
        output_file = "test_revenue_profit_trends.png"

        visualizer.revenue_profit(start_month, start_year, end_month, end_year, output_file=output_file)
        
        # Verify that the file is saved
        self.assertFileSaved(output_file)

    # Test Case 5: Test 'b' (Gender distribution)
    def test_gender_distribution(self):
        visualizer = DataVisualizer(self.df)
        output_file = "test_gender_distribution.png"

        visualizer.gender_distribution(output_file=output_file)
        
        # Verify that the file is saved
        self.assertFileSaved(output_file)

if __name__ == "__main__":
    unittest.main()