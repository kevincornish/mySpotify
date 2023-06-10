# mySpotify

I created this script as there is (at the time of writing this) no way to view your entire history on spotify since account creation. My data is only 35,308 songs but, some inserts are failing so the importer isn't perfect at parsing the data (yet!).

## Features

- Import entire history from Spotify

## Todo

- Bulk insert the exported json history, current importer is slow
- Proactively sync between spotify history and database

### Request spotify data
- Request your **Full privacy data** [here](https://www.spotify.com/us/account/privacy/).
- Click **Extended streaming history**.
- Save all files listed as `endsong_X.json`.

## Create Spotify Developer Application

Create **Spotify Dev App** [here](https://developer.spotify.com/dashboard/applications).

1. **Create a client ID**.
2. Rename `/music/sample.env` to `.env`
3. Copy the **public** and the **secret** key into the .env file.
4. Click `EDIT SETTINGS`
5. Add `http://localhost:8000/redirect` to the `Redirect URIs`.
6. Click `Save`

### Installation

- Create Virtual Environment 
```
py -m venv env
```
- Activate Environment

Mac/Unix
```
source env/bin/activate
```
Windows
```
.\env\Scripts\activate
```

- Install requirements
```
pip install -r requirements.txt
```

- Make migrations and then run migrations
```
python manage.py makemigrations
python manage.py migrate
```

- Create a superuser
```
python manage.py createsuperuser
```

- Run server
```
python manage.py runserver
```

- To import data, save all files listed as `endsong_X.json` into the root directory of this project and run the import command
```
python manage.py import