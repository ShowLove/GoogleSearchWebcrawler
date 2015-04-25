import GoogleCustomSearch

SEARCH_ENGINE_ID = os.environ['000839040200690289140:u2lurwk5tko']                           
API_KEY = os.environ['171757440843-eq8kf7mcuoflj5ocvt0jn0sddndvbrpq.apps.googleusercontent.com']

api = GoogleCustomSearch(SEARCH_ENGINE_ID, API_KEY)

for result in api.search('prayer', 'https://cse.google.com/cse/publicurl?cx=000839040200690289140:u2lurwk5tko'):
    print(result['title']) 
    print(result['link']) 
    print(result['snippet']) 