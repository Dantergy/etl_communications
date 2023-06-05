import pandas as pd
import zipfile

def extract_csv():
    """ This function extracts the CSV files and creates a pandas Dataframe """

    #Using zipfile to load CSV files in the .zip file
    with zipfile.ZipFile('cdr-files.zip', 'r') as file:
        #Check all the csv files
        filenames = [f for f in sorted(file.namelist()) if f.endswith('.csv')]
        dfs = []
        #Loop over all filenames
        for filename in filenames:
            with file.open(filename) as f:
                dfs.append(pd.read_csv(f))
        
        data_df = pd.concat(dfs, ignore_index=True)

        return data_df