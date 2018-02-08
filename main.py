from pynput.keyboard import Key, Controller
import speech_recognition as sr
import subprocess, time, webbrowser, keyboard, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import mkj_pkg.main as mkj
while True:
    while keyboard.is_pressed('ins'):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening... ")
                audio = r.listen(source)
                BING_KEY = ""  #API KEY HERE
                word = r.recognize_bing(audio, key=BING_KEY)
                print(word)
                mkj.ty(word)
                mkj.pr(Key.enter)