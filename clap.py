import sounddevice as sd
import numpy as np
import pyautogui

CLAP_THRESHOLD = 27 #the higher, the more not senstive
KEY_TO_PRESS = 'space' #space recomanded for rythem hell.

#IMPORTANT! Read readme on github for more information
#Code taken from gpt and simplifed :)

def detect_clap(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > CLAP_THRESHOLD:
        print("Clapped!")
        pyautogui.press(KEY_TO_PRESS)

def main():
    print("Clapping mode, ACTIVATED! Use CTRL+C to exit (you must be in the terminal)")
    with sd.InputStream(callback=detect_clap):
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("CTRL+C Detected. Closing program!")

if __name__ == "__main__":
    main()
