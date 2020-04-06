import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Sports").get_worksheet(0)
data = sheet.get_all_records()
#print(data)

wks = client.open("Sports").get_worksheet(1)
data2 = wks.get_all_records()
#print(data2)

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

def spreadsheet_call(teams,user_team):
    for x in range(len(user_team)):
        index = teams.index(user_team[x])      
        sheet = client.open("Sports").get_worksheet(index)
        data = sheet.row_values(2)
        print(data)
            
                
def main():
    valid_team_input(teams,user_team)
    
    spreadsheet_call(teams,user_team)
    

    
#----------------------------------------------------------------
main()

        






