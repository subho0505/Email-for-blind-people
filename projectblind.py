import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_audio():
    try:
        with sr.Microphone() as source:
            print('say...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('projectblind132@gmail.com', 'Subho132' )
    email = EmailMessage()
    email['From'] = 'projectblind132@gmail.com'
    email ['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'good': 'subitabhdey132@gmail.com',
    'better': 'itwasntme890@gmail.com',
    'best': 'rathourabhay0305@gmail.com',
    'sunny': '21kabirkashyap@gmail.com',
    'rohan': 'kumarrohan674@gmail.com',
}


def get_email_info():
    print('to whome you want to send email')
    talk('to whome you want to send email')
    name = get_audio()
    receiver = email_list[name]
    print(receiver)
    print('what will be the subject of this mail?')
    talk('what will be the subject of this mail?')
    subject = get_audio()
    print('please speak the body of the mail')
    talk('please speak the body of the mail')
    message = get_audio()
    send_email(receiver, subject, message)
    print('mail has been succesfully sent')
    talk('mail has been succesfully sent')
    print('Do you want to send more email?')
    talk('Do you want to send more email?')
    send_more = get_audio()
    if 'yes' in send_more:
        get_email_info()
    else:
        print('thank you for using this mail service')
        talk('thank you for using this mail service')

get_email_info()