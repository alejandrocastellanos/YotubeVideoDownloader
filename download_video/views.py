from django.http import JsonResponse
from pytube import YouTube
from django.shortcuts import render


def download_video(request):
    response = None
    if request.method == 'POST':
        link = request.POST['link'] or None
        if link:
            yt = YouTube(link)
            yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(
                '/Users/user/Downloads/')
            response = f'Downloaded video "{yt.title}" in download folder.'
    return render(request, 'download_video/index.html', {'response': response})


def info_video(request):
    image = None
    title = None
    if request.method == 'POST':
        link = request.POST['link'] or None
        if link:
            yt = YouTube(link)
            image = yt.thumbnail_url
            title = yt.title
    return JsonResponse({'image': image, 'title': title})
