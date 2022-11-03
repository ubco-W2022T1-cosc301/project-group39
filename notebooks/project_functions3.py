import pandas as pd

def load_and_process(csvPath):
    df_splitDate = (
         pd.read_csv(csvPath)
        .assign(Month=lambda x : x.incident_date.str.split().str[0]) #adds new column holding the month of the incident
        .assign(Year=lambda x : x.incident_date.str.split().str[2]) #adds new column holding the year of the incident
        .astype({'Year': 'int64'}) #sets data in year to a numerical value instead of a string
        .loc[lambda x: x['Year'] < 2021] #removes incidents past 2020 as data from that year is incomplete 
        #.loc[lambda x: x['injured'] < 100]
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
    row.sort()
    
    state_code = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", 
                   "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", 
                   "MN", "MS", "MO", "MT", "NE", "NV", "NJ", "NM", "NY", "NC", "OH", 
                   "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", 
                   "WA", "WV", "WI", "WY"]

    df_states = (
        pd.DataFrame(row)#creates new dataframe holding a row for each state
        .rename(columns = {0:'State'})
    ) #
    df_states['State_Code']=state_code
    #This dataframe is made to hold a row for every state in the US_Gun_Violence dataframe and its matching state code. This will be merged with the summed violence (sv) dataframe so that every state from the orignal dataframe is in the data even if there was no recorded violence in the 2019 year.
    
    df_sv = (
        pd.DataFrame(row)#creates new dataframe holding a row for each state
        .rename(columns = {0:'State'})
    )
    for x in row:
        df_sv.at[row.index(x), c1] = df[df[r] == x][c1].sum()
        df_sv.at[row.index(x), c2] = df[df[r] == x][c2].sum()
        
        #This is the dataframe that holds the summed values of Killed and Injured from 2019
    df_sv = pd.merge(df_states, df_sv, how='left')
    
    return df_sv

def violence_per_population(df_s, df_pop):
    df_vpp = (
        pd.merge(df_s, df_pop, how="outer",)
        #merges the dataframe of state violence to the dataframe holding the population from 2019.
        .dropna()
        .assign(Death_Percent=lambda x : x.Killed / x.Population_2019 * 100)
        .assign(Injured_Percent=lambda x : x.Injured / x.Population_2019 * 100)
        #This gives a percent of the number of people killed and injured per total people in that given state 
        [['State','State_Code','Population_2019','Killed','Death_Percent','Injured','Injured_Percent']]
    )
    return df_vpp
