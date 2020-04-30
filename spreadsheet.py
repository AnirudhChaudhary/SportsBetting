import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe
import pandas as pd
import numpy as np
from sklearn import linear_model

# use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


teams = ["Bears", "Bengals", "Bills", "Broncos", "Browns", "Buccaneers", "Colts", "Cardinals", "Chargers", "Chiefs", "Cowboys", "Dolphins", "Eagles", "Falcons", "Giants", "Jaguars", "Jets", "Lions",
         "Packers", "Panthers"
         , "Patriots", "Redskins", "Raiders", "Rams", "Ravens", "Saints", "Seahawks", "Steelers", "Texans", "Titans", "Vikings", "49ers"]
user_team = []

def valid_team_input(teams,user_team):
    input_bool = False
    team_bool = False
    while not input_bool:
        user_input = input("What team does the player play for? Enter D when done: ")
        for team in teams:
            if user_input == team:
                print("Found team")
                team_bool = True
                user_team.append(team)
        if user_input == "D":
            input_bool = True
            print(user_team)
        if not(team_bool):
            print("It looks like you spelled the team incorrectly")

        #After validation of the team, then you can state the player and the predictions. Computer should be able to take the averages of the entire row / column 

def prediction_input():
    location = upper(input("Is the player at home or away"))
    if location == "HOME":
        location = 1
    else:
        location = 0

def spreadsheet_call(teams,user_team):
    for x in range(len(user_team)):
        index = teams.index(user_team[x])      
        sheet = client.open("Sports").get_worksheet(index)
        df = worksheet_to_df(sheet)
        prediction(df)

def prediction(sheet):
        reg = linear_model.LinearRegression()
        sheet["Opponent Strength"] = pd.to_numeric(sheet["Opponent Strength"], downcast="float")
        reg.fit(sheet[['Location', 'Opponent Strength', 'Receptions', 'Yards', 'TD']],sheet.PPR)
        x = reg.predict([[0,0.625, 6.73, 82.26666667, 0.333333]])
        print(x)
        
def worksheet_to_df(worksheet):
    df = get_as_dataframe(worksheet, parse_dates = True, header = 0)
    df.dropna(axis = 'columns', how ='all', inplace=True)
    df.dropna(axis='rows', how='all', inplace=True)
    return df
                
def main():
    valid_team_input(teams,user_team)
    
    spreadsheet_call(teams,user_team)
    
    

    
#----------------------------------------------------------------
main()

        






