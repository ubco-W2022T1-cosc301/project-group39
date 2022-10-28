import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    df = (
        pd.DataFrame(data=pd.read_csv(url_or_path_to_csv_file))
        .drop(['incident_id', 'address', 'city_or_county'], axis=1)
        .assign(month=lambda x : x.incident_date.str.split().str[0])
        .assign(year=lambda x : x.incident_date.str.split().str[2])
        .drop(['incident_date'], axis=1)
        .astype({'year': 'int64'})
        .loc[lambda x : x['year'] <= 2020]
    )

    return df;