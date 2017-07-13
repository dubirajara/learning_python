import sys
import spotipy
spotify = spotipy.Spotify()

#results = sp.search(q='weezer', limit=20)
#for i, t in enumerate(results['tracks']['items']):
#    print(i, t['name'])

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q=f'artist:{name}', type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])