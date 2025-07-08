import speech_recognition as sr

def bangla_voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🔊 কথা বলুন... (বাংলা ভাষায়)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🔍 চিনে নেওয়া হচ্ছে...")
        text = recognizer.recognize_google(audio, language="bn-BD")
        print("✅ লিখিত রূপ:")
        print(text)
    except sr.UnknownValueError:
        print("😔 বোঝা যায়নি, আবার চেষ্টা করুন।")
    except sr.RequestError:
        print("🚫 গুগল সার্ভিসে সমস্যা হয়েছে। ইন্টারনেট আছে তো?")

if __name__ == "__main__":
    bangla_voice_to_text()
