from flask import Flask, request, jsonify
import pyglet
from utils import play_mp3, connect_bluetooth_speaker

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook():
        play_mp3('sound.mp3')
        return jsonify({'status': 'mp3 played'}), 200

if __name__ == '__main__':
    connect_bluetooth_speaker()
    app.run(host='0.0.0.0', port=5000)
