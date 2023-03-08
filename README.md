# spotify-ar
An A&amp;R tool that helps democratize in-house tools used by big music labels to detect up and coming talent within specific genres.

# What is this about
Big music labels utilize tools that use Spotify data to easily find up and coming talent. This application is an attempt at democratizing these tools for anyone who may have something to gain from finding up and coming artists within a specific genre. Findability through Spotify has been a huge issue largely due to the saturation of the platform in terms of the number of artists, as well as Spotify's habit of pushing larger artists. With over 11 million artists on the platform, organic findability becomes virtually impossible. This tool uses following parameters and genres to find artists within a specific niche and generates a playlist on your account containing randomized tracks from each of these artists.

# Features
* Generates a playlist based on your discovered artists
* Returns artists who exactly fit your niche

# Installation
* Clone the repository or download the ZIP file and extract it to a local directory.
* Install the required Python packages using pip install
* Make sure you can access your client ID and client secret through <a href="https://developer.spotify.com/documentation/general/guides/authorization/app-settings/">Spotify For Developers.</a>

# Usage
1. Make sure you have the necessary packages installed by running pip install spotipy.
2. Download and save the file in your working directory.
3. Set your Client ID and Client secret. 
4. Fill in the variables with your desired genre, minimum- and maximum number of followers. Note that 'limit' should be a value between 1-50 depending on how many artist you'd like to find, and the fact that Spotify API calls can only return 50 results at a time.
5. Note that the range will depend on how niche your genre is, but ranges of 500-1000 are generally what works best. e.g. 20.000 - 20.500.
6. You will now find your generated playlist in your Spotify account.

# Future
In the future I'd like to deploy this to a (simple)online platform for anyone to freely access instead of running it through Python.

# Documentation
For more info on Spotipy please refer to https://spotipy.readthedocs.io/en/2.22.1/
