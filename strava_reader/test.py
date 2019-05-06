from strava_reader.utils.directories import PROJECT_ROOT_DIR
from strava_reader.config import Config

from stravalib.client import Client

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
client.access_token = Config.
# You must also store the refresh token to be used later on to obtain another valid access token
# in case the current is already expired
client.refresh_token = refresh_token

# An access_token is only valid for 6 hours, store expires_at somewhere and
# check it before making an API call.
client.token_expires_at = expires_at

athlete = client.get_athlete()
print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))
