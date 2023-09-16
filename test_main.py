import unittest
import polars as pl
from main import load_data, display_dataset_head, display_basic_statistics, generate_summary_statistics

# Mock data
mock_data = pl.DataFrame({
    "Age": [25, 30, 35, 40, 45],
    "Salary": [50000, 55000, 60000, 65000, 70000],
    "Score": [85, 89, 78, 90, 82]
})


class TestMainFunctions(unittest.TestCase):

    def test_load_data(self):
        # This test assumes that 'data.csv' exists in the same directory as the test file.
        data = load_data('data.csv')
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 5)

    def test_display_dataset_head(self):
        # For functions that print output and do not return anything,
        # we capture the printed output and check if it's correct
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        display_dataset_head(mock_data)
        sys.stdout = sys.__stdout__
        self.assertIn("Dataset Head:", output.getvalue())

    def test_display_basic_statistics(self):
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        display_basic_statistics(mock_data)
        sys.stdout = sys.__stdout__
        self.assertIn("Basic Descriptive Statistics:", output.getvalue())

    def test_generate_summary_statistics(self):
        from io import StringIO
        import sys
        output = StringIO()
        sys.stdout = output
        generate_summary_statistics(mock_data)
        sys.stdout = sys.__stdout__
        self.assertIn("Median:", output.getvalue())

    # NOTE: Testing visualization functions can be complex and is often done differently.
    # For now, we're skipping the test for `visualize_data` unless there's a specific logic or output to validate.


if __name__ == '__main__':
    unittest.main()
