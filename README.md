# Strava-Adjuster

# How to use

### Setup 
1. Create an App though the [Strava API](https://www.strava.com/settings/api)
2. Insert `Client ID` and `Client Secret` into [`strava_api.py`](strava_api.py).
3. Insert token from Notion cookies into [`notion_api.py`](notion_api.py).
4. Create a page called `Strava` in Notion (top level).

### How to run
1. `git clone https://github.com/sam-remler/strava_adjuster.git`
2. `cd strava_adjuster`
3. `virtualenv venv`
4. `source venv/bin/activate` (Mac) or `venv/Scripts/activate` (Window)
5. `pip install -r requirements.txt`
6. `python strava_api.py` (Requires 3.5+ and 64-bit python install)
7. If you've set it up correctly a Strava App auth page will appear.
8. Click Authorize ![Strava Auth](/media/oauth.png)
9. You should see the data exported to a csv 