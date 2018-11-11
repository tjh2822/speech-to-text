import speech_recognition as sr

def main():
    # Print the SR Version and program data
    print("Python Speech To Text via speech_recognition\n Speech Recognition Version:" + str(sr.__version__) )

    r = sr.Recognizer()
    harvard = sr.AudioFile('harvard.wav')

    recording=""
    with harvard as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        recording= = r.record(source)

if __name__ == '__main__':
    main()