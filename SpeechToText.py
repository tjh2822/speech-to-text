"""
Thomas James Hall
github.com/tjh2822
Speech to Test with speech_recognition
"""

import speech_recognition as sr

"""Transcribe speech from recorded from `microphone`.

Returns a dictionary with three keys:
"success": a boolean indicating whether or not the API request was
            successful
"error":   `None` if no error occured, otherwise a string containing
            an error message if the API could not be reached or
            speech was unrecognizable
"transcription": `None` if speech could not be transcribed,
            otherwise a string containing the transcribed text
"""
def recognize_speech_from_mic(recognizer, microphone):

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    print("Speak now!")
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    print("Transcribing..")
    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def main():
    # Print the SR Version and program data
    print("Python Speech To Text via speech_recognition\n Speech Recognition Version:" + str(sr.__version__) )

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while(True):
        response = recognize_speech_from_mic(recognizer, microphone)
        print(type(response))
        print("You said... " + str(response))

if __name__ == '__main__':
    main()