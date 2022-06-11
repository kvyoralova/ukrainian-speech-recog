import sounddevice as sd
duration = 2.5  # seconds

if st.button("Say something"):
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
