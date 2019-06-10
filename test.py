import pandas as pd

from stravalib.client import Client

from config import Config

config = Config()

client = Client(config.access_token)

athlete = client.get_athlete()
print("For {id}, I now have an access token {token}".format(id=athlete.id, token=client.access_token))

# my_activities = client.get_activities(limit=100)
#
# data = []
# for activity in my_activities:
#     my_dict = activity.to_dict()
#     data.append(my_dict)
#
# df = pd.DataFrame(data)

clubs = client.get_athlete_clubs()
res_club = clubs[0]
res_club_activities = client.get_club_activities(res_club.id)

club_activities = []
for activity in res_club.activities:
    activity_dict = activity.to_dict()
    activity_dict['athlete_name'] = activity_dict['athlete']['firstname'] + ' ' + activity_dict['athlete']['lastname']
    club_activities.append(activity_dict)
club_df = pd.DataFrame(club_activities)
club_df.dropna(axis=1, inplace=True)
club_df.drop('athlete', axis=1, inplace=True)
club_df.to_csv('res_club_activities.csv')

