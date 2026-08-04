from gtts import gTTS
from pathlib import Path
#Turn your text to speech MP3 file ready
#Language is English
#If you want to make your code to have an path use this line under
#voices_dir = Path("Voices")

while True:
    text = input("Write something in any language:")
    file = Path(f"{text.title().strip()}")
    if text.upper().strip() == "XXX":
        break
    else:
        voice = gTTS(text=text, lang = "en")
        file_path = voices_dir / f"{text.title().strip()}.mp3"
        voice.save(str(file_path))
        print("Process done succesfully")
