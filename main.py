import pandas as pd

def studiju_plano_pravalymas(ekselio_dokumentas):
    dieninis = pd.read_excel(ekselio_dokumentas, sheet_name='Dieninis', header=8)
    dieninis_pravalytas = dieninis[dieninis['DalykoKatedra'].str.len() > 2]

    grupe = pd.read_excel(ekselio_dokumentas, sheet_name='Grupes', header=1)
    merged_data = pd.merge(dieninis_pravalytas, grupe, how='inner', on='Semestras')
    output_excel_path = 'rezultatas.xlsx'

    # Write the merged DataFrame to a new Excel file
    merged_data.to_excel(output_excel_path, index=False)  # Set index to False if you don't want to write row numbers


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

