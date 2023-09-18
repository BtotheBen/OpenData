from pytube import YouTube

link = str(input("Link to the Youtube Video: "))
yt = YouTube(link)

print(yt.title)
print(str(yt.views) + " views")
print(str(yt.length/60) + " min")

try:
    if input('Download Video in 720p (Y/N): ').lower() == 'y':
        yd = yt.streams.get_by_itag(22)
        yd.download('vids')
        exit()
    if input('Download Video in 360p (Y/N): ').lower() == 'y':
        yd = yt.streams.get_by_itag(18)
        yd.download('vids')
        exit()
    if input("Download Audio in (Y/N): ").lower() == "y":
        yd = yt.streams.filter(only_audio=True).first()
        yd.download("vids", filename=f"{yt.title}.mp3")
        exit()
except KeyError:
    if yt.age_restricted == True:
        print('This video is age restricted and cannot be downloaded!')