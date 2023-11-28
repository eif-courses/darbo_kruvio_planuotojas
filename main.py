import pandas as pd

# Read the tables from Excel files, skipping the first 9 rows and using the 10th row as the header
main_table = pd.read_excel('main_table.xlsx', header=16)
teacher_info = pd.read_excel('lecturer_info.xlsx', header=1)  # Adjust header value as needed

# Print column names to check for typos or case sensitivity
# print("Main Table Columns:", main_table.columns)
# print("Teacher Info Columns:", teacher_info.columns)

# Merge data
merged_data = pd.merge(main_table, teacher_info, on='ReferenceColumn')

# Create Excel sheet with merged data
with pd.ExcelWriter('output_merged_data.xlsx', engine='xlsxwriter') as writer:
    # Write the merged data to a new sheet
    merged_data.to_excel(writer, sheet_name='Merged_Data', index=False)

