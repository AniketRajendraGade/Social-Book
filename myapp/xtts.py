import torch
from TTS.api import TTS

# # Get device
device = "cpu"

# # List available 🐸TTS models
# print(TTS().list_models())

# # Init TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# # Run TTS
# # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# # Text to speech list of amplitude values as output
# wav = tts.tts(text="माझ्या देशावर माझे प्रेम आहे. विविधतेने नटलेल्या परंपरांचा मला अभिमान आहे. आणि प्रत्येकाशी सौजन्याने वागेन. मी प्रतिज्ञा करीत आहे", speaker_wav="E:\zMarkytics\social_book\myapp\sample.m4a", language="hi")
# # Text to speech to a file
# tts.tts_to_file(text="माझ्या देशावर माझे प्रेम आहे. विविधतेने नटलेल्या परंपरांचा मला अभिमान आहे. आणि प्रत्येकाशी सौजन्याने वागेन. मी प्रतिज्ञा करीत आहे", speaker_wav="E:\zMarkytics\social_book\myapp\sample.m4a", language="hi", file_path="output.wav")



tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False).to(device)

# Run TTS
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path="E:\zMarkytics\social_book\myapp\sample.m4a")

# Example voice cloning with YourTTS in English, French and Portuguese
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
tts.tts_to_file("This is voice cloning.", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")