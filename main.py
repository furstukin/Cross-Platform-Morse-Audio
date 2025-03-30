# MIT License
#
# Copyright (c) 2025 furstukin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from data import NATO_CODE, MORSE_CODE, BRAILLE
from crossmorsepy import MorseAudio

my_word = input("Enter a word: ")

nato = [NATO_CODE[letter] if letter.isalpha() else letter for letter in my_word.upper()]
morse = [MORSE_CODE[letter] for letter in my_word.upper()]
braille = [BRAILLE[letter] for letter in my_word.lower()]
nato_sentence = ' '.join(nato).strip()
morse_sentence = '.'.join(morse).strip()
braille_sentence = ''.join(braille).strip()
print(f"NATO Phonetic:\n{nato_sentence}\n")
print(f"Morse Code:\n{morse_sentence}\n")
print(f"Braille:\n{braille_sentence}")

morse_audio = MorseAudio()

morse_audio.play_audio(my_word)
