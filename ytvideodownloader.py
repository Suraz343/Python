from pytube import YouTube
link=input("enter the video url:-")
video=YouTube(link)
print(f"{video.title} is downloading")
print(video.title)
stream=video.streams.get_highest_resolution()
stream.download()
print(" Congratulations!! your video downloaded successfully")