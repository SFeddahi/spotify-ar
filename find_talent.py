import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth



#client_credentials_manager = SpotifyClientCredentials(client_id="6003907958e9442895a65c76dc38e558", client_secret="25cf8b24506149b498d9a2b83baca1a3")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='6003907958e9442895a65c76dc38e558', client_secret='25cf8b24506149b498d9a2b83baca1a3', redirect_uri='http://localhost:8080/callback', scope='playlist-modify-public'))


#follower_min = int(input("Enter the minimum follower count: "))
#follower_max = int(input("Enter the maximum follower count: "))
#genre = input("Enter the genre: ")

follower_min = 20000
follower_max = 20500
genre = 'german'
selected_tracks = []
countartists=0
limit=2

results = sp.search(q = f'genre:"{genre}"', type="artist", limit=50)
artists = results['artists']

while artists['next']:
    results = sp.next(artists)
    artists = results['artists']
    
    for artist in artists['items']:
        followers = artist['followers']['total']
        genres = artist['genres']
        
        if follower_min <= followers <= follower_max:
            
            if countartists >= limit:
                break
                
            else:
                print(f"{artist['name']}: {followers} followers {genres} ")
                countartists+=1
                top_tracks = sp.artist_top_tracks(artist['id'])['tracks']
            
                if top_tracks:
                    selected_track = random.choice(top_tracks)['id']
                    selected_tracks.append(selected_track)
                    
playlist_name = f"My discovered {genre} artists"

playlist_description = f"A playlist of random tracks by {genre} artists."

playlist = sp.user_playlist_create(user='samirfeddahi', name=playlist_name, public=True, description=playlist_description)

playlist_id = playlist['id']

sp.user_playlist_add_tracks(user='samirfeddahi', playlist_id=playlist_id, tracks=selected_tracks)
