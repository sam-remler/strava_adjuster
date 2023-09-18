from stravaio import strava_oauth2
from stravaio import StravaIO

from config import CLIENT_ID, CLIENT_SECRET

token = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Get Strava Data
client = StravaIO(access_token=token["access_token"])
activities = client.get_logged_in_athlete_activities()

for activity in activities:
    print(activity)
    break

