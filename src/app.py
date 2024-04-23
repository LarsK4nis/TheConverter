import yt_dlp

def download_video_and_convert(url):
    # Configuración para descargar solo el audio, convertirlo a MP3 y guardar la miniatura
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_args': {
            'key': 'FFmpegMetadata'
        },
        'writethumbnail': True,
        'outtmpl': {
            'default': '%(id)s.%(ext)s',  # Salva el archivo con el ID del video como nombre
            'thumbnail': '%(id)s.%(ext)s' # Salva la miniatura con el mismo ID
        },
        'embedthumbnail': True,  # Incrusta la miniatura en el archivo MP3
        'addmetadata': True,      # Añade metadatos al archivo MP3
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    print("Descargando video y convirtiendo a MP3...")
    download_video_and_convert(url)
