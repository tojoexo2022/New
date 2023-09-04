import tkinter as tk
import os
import boto3
import pywhatkit
from tkinter import simpledialog
import speech_recognition as sr
import datetime as dt
import cv2
import time
from instabot import Bot

myec2 = None  # Initialize myec2 as None

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)
            return user_input
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, could not understand your speech.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def create_basic_window():
    global myec2  # Access the global myec2 variable
    root = tk.Tk()
    root.title("Basic GUI")
    root.geometry("400x650")
    
    #date
    date = dt.datetime.now()
    label = tk.Label(root, text="%s" % date)
    label.pack()

    # Add widgets and functionality here
    label = tk.Label(root, text="Hello Jarvis here by Team Tech Buddies:")
    label.pack()

    def enable_voice_assistance():
        user_input = get_voice_input()
        if user_input:
            process_voice_command(user_input)
    
    voice_assistance_button = tk.Button(root, text="Voice Assistance", command=enable_voice_assistance)
    voice_assistance_button.pack(pady=20)

    button = tk.Button(root, text="Email", command=on_button_email)
    button.pack(pady=10)

    button = tk.Button(root, text="EC2", command=on_button_ec2)
    button.pack(pady=10)
    
    button = tk.Button(root, text="Add S3 Bucket", command=s3_bucket_create)
    button.pack(pady=10)

    button = tk.Button(root, text="Notepad", command=on_button_click)
    button.pack(pady=10)

    button = tk.Button(root, text="Chrome", command=on_click)
    button.pack(pady=10)

    button = tk.Button(root, text="Paint", command=on_click_paint)
    button.pack(pady=10)

    button = tk.Button(root, text="Word", command=on_click_word)
    button.pack(pady=10)
    
    button = tk.Button(root, text="Play on YouTube", command=youtube_music)
    button.pack(pady=10)
    
    button = tk.Button(root, text="Click Photo", command=take_photo)
    button.pack(pady=10)
    
    exit_button = tk.Button(root, text="Exit", width=10, fg="#fff", bg="#f00", command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()

def on_button_email():
    msg = "Hello from python"
    recipient_email = get_voice_input()
    if not recipient_email:
        recipient_email = simpledialog.askstring("Input", "Enter recipient's email address:")
    if recipient_email:
        pywhatkit.send_mail("testprect@gmail.com", "aljeobaueiacqtko", "test code",msg, recipient_email)

def on_button_click():
    os.system("notepad")

def on_click():
    os.system("start chrome")
    
def on_click_paint():
    os.system("start mspaint")

def on_click_word():
    os.system("start write")
    
def s3_bucket_create():
    ec2_client = boto3.client('ec2')
    response_ec2 = ec2_client.describe_instances()

    s3_client = boto3.client('s3')

    response_s3 = s3_client.create_bucket(
        ACL='private',
        Bucket='shajafi',
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )

def youtube_music():
    final_music = "dil meri na sune"
    print(f"playing {final_music} on youtube")
    pywhatkit.playonyt(final_music)

def take_photo():
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    ret, frame = cap.read()
    if ret:
        cv2.imshow('photo.jpg', frame)
        cv2.imwrite('photo.jpg',frame)
        cap.release()
        cv2.destroyAllWindows()

create_basic_window()