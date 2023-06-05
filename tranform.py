from extract import extract_csv
import pandas as pd

pd.options.display.max_columns = None

def transform_data():
    """ This function transforms and cleans the Dataframe data """

    data_df = extract_csv()

    #Removing PACKAGE_ID column because all it's values are null
    data_df = data_df.drop('PACKAGE_ID', axis=1)

    #Removing duplicates in CDR_ID and ICCID
    data_df = data_df.drop_duplicates(subset=['CDR_ID','ICCID'])

    #Converting columns to datetime
    data_df['CONNECT_TIME'] = pd.to_datetime(data_df['CONNECT_TIME'])
    data_df['CLOSE_TIME'] = pd.to_datetime(data_df['CLOSE_TIME'])

    data_df['COMPANY_NAME'] = data_df['COMPANY_NAME'].replace('Ubicate GPS', 'CLIENTE E')

    #Lowercase all columns
    data_df.columns = map(str.lower, data_df.columns)
    data_df = data_df.rename(columns={'iccid':'icc_id'})

    return data_df
