"""virtual assistant delta """
import pyttsx3
import datetime
import JarvisAI
import os
import time
from geopy.geocoders import Nominatim
import speech_recognition as sr
import wikipedia
import pprint
import webbrowser
import pyjokes
import ctypes
import requests
from tkinter import *

assistantName = "Delta Virtual Assistant 2.0"
obj = JarvisAI.JarvisAssistant()

class commands:
    
    def speak(self,audio):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)
        self.engine.say(audio)
        self.engine.runAndWait()

    def greet(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning!")
        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("I'm delta, Here to help.")
        
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        
        except Exception as e:
            print("Say that again please...")
            return "None"             """ Solve doubt here"""
        return query
    

class GUI(commands):

    def __init__(self):
        self.window = Tk()
        self.window.title(assistantName)
        self.window.geometry("600x400")
        self.window.configure(bg="white")
        self.window.iconbitmap("C:/Users/user/Desktop/DELTA/DELTA GUI/_resources/main.ico")
        self.window.resizable(0,0)
        
        # self.window.iconbitmap('app_icon.ico')       # solve doubt here
        
    def guiLayout(self):
        self.name_label = Label(text = assistantName,width = 300, bg = "white", fg="grey", font = ("Calibri", 13))
        self.name_label.pack()
        
        self.canvas = Canvas(self.window,width = 398, height = 400,bg='black')
        self.canvas.pack(side= RIGHT)
        self.img = PhotoImage(file="C:/Users/user/Desktop/DELTA/DELTA GUI/_resources/jarvis.gif")
        self.canvas.create_image(201,218,image=self.img)

#C:/Users/user/Desktop/DELTA/DELTA GUI

    def instructions(self):
        self.insWindow = Toplevel(self.window)
        self.insWindow.title("Instructions Page")
        self.insWindow.geometry("690x760")
        self.insWindow.iconbitmap("C:/Users/user/Desktop/DELTA/DELTA GUI/_resources/main2.ico")
        self.canvas = Canvas(self.insWindow,width = 680, height = 710,bg='white')
        self.canvas.pack(expand= TRUE, fill=BOTH)
        self.inst_photo = PhotoImage(file = "C:/Users/user/Desktop/DELTA/DELTA GUI/_resources/instructions.png")
        self.canvas.create_image(345,380,image=self.inst_photo)
     
    def allButtons(self):
        # mic button
        self.microphone_photo = PhotoImage(file = "C:/Users/user/Desktop/DELTA/DELTA GUI/_resources/logo.png")
        self.microphone_button = Button(image=self.microphone_photo, command = self.Run, bg= 'black', borderwidth=0)
        self.microphone_button.place(x=39,y=100)

        # exit button
        self.exitbtn_photo = PhotoImage(file = "C:/Users/user/Desktop/DELTA/DELTA GUI/_resources/exit_button.png")
        self.exitbtn = Button(image=self.exitbtn_photo, command = self.stop_exit,bg= 'black',borderwidth=0)
        self.exitbtn.place(x=68,y=270)

        # instruction button
        self.insbtn_photo = PhotoImage(file = "C:/Users/user/Desktop/DELTA/DELTA GUI/_resources/ins.png")
        self.insbtn = Button(image=self.insbtn_photo, command = self.instructions,borderwidth=0)
        self.insbtn.place(x=567,y=27)
    
    def Run(self):
        
        self.greet()
        while True:
            query = self.takeCommand().lower()

            if 'what is' in query:
                try:
                    query = query.replace("what is", "")
                    try:
                        self.speak('Searching Wikipedia...')
                        results = wikipedia.summary(query, sentences=3)
                        self.speak("According to wikipedia")
                        pprint.pprint(results)
                        self.speak(results)
                    except:
                        res = wikipedia.search(query)
                        self.speak("Direct search not found, here are some related topics")
                        pprint.pprint(res)
                
                except Exception as e:
                    print("Unable to process your request!!!")

            elif 'who is' in query:
                query = query.replace("who is", "")
                try:
                    webbrowser.open(query)
                    results = wikipedia.summary(query, sentences=3)
                    self.speak(results)
                except:
                    self.speak("Try adding a middle name")
                    self.speak("If search doesn't exist, try these")
                    res = wikipedia.search(query)
                    pprint.pprint(res)


            elif 'youtube' in query:
                self.speak("opening youtube")
                webbrowser.open("youtube.com")
            
            #ADD MORE COMMANDS

            elif 'news' in query:
                try:
                    news = obj.news()
                    self.speak(f"I have found {len(news)} topics, that you can reed, I'll reed the first 2 of them")
                    pprint.pprint("\n", news)
                    self.speak(news[0])
                    self.speak(news[1])

                except:
                    self.speak("WI-FI is slow")

            elif 'google' in query:
                webbrowser.open("google.com")

            elif 'get exact location of' in query:
                query = query.replace("get exact location of", "")
                loc = Nominatim(user_agent="GetLoc")
                getLoc = loc.geocode(query)
                self.speak("Locating ", query, " ...")
                try:
                    self.speak(getLoc.address)
                    self.speak(getLoc.address)
                    print(getLoc.address)
                    lat = getLoc.latitude
                    lon = getLoc.longitude
                    print("Latitude = ", lat, "\n")
                    self.speak("Latitude = ", lat)
                    print("Longitude = ", lon)
                    self.speak("Longitude = ", lon)
                except:
                    self.speak("location not found")

            elif 'hack' in query:
                try:
                    query = query.replace("hack", "")
                    os.system(f'cmd /c "python main.py {query}"')
                    print(f"Hacking{query}")
                    self.speak(f"Hacking {query}")
                    self.speak("Attempt to login in")
                except:
                    self.speak("Error while accessing account, please try again later")
                    print("Error while accessing account, please try again later")
            
            elif 'where is' in query:
                query = query.replace("where is", "")
                loc = Nominatim(user_agent="GetLoc")
                getLoc = loc.geocode(query)
                self.speak("Locating ", query, " ...")
                try:
                    self.speak(getLoc.address)
                    print(getLoc.address)
                    lat = getLoc.latitude
                    lon = getLoc.longitude
                    print("Latitude = ", lat, "\n")
                    self.speak("Latitude = ", lat)
                    print("Longitude = ", lon)
                    self.speak("Longitude = ", lon)
                except:
                    self.speak("location not found")

            elif 'your code| the code' in query:
                print("my code is a 500 line complex code that is pretty hard to show")
                self.speak("my code is a 500 line complex code that is pretty hard to show")
                print("however you can find my code at https://github.com/kprosoft")
                self.speak("however you can find my code at https://github.com/kprosoft")

            elif 'locate' in query:
                geoLoc = Nominatim(user_agent="GetLoc")
                self.speak("Enter latitude:")
                lat = self.takeCommand()
                print(lat)
                self.speak("Enter Longitude:")
                lon = self.takeCommand()
                print(lon)
                locname = geoLoc.reverse(f"{lat}, {lon}")
                try:
                    self.speak(locname.address)
                    print(locname.address)
                except:
                    self.speak("address not found")


            #elif 'what is' in query:
                #topic = query.split('  ')[-2]
                #wiki = obj.tell_me(topic)
                #print(wiki)
                #self.speak(wiki)

            elif 'stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open' in query:
                res = query.replace("open", "")
                self.speak(f"Opening {res}")
                webbrowser.open(res)

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                self.speak(f"Sir, the time is {strTime}") 
                    
            elif 'hi'in query or 'hello' in query:
                self.speak("Hey")
            
            elif 'what are you doing'in query:
                self.speak("Standing-by for instructions")
            
            elif 'alexa'in query or 'siri'in query or 'crotana'in query:
                self.speak("I'm a fan of helpful beings such as my self")
            
            elif 'creator'in query or 'who is your creator'in query:
                self.speak("world data inc")
                print("WORLD DATA, inc")

            elif 'joke' in query or 'tell a joke' in query:
                jk = pyjokes.get_joke()
                self.speak(jk)
                pprint.pprint(jk)
            
            elif 'write a memo' in query:
                self.speak("what should I write")
                note = self.takeCommand()
                memo = open("memo.txt",'w')
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                memo.write(strTime)
                memo.write(" :- ")
                memo.write(note)
            
            elif 'read memo' in query:
                with open("memo.txt","r") as f:
                    print(f.read())
                    self.speak(f.read())

            elif 'read' in query:
                # check if working
                query = query.replace("read", "")
                with open(query, "r") as f:
                    print(f.read())
                    self.speak(f.read())
            
            #elif 'email to me' in query:
             #   try:
              #      speak("What should I say?")
               #     content = takeCommand()
                #    to = "you@youremail.com"    
                 #   sendEmail(to, content)
                  #  speak("Email has been sent!")
                #except Exception as e:
                 #   print(e)
                  #  speak("Sorry, I couldn't send the email")


            elif 'lock windows' in query:
                try:
                    self.speak("locking windows")
                    ctypes.windll.user32.LockWorkStation()
                except Exception:
                    print("Could not process the request")
            
            elif 'shutdown' in query:
                self.speak("shutting down delta")
                self.stop_exit() 

            elif "weather" in query or "temperature" in query:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                self.speak("whats the city name")
                city_name=self.takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                try:
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    self.speak(str((current_temperature)-273.15) + " Celsius" +"\n Humidity percentage " +str(current_humidiy) + "%" +"\n Description:  " +str(weather_description))
                    print(""+str(round((current_temperature)-273.15)) + "°C" +"\n Humidity percentage " +str(current_humidiy) + "%" +"\n Description:  " +str(weather_description))

                except:
                    wet = obj.weather(city=city_name)
                    self.speak(wet)
                    pprint.pprint(wet)

    def stop_exit(self):
        exit()

    def main_window(self):
        self.guiLayout()
        self.allButtons()
        self.window.mainloop()

if __name__ == "__main__":
    start = GUI()
    start.main_window()
    
