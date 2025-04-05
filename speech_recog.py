import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

# Initialize the recognizer and text-to-speech engine
listening = sr.Recognizer()
engine = pt.init()

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def hear():
    """Listens to the microphone and converts speech to text"""
    cmd = ""  # Initialize cmd variable to prevent UnboundLocalError
    try:
        with sr.Microphone() as mic:
            listening.adjust_for_ambient_noise(mic, duration=1)  # Adjust for background noise
            print('Listening...')
            voice = listening.listen(mic)  # Capture audio
            cmd = listening.recognize_google(voice)  # Convert to text
            cmd = cmd.lower()

            if 'peepee' in cmd:
                cmd = cmd.replace('peepee', '').strip()  # Remove 'kodi' and extra spaces
                print("Command recognized:", cmd)
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
    except Exception as e:
        print(f"Error: {e}")

    return cmd  # Always return cmd, even if empty

def run():
    """Runs the voice command system"""
    cmd = hear()
    
    if cmd:  # Ensure cmd is not empty
        print("You said:", cmd)

        if 'play' in cmd:
            song = cmd.replace('play', '').strip()
            speak('Playing ' + song)
            pk.playonyt(song)
    else:
        print("No valid command detected.")

# Run the voice assistant
if __name__ == "__main__":
    run()
