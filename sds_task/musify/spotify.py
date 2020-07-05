import os
import requests
import datetime
from urllib.parse import urlencode
import base64

client_id = os.environ.get('SPOTIFY_CLIENT_ID')      # Spotify Client ID
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')  # Spotify Client Secret

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token' # The endpoint to get the access token by performing authentication.
    
    # Constructor method.
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        
    def get_client_credentials(self):
        client_id = self.client_id
        client_secret = self.client_secret
        if client_id == None or client_secret == None:
            raise Exception("You must set client_id and client_secret!")
        client_creds = f"{client_id}:{client_secret}"                   # Simple f-string of client id and client secret.
        client_creds_b64 = base64.b64encode(client_creds.encode())      # f-string converted to bytestring and then
                                                                        # converted to base 64 byte string.
        return client_creds_b64.decode()
        
    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()        # Gets base64 client credentials.
        return {
            "Authorization": f"Basic {client_creds_b64}"        # Token headers as dictionary.
        }
    
    def get_token_data(self):
        return {
            'grant_type': 'client_credentials'                  # Tokent data as dictionary.
        }
        
    def performAuth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client.")
            # return False
        data = r.json()
        # data = {
        # 'access_token': 'BQBeTRmb25nPdR7-zmGtXC0SzJccb4YIOVDi_esYCMGIFret_Vk6QhbKGDEtL7Zdvem1QMpy9oLQjjB9qE8',
        #  'token_type': 'Bearer', 'expires_in': 3600, 'scope': ''
        # }

        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now   # Checking if the token has expired or not.
        return True
    
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()   # Getting current time.
        if expires < now:               # Getting new access token if the previous one has expired
            self.performAuth()
            return self.get_access_token()
        elif token == None:             # Getting access token if for some reason the access token wasn't set previously.
            self.performAuth()
            return self.get_access_token()

        return token
    
    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"   # Getting headers which will be used as a parameter with every endpoint
                                                        # that I will be using.
        }
        return headers
    
    def search(self, query, search_type="artist"):      # Search method to perform search based on the search type and query.
        headers = self.get_resource_header()            # Search types allowed are artist, album, track, playlist.....
        endpoint = "https://api.spotify.com/v1/search"
        data = urlencode({"q": query, "type": search_type.lower()})
        lookup_url = f"{endpoint}?{data}"               # Joining the parameters in the correct way with the endpoint.
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):        # Any response's status code if not in between 200-299 then
            return {}                                   # then it is not a correct way to request.
                                                        # Something is wrong in the way we requested data using
                                                        # the endpoint.
        return r.json()

    def new_releases(self):                             # This method to get new released albums.
        headers = self.get_resource_header()
        endpoint = "https://api.spotify.com/v1/browse/new-releases"
        data = urlencode({"country": "IN"})             # Specfic to India.
        lookup_url = f"{endpoint}?{data}"               # Joining the parameters in the correct way with the endpoint.
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):        # Any response's status code if not in between 200-299 then
            return {}                                   # then it is not a correct way to request.
                                                        # Something is wrong in the way we requested data using
                                                        # the endpoint.
        return r.json()

    def get_category_playlists(self, category):         # Method to get playlists by category.
        headers = self.get_resource_header()            # Categories allowed are many. I have used party, pop, hiphop, bollywood.
        endpoint = f"https://api.spotify.com/v1/browse/categories/{category}/playlists"
        data = urlencode({"country": "IN"})
        lookup_url = f"{endpoint}?{data}"               # Joining the parameters in the correct way with the endpoint.
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):        # Any response's status code if not in between 200-299 then
            return {}                                   # then it is not a correct way to request.
                                                        # Something is wrong in the way we requested data using
                                                        # the endpoint.
        return r.json()

# Making an object of the SpotifyAPI class by passing on the client id and secret.      
client = SpotifyAPI(client_id, client_secret)