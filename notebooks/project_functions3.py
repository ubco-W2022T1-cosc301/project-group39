import pandas as pd

def load_and_process(csvPath):
    df = (
         pd.read_csv(csvPath)
        .drop(['incident_id','address'], axis=1)
        .dropna(axis = 0)
        .rename(columns={"city_or_county":"City/County","state":"State","killed":"Killed","injured":"Injured"})     
    ) 
    df1 = (
        df
        .assign(Total= df.Killed+ df.Injured)
        [(df.Killed < 15) & (df.Injured < 20)]
        .assign(Month=lambda x : x.incident_date.str.split().str[0])
        .assign(Year=lambda x : x.incident_date.str.split().str[2])
        
    )  
    df2 = (
        df1
        .drop(['incident_date'], axis=1)
        .astype({'Year': 'int64'})
        .loc[lambda x: x['Year'] < 2021]
        [['Year','Month','State','City/County','Killed','Injured','Total']]
    )
    return df2


def sum_column(df, r, c):

    row = df_cleaned[r].tolist()
    row = set(row)
    row = list(row)

    df_sv = pd.DataFrame(row, columns=[r])#creates new dataframe holding a row for each month

    for x in row:
        df_sv.at[row.index(x), c] = df[df[r] == x][c].sum()
    return df_sv


df_cleaned = load_and_process("../data/raw/US_Gun_Violence_Data.csv")
print(df_cleaned)
