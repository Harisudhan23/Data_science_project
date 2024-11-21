import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt

# Assuming DataVisualizer class is already defined earlier in the same file

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
