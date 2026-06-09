# CSV Data Summarizer - Resources

---

## Sample Data

The `sample.csv` file contains example sales data with the following columns:

- **date**: Transaction date
- **product**: Product name (Widget A, B, or C)
- **quantity**: Number of items sold
- **revenue**: Total revenue from the transaction
- **customer_id**: Unique customer identifier
- **region**: Geographic region (North, South, East, West)

## Usage Examples

### Basic Summary

```
Analyze sample.csv
```

### With Custom CSV

```
Here's my sales_data.csv file. Can you summarize it?
```

### Focus on Specific Insights

```
What are the revenue trends in this dataset?
```

## Testing the Skill

You can test the skill locally before uploading to Claude:

```bash
# Install dependencies
pip install -r ../requirements.txt

# Run the analysis
python ../analyze.py sample.csv
```

## Expected Output

The analysis will provide:

1. **Dataset dimensions** - Row and column counts
2. **Column information** - Names and data types
3. **Summary statistics** - Mean, median, std dev, min/max for numeric columns
4. **Data quality** - Missing value detection and counts
5. **Visualizations** - Time-series plots when date columns are present

## Customization

To adapt this skill for your specific use case:

1. Modify `analyze.py` to include domain-specific calculations
2. Add custom visualization types in the plotting section
3. Include validation rules specific to your data
4. Add more sample datasets to test different scenarios
