# python-player

## Project Description
This project is a Python-based server application that handles web hooks and plays mp3 sounds. It is designed to work with a Bluetooth speaker and can be run on a Raspberry Pi.

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/esunke/python-player.git
   cd python-player
   ```
2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Project
1. Start the Flask server:
   ```
   python app.py
   ```
2. The server will be running on `http://localhost:5000`. You can send web hooks to this URL to trigger the mp3 sound playback.
