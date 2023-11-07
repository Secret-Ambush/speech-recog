import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening now: ")
    audio = r.listen(source, timeout=2)
    print("Stopped Listening")
    text = r.recognize_google(audio, show_all=True)
    print(text)

alternative_list = text.get('alternative', [])

# Iterating to find text with numeric digits
selected_text = ""
for item in alternative_list:
    transcript = item.get('transcript', '')
    if any(char.isdigit() for char in transcript):
        selected_text = transcript
        break

# If no text with numeric digits found, select the first one
if selected_text == '' and alternative_list:
    selected_text = alternative_list[0].get('transcript', '')

print("Selected Text:", selected_text)