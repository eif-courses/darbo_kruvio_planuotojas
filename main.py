import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql://root:@localhost/kruvio_skirstymas')


# Save the DataFrame to a new table in the SQL database


def studiju_plano_pravalymas(ekselio_dokumentas):
    dieninis = pd.read_excel(ekselio_dokumentas, sheet_name='Dieninis', header=8)
    dieninis_pravalytas = dieninis[dieninis['DalykoKatedra'].str.len() > 2]

    grupe = pd.read_excel(ekselio_dokumentas, sheet_name='Grupes', header=1)
    merged_data = pd.merge(dieninis_pravalytas, grupe, how='inner', on='Semestras')
    output_excel_path = 'kosmosas.xlsx'

    # Write the merged DataFrame to a new Excel file
    merged_data.to_excel(output_excel_path, index=False)  # Set index to False if you don't want to write row numbers

    merged_data.to_sql('my_table', con=engine, index=False, if_exists='replace')

    # english = pd.read_excel(ekselio_dokumentas, sheet_name='English',
    #                         header=8)
    # english_pravalytas = english[english['DalykoKatedra'].str.len() > 2]
    # print(english_pravalytas)
    # english_pravalytas.to_excel('english_output.xlsx',
    #                             index=False)  # Set index to False if you don't want to write row numbers
    #
    # sesijinis = pd.read_excel(ekselio_dokumentas, sheet_name='Sesijinis',
    #                           header=3)
    # sesijinis_pravalytas = sesijinis[sesijinis['DalykoKatedra'].str.len() > 2]
    # print(sesijinis_pravalytas)
    # sesijinis_pravalytas.to_excel('sesijines_output.xlsx',
    #                               index=False)  # Set index to False if you don't want to write row numbers
    #


studiju_plano_pravalymas('planas.xlsx')



selected_columns = ['Pavadinimas', 'Semestras']

# Read only the specified columns from the SQL database into a DataFrame
table_name = 'my_table'  # Replace with the name of your table
query = f"SELECT {', '.join(selected_columns)} FROM {table_name}"
df = pd.read_sql(query, con=engine)
# Display the DataFrame
print(df)