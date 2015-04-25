import os
from google_search import GoogleCustomSearch

#set variables
os.environ["SEARCH_ENGINE_ID"] = "000839040200690289140:u2lurwk5tko"
os.environ["GOOGLE_CLOUD_API_KEY"] = "AIzaSyDaVumrGegjjGBRperM8oH49dHvlGbThtA"

SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']                           
API_KEY = os.environ['GOOGLE_CLOUD_API_KEY']

api = GoogleCustomSearch(SEARCH_ENGINE_ID, API_KEY)

print("we got here\n")

#for result in api.search('prayer', 'https://cse.google.com/cse/publicurl?cx=000839040200690289140:u2lurwk5tko'):
for result in api.search('pdf', 'http://scraperwiki.com'):
    print(result['title']) 
    print(result['link']) 
    print(result['snippet']) 