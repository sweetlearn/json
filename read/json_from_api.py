### https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python 
# Importing Data from a JSON Resource with Python

# import the library and the json module
import urllib.request as request
import json

# open the URL with the .urlopen()

with request.urlopen('http://data.nba.net/prod/v2/2018/teams.json') as response:
        source = response.read()
        data = json.loads(source)

# Option
with request.urlopen('http://data.nba.net/prod/v2/2018/teams.json') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')

# shows the keys in data (_internal and league, as expected)
type(data)
data.keys()
type(data['league'])
data['league'].keys()

type(data['league']['standard'])
len(data['league']['standard'])
data['league']['standard'][5]

nba_teams = [team for team in data['league']
             ['standard'] if team['isNBAFranchise']]

with open('nba_teams.json', 'w') as f:
        json.dump(nba_teams, f, indent=4, sort_keys=True)
