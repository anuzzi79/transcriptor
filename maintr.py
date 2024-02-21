from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    video_url = request.form['url']
    language = request.form['language']
    video_id = video_url.split('=')[-1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        transcript_text = ' '.join([line['text'] for line in transcript])
        return jsonify({'transcript': transcript_text})
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message})

if __name__ == '__main__':
    app.run(debug=True)
