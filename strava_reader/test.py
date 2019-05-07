from config import Config
import pandas as pd
import polyline
from stravalib.client import Client

config = Config()

client = Client()
# authorize_url = client.authorization_url(client_id=1234, redirect_uri='http://localhost:8282/authorized')
# Have the user click the authorization URL, a 'code' param will be added to the redirect_uri
# .....

# Extract the code from your webapp response
# code = request.get('code')  # or whatever your framework does
# token_response = client.exchange_code_for_token(client_id=1234, client_secret='asdf1234', code=code)
# access_token = token_response['access_token']
# refresh_token = token_response['refresh_token']
# expires_at = token_response['expires_at']


# Now store that short-lived access token somewhere (a database?)
client.access_token = config.access_token
# You must also store the refresh token to be used later on to obtain another valid access token
# in case the current is already expired
client.refresh_token = config.refresh_token

# An access_token is only valid for 6 hours, store expires_at somewhere and
# check it before making an API call.
# client.token_expires_at =

athlete = client.get_athlete()
print("For {id}, I now have an access token {token}".format(id=athlete.id, token=client.access_token))

my_activities = client.get_activities(limit=100)

for my_activity in my_activities:
    test = my_activity.map.summary_polyline


clubs = client.get_athlete_clubs()

res_club = clubs[0]

club_activities_list = []

for activity in res_club.activities:
    club_activities_list.append({'fist_name':activity.athlete.firstname,
                                 'last_name':activity.athlete.lastname,
                                 'type':activity.type,
                                 'distance':activity.distance,
                                 'total_elevation_gain':activity.total_elevation_gain
                                 })
club_df = pd.DataFrame(club_activities_list)
club_df.to_csv('res_club_activities.csv')

