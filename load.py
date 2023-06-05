from tranform import transform_data
from sqlalchemy import create_engine, text, exc

def load_data():

    data_df = transform_data()

    try:
        engine = create_engine('postgresql://postgres:password@localhost:5432/moabits')

        #Filtering and creating the dataframes
        dim_country_df = data_df[['country_iso3', 'country_name', 'mcc']].drop_duplicates()
        dim_sim_df = data_df[['inventory_id', 'company_name']].drop_duplicates()
        fct_cdr_df = data_df[['cdr_id','icc_id','inventory_id','type','connect_time','close_time','duration','direction','called_party','calling_party','country_iso3','mnc','imsi_id','imsi_no']]

        #Creating temporary tables to save the data
        dim_country_df.to_sql('temp_dim_country', engine, if_exists='append', index=False)
        dim_sim_df.to_sql('temp_dim_sim', engine, if_exists='append', index=False)
        fct_cdr_df.to_sql('temp_fct_cdr', engine, if_exists='append', index=False)

        with engine.begin() as conn:
            try:
                #This method was used to avoid conflicts on Unique Key Violation
                query = text(""" 
                    INSERT INTO dim_country (country_iso3, country_name, mcc)
                    SELECT *
                    FROM temp_dim_country
                    ON CONFLICT (country_iso3) DO NOTHING;

                    INSERT INTO dim_sim (inventory_id, company_name)
                    SELECT *
                    FROM temp_dim_sim
                    ON CONFLICT (inventory_id) DO NOTHING;

                    INSERT INTO fct_cdr (cdr_id,icc_id,inventory_id,type,connect_time,close_time,duration,direction,called_party,calling_party,country_iso3,mnc,imsi_id,imsi_no)
                    SELECT *
                    FROM temp_fct_cdr
                    ON CONFLICT (cdr_id) DO NOTHING;
                """)

                drop_temp_query = text(""" 
                    DROP TABLE IF EXISTS temp_dim_country;
                    DROP TABLE IF EXISTS temp_dim_sim;
                    DROP TABLE IF EXISTS temp_fct_cdr;
                """)

                conn.execute(query)
                conn.execute(drop_temp_query)
            except exc.SQLAlchemyError as e:
                print(f'Error executing the query: {e}')
                return 
    except Exception as e:
        print(f'Error loading the data: {e}')
