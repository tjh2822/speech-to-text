import speech_recognition as sr
import pyaudio

def main():
    # Print the SR Version and program data
    print("Python Speech To Text via speech_recognition\n Speech Recognition Version:" + str(sr.__version__) )

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(r.recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    
    #source file = sr.AudioFile('harvard.wav')

    # Set Ambient Noise
    with mic as source:
        r.recognizer.adjust_for_ambient_noise(source)
        audio = r.recognizer.listen(source)
      
    # Try recording the audio sample
    recording=""
    with mic as source:
        print("Recording... Speak Now")
        r.adjust_for_ambient_noise(source, duration=0.5)
        recording = r.record(source duration=4)
    
    results = r.recognize_google(recording)
    print("Results" + str(results))

if __name__ == '__main__':
    main()