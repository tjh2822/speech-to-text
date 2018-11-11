import speech_recognition as sr
import pyaudio

def main():
    # Print the SR Version and program data
    print("Python Speech To Text via speech_recognition\n Speech Recognition Version:" + str(sr.__version__) )

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=3)
    
    #source file = sr.AudioFile('harvard.wav')

    recording=""
    with mic as source:
        print("Recording... Speak Now")
        r.adjust_for_ambient_noise(source, duration=0.5)
        recording = r.record(source)
    
    results = r.recognize_google(recording)
    print("Results")

if __name__ == '__main__':
    main()