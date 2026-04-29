import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

def record_voice(seconds):
    print("Speak now...")
    audio=sd.rec(int(seconds*16000),samplerate=16000,channels=1)
    sd.wait()
    print("Recording done!\n")
    return audio

def find_volume(audio):
    volume=np.mean(np.abs(audio))
    return volume

print("=======VOICE ANALYSIS LAB=======")

print("recording 1:Speak normally")
voice1=record_voice(3)
vol1=find_volume(voice1)

print("recording 2:Speak loudly")
voice2=record_voice(3)
vol2=find_volume(voice2)

print("=======RESULT=======")
print("Volume of Recording 1:",vol1)
print("Volume of Recording 2:",vol2)

if vol1>vol2:
    print("Recording 1 is louder")
else:
    print("Recording 2 is louder")

plt.plot(voice1,label="Normal voice")
plt.plot(voice2,label="Loud voice")
plt.title("Voice Comparison")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
