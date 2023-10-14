try:
    from pytube import Playlist
    from os import mkdir
except:
    from pip._internal import main as pip
    pip(["install","pytube"])    
    from pytube import Playlist
def download_videos():
    url=input("enter the playlist url:")
    folder=input("where to save the files? press enter to skip")
    try:
        mkdir(folder)
    except:
        print("Saving videos now")  
    p=Playlist(url)
    print(p.title)
    for video in p.videos:
        video.streams.get_highest_resolution().download(folder)  
        print(f"downloading...{video.title}")    
download_videos()