import pandas as pd

def load_and_process(csvPath):
    df_splitDate = (
         pd.read_csv(csvPath)
        .assign(Month=lambda x : x.incident_date.str.split().str[0]) #adds new column holding the month of the incident
        .assign(Year=lambda x : x.incident_date.str.split().str[2]) #adds new column holding the year of the incident
        .astype({'Year': 'int64'}) #sets data in year to a numerical value instead of a string
        .loc[lambda x: x['Year'] < 2021] #removes incidents past 2020 as data from that year is incomplete 
    )  
    
    df_organized = (
        df_splitDate
        .drop(['incident_id','incident_date','address',"city_or_county"], axis=1) #removes un-used columns
        .dropna(axis = 0)
        .rename(columns={"state":"State","killed":"Killed","injured":"Injured"}) #capitalizes column names
        [['Year','Month','State','Killed','Injured']] #re-arranges columns   
    )
    return df_organized


def sum_column(df, r, c1, c2):
    row = df[r].tolist()
    row = set(row)
    row = list(row) #row = list of all states
    
    state_code = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", 
                   "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", 
                   "MN", "MS", "MO", "MT", "NE", "NV", "NJ", "NM", "NY", "NC", "OH", 
                   "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", 
                   "WA", "WV", "WI", "WY"]

    df_sv = pd.DataFrame(row, columns=[r])#creates new dataframe holding a row for each month

    for x in row:
        df_sv.at[row.index(x), c1] = df[df[r] == x][c1].sum()
        df_sv.at[row.index(x), c2] = df[df[r] == x][c2].sum()
        
    df_sum = (
        df_sv
        .sort_values(r,ascending=True,inplace=True)
    )
    df_sv['State_Code'] = state_code
    return df_sv
