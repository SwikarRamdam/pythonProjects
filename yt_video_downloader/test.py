#doesn't work
# from pytube import YouTube

# vid_url = "https://youtu.be/OKuiyX5k6zg"

# yt1 = YouTube(vid_url)

# # print(yt.title)
# # print(yt.thumbnail_url)
# vids = yt1.streams.all() #provides all available format
# vids = yt1.streams.filter(only_audio=True) #filters audio from video

# streamlist = list(enumerate(vids))
# for i in streamlist:
#     print(i)
# print()
# stream = int(input("Enter : "))
# vids[stream].download()
# print("Successful")

# from pytube import Playlist

# pl = "https://www.youtube.com/c/BeatsQ/playlists?view=1&sort=dd&flow=grid"
# print(f'Downloading : {py.title}')

# for video in py.videos:
#     video.streams.first().download()
