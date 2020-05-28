# !pip install gtts
from gtts import gTTS
import os

text = "This is probably a small text and it works ...................... Yay"
language = "en"

# internet required
speech = gTTS(text=text, lang = language, slow=False)
speech.save("test.mp3")
os.system("start test.mp3")
