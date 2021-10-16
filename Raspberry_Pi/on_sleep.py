import os
import time

filePath = os.path.dirname(os.path.realpath(__file__))


def playFile(fileName: str, volume: float = 1) -> None:
    """
    :param fileName: name of audio file in ./media
    :param volume: volume of sound, with 1 being 100%
    :return: void
    """
    os.system(f"mpg123 -q --scale {32768 * volume} {filePath}/media/{fileName}.mp3")


def onSleep() -> None:
    for _ in range(10):
        playFile("alarm", 10)
        playFile("wake_up", 10)

        time.sleep(0.5)


if __name__ == "__main__":
    onSleep()
