import pyglet
import bluetooth

def play_mp3(file_path):
    """
    Play an mp3 file.
    :param file_path: Path to the mp3 file.
    """
    music = pyglet.media.load(file_path)
    music.play()
    pyglet.app.run()

def connect_bluetooth_speaker():
    """
    Connect to a Bluetooth speaker.
    """
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in nearby_devices:
        print(f"Found Bluetooth device {name} with address {addr}")
        # Add logic to connect to the Bluetooth speaker
