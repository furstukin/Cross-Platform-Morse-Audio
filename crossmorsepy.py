from playsound import playsound
import time
from data import BRAILLE, MORSE_AUDIO_DICT, MORSE_CODE, NATO_CODE

class MorseAudio:

    @classmethod
    def play_audio(cls, text_to_encode: str):
        for char in text_to_encode.lower():
            # Check if the character is in the dictionary
            if char in MORSE_AUDIO_DICT:
                m_char = MORSE_AUDIO_DICT[char]
                playsound(f'static/audio/morse_code/{m_char}.mp3')
                time.sleep(0.01)  # Sets delay between sounds
            else:
                # Skip the character if it is not in the dictionary
                continue