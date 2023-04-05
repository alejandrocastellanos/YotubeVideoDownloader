from pytube import YouTube

link ='https://www.youtube.com/watch?v=V89J_Ntg6ss'
yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download('/Users/user/Downloads/')
