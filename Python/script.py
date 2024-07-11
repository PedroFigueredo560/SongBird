import os
from flask import Flask, jsonify, request
from pytube import Playlist, YouTube
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://127.0.0.1:5500')

@app.route('/download_music', methods=['POST'])
def download_music():
    try:
        data = request.get_json()
        music_url = data.get('music')

        if not music_url:
            return jsonify({'error': 'Missing music URL'}), 400

        music = YouTube(music_url)
        
        try:
            audio_stream = music.streams.filter(only_audio=True).first()
            if audio_stream:
                download_path = os.path.join(os.path.expanduser("~"), "Downloads")  # Replace this with your desired download path
                filename = f"{music.title}.mp3"
                audio_stream.download(output_path=download_path, filename=filename, max_retries=3)
                print(f"{music.title} baixado com sucesso!")
        except Exception as e:
                print('Erro ao baixar {video.title}')
        
        return jsonify({'message': 'Música baixada com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/download_playlist_music', methods = ['POST'])
def download_playlist_music():
    try:
        data = request.get_json()
        playlist_url = data.get('playlist')

        if not playlist_url:
            return jsonify({'error': 'Missing playlist URL'}), 400

        playlist = Playlist(playlist_url)

        playlist_title = playlist.title
        download_path = os.path.join(os.path.expanduser("~"), "Downloads", playlist_title)
        os.makedirs(download_path, exist_ok=True)  # Create directory without error if exists

        for video in playlist.videos:
            try:
                audio_stream = video.streams.filter(only_audio=True).first()

                if audio_stream:
                    filename = f"{video.title}.mp3"
                    audio_stream.download(output_path=download_path, filename=filename, max_retries=3)
                    print(f"Download concluído: {filename}")
            except Exception as e:  # Catch any exception during download
                print(f"Erro ao baixar áudio de: {video.title} - {str(e)}")

        return jsonify({'message': 'Playlist baixada com sucesso!'}), 200
    except Exception as e:  # Catch any remaining exceptions
        return jsonify({'error': str(e)}), 400
    
@app.route('/download_video', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        video_url = data.get('video')

        if not video_url:
            return jsonify({'error': 'Missing video URL'}), 400

        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        
        if stream:
            download_path = os.path.join(os.path.expanduser("~"), "Downloads")  # Replace this with your desired download path
            filename = f"{video.title}.mp4"
            stream.download(output_path=download_path, filename=filename, max_retries=3)
            return jsonify({'message': '{video.title} baixado com sucesso!'}), 200
        else:
            return jsonify({'error': 'Erro ao baixar {video.title}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/download_playlist_video', methods = ['POST'])
def download_playlist_video():
    try:
        data = request.get_json()
        playlist_url = data.get('playlist')

        if not playlist_url:
            return jsonify({'error': 'Missing playlist URL'}), 400

        playlist = Playlist(playlist_url)

        playlist_title = playlist.title
        download_path = os.path.join(os.path.expanduser("~"), "Downloads", playlist_title)
        os.makedirs(download_path, exist_ok=True)  # Create directory without error if exists

        for video in playlist.videos:
            try:
                video_stream = video.streams.get_highest_resolution()

                if video_stream:
                    filename = f"{video.title}.mp3"
                    video_stream.download(output_path=download_path, filename=filename, max_retries=3)
                    print(f"Download concluído: {filename}")
            except Exception as e:  # Catch any exception during download
                print(f"Erro ao baixar áudio de: {video.title} - {str(e)}")

        return jsonify({'message': 'Playlist baixada com sucesso!'}), 200
    except Exception as e:  # Catch any remaining exceptions
        return jsonify({'error': str(e)}), 400
    
if __name__ == '__main__':
    app.run(debug=True)
