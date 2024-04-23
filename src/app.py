from pytube import YouTube
from moviepy.editor import AudioFileClip
import requests
import eyed3
import os

def download_thumbnail(thumbnail_url, path):
    response = requests.get(thumbnail_url)
    with open(path, 'wb') as file:
        file.write(response.content)

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    download_path = video.download()
    thumbnail_url = yt.thumbnail_url
    thumbnail_path = download_path.replace('.mp4', '.jpg')
    download_thumbnail(thumbnail_url, thumbnail_path)
    return download_path, thumbnail_path

def convert_to_mp3(video_path, thumbnail_path):
    mp3_path = video_path.replace('.mp4', '.mp3')
    video_clip = AudioFileClip(video_path)
    video_clip.write_audiofile(mp3_path)
    video_clip.close()
    tag_mp3(mp3_path, thumbnail_path)
    return mp3_path

def tag_mp3(mp3_path, thumbnail_path):
    audiofile = eyed3.load(mp3_path)
    if audiofile.tag is None:
        audiofile.initTag()
    with open(thumbnail_path, 'rb') as img_file:
        audiofile.tag.images.set(3, img_file.read(), 'image/jpeg')
    audiofile.tag.save()
    os.remove(thumbnail_path)  # Opcional: eliminar la miniatura después de usarla

if __name__ == '__main__':
    import sys
    url = sys.argv[1]  # Toma la URL desde la línea de comando
    print("Descargando video y miniatura...")
    video_path, thumbnail_path = download_video(url)
    print("Convirtiendo a MP3 y añadiendo miniatura...")
    mp3_file = convert_to_mp3(video_path, thumbnail_path)
    print(f"Archivo MP3 guardado en: {mp3_file}")
