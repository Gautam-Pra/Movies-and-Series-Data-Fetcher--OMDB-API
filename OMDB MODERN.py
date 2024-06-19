#IMPORTING OF REQUIRED MODULES AND LIBRARIES

import requests
import json
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import io
import customtkinter

#Setting up theme of our app
customtkinter.set_appearance_mode ("dark")

# create CT window like you do with the k window
root = customtkinter.CTk()

#TITLE OF THE WINDOW
root.title(" Movies and Series- DATA Fetcher")

#DIMENSIONS OF THE WINDOW
root.geometry("750x550")
root.maxsize(750,550)
root.minsize(750,550)

#FIRST TOP LABEL IN THE WINDOW
TOP_LABEL=customtkinter.CTkLabel(root, text="Fetch DATA",
                                                                           font=("Impact",34),
                                                                           fg_color="transparent")
TOP_LABEL.place(anchor = CENTER,
                                relx = .5,
                                rely = 0.04)

#FOR CENTRAL IMAGE SEARCH HERE! IN MAIN WINDOW
CENTRAL_LABEL1=  customtkinter.CTkLabel(root, text="Search Here!",
                                                                                       font=("Impact",39),
                                                                                       fg_color="transparent",
                                                                                      text_color=("#A9A9A9"))
CENTRAL_LABEL1.place(anchor = "s",
                                          relx = 0.5,
                                          rely = 0.5)

IMAGE=ImageTk.PhotoImage(file="search_logo.png")
CENTRAL_LABEL2= Label(image=IMAGE,
                                            bg="#252425",
                                            border=0,
                                            padx="300"  )

CENTRAL_LABEL2.place(anchor = CENTER,
                                          relx = 0.5,
                                          rely = 0.56)

try:
	requests.get('https://www.google.com/')
except:
	print('[!] No internet connection...Please connect to the Internet')
	messagebox.showwarning("Internet Connection","Please Connect to Internet...")



#API KEY FOR DATABASE(PLEASE CHANGE IT ACCORDING TO YOUR NEED AS IT HAVE 1000 DAILY REQUEST LIMIT, DONT USE IT ANYWHERE OTHER THAN THIS PROGRAM)
API_KEY="d7caee7d"

#FUNCTION DEFINITION OF SETTINGS() FOR BUTTON
def SETTINGS():

    " Setting up theme of your app"
    customtkinter.set_appearance_mode ("dark")
    
    #INITIALISATION OF SETTINGS WINDOW
    SET_WINDOW= customtkinter.CTk()
    SET_WINDOW.bell()

    #SETTINGS WINDOW TITLE 
    SET_WINDOW.title("Settings")

    #DIMENSIONS OF THE WINDOW
    SET_WINDOW.geometry("445x300")
    SET_WINDOW.maxsize(450,300)
    SET_WINDOW.minsize(450,300)

    
    PROJECT_DETAILS_LABEL=customtkinter.CTkLabel(SET_WINDOW,text="PROJECT DETAILS:- Helps to know about Movies and Series using API\n",
                                                                                                                           wraplength=450,
                                                                                                                           justify="center" ,
                                                                                                                           font=("helvetica", 16)  )
    PROJECT_DETAILS_LABEL.pack(side=TOP)
    
    AUTHOR_LABEL=customtkinter.CTkLabel(SET_WINDOW,text="CREDITS:-  ",
                                                                                                          wraplength=450,
                                                                                                          justify="center" ,
                                                                                                          font=("helvetica", 17))
    AUTHOR_LABEL.pack(side=TOP)
    
    API_USED=customtkinter.CTkLabel(SET_WINDOW,text="API USED:- OMDB API",
                                                                                              wraplength=535,
                                                                                              justify="center" ,
                                                                                              font=("helvetica", 11),
                                                                                              fg_color="transparent" )
    
    API_USED.pack(side=BOTTOM)
    
    SET_WINDOW.mainloop()

#SETTINGS BUTTON CONFIGURATIONS
BUTTON_IMAGE= customtkinter.CTkImage(Image.open("settings.png"),size=(30, 30))
SETTINGS_BUTTON= customtkinter.CTkButton(master=root,text="",
                                                                                     image=BUTTON_IMAGE,
                                                                                     command= SETTINGS ,
                                                                                     width=4,
                                                                                     height=4,
                                                                                     border_width =0,
                                                                                     corner_radius=15, fg_color="transparent", hover=False)

SETTINGS_BUTTON.image=BUTTON_IMAGE
SETTINGS_BUTTON.place(anchor = CENTER,
                                              relx = 0.97,
                                              rely = 0.04)


#FUNCTION DEFINITION OF SEARCH() FOR BUTTON
def search(event=None):
    try:
        root.bell()
        
        #REMOVES SEARCH HERE! IMAGE FROM CENTER
        CENTRAL_LABEL1.configure(text="       ")
        CENTRAL_LABEL2.config(image="")
        
        global TITLE
        TITLE=DATAVALUE.get()
        global response
        response = requests.get(f'http://www.omdbapi.com?t={TITLE}&apikey={API_KEY}')
        response.raise_for_status()
        global json_data
        json_data= json.loads(response.text)
        
        #LOADING OF POSTER IMAGE FROM URL
        global POSTERURL
        POSTERURL=json_data['Poster']
        global r
        r = requests.get(POSTERURL)
       
        global PILIMAGE
        PILIMAGE = Image.open(io.BytesIO(r.content))
      
        PILIMAGE = PILIMAGE.resize((200, 350))
      
        #FRAME-1
        FRAME1= customtkinter.CTkFrame(root ,bg_color="#252425",
                                                                                 fg_color="#252425",
                                                                                 border_width=0)
        FRAME1.place(anchor = "se",
                                     relx = 1.01,
                                     rely = 0.57)

        #POSTER IMAGE
        POSTER=customtkinter.CTkImage(PILIMAGE,size=(175, 270))      
        LABEL=customtkinter.CTkLabel(FRAME1,image=POSTER ,
                                                                                text="",
                                                                                corner_radius=20 )
        
        LABEL.image=POSTER
        LABEL.grid()

        #USER DEFINED FUNCTION TO DOWNLOAD IMAGE IN LOCAL DEVICE
        def imgdownload():
            img_DATA = requests.get(POSTERURL).content
            with open('POSTER.jpg', 'wb') as handler:
                 handler.write(img_DATA)
            messagebox.showinfo("Download Progress","Downloaded")

         
        if json_data['Type']=="series":
            TYPE= json_data['Type']
            TYPE_CAPITAL= TYPE.capitalize()
            
            SEASONS=", Seasons: "+json_data['totalSeasons']
            SEASONS_CAPITAL=SEASONS.capitalize()

            TYPE_SEASONS= TYPE+SEASONS
            
            LABEL_SERIES=Label(root,text= TYPE_SEASONS,
                                                            font="helvetica 16 bold",
                                                            bg="#252425",
                                                            fg="white")
                                    
            LABEL_SERIES.place(anchor = "s",
                                               relx = 0.87,
                                               rely = 0.62)
        else:
            
            TYPE= json_data['Type']
            TYPE_CAPITAL= TYPE.capitalize()
            
            TYPE_MOVIES="          "+TYPE_CAPITAL+"          "
            LABEL_MOVIES=Label(root,text = TYPE_MOVIES,
                                                               font="helvetica 16 bold",
                                                               bg="#252425",
                                                               fg="white")

            LABEL_MOVIES.place(anchor = "s",
                                                   relx = 0.87,
                                                   rely = 0.62)
                                
        
        #BUTTON CONFIG'S
        BUTTONIMAGE= customtkinter.CTkImage(Image.open("download_poster.png"),size=(150, 36))
        BUTTON1= customtkinter.CTkButton(master=root,text="",
                                                                                                 image=BUTTONIMAGE,
                                                                                                 command=imgdownload,
                                                                                                 fg_color="transparent",
                                                                                                 hover=False,
                                                                                                 font=("helvetica" ,30))
                                                    
        BUTTON1.image=BUTTONIMAGE
        BUTTON1.place(anchor = "s",
                                      relx = 0.88,
                                      rely = 0.69)

        #FRAME-2
        FRAME2= customtkinter.CTkFrame(root)
        FRAME2.place(anchor = "nw",
                                     relx = 0.01,
                                     rely = 0.09)

        #LOADING OF TITLE FROM JSON TO WINDOW
        DATA_TEXTt="TITLE: " +json_data['Title']+"              "
        
        LABELt=Label(FRAME2,text=DATA_TEXTt,
                                                font="helvrtica 16 bold",
                                                bg="#252425",
                                                fg="white")
        
        LABELt.pack(side=LEFT)
        LABELt.configure(text=DATA_TEXTt)
        LABELt['text']=DATA_TEXTt

        #FRAME-3
        FRAME3= customtkinter.CTkFrame(root)
        FRAME3.place(anchor = "nw",
                                     relx = 0.01,
                                     rely = 0.16)

        #LOADING OF RELEASE YEAR FROM JSON TO WINDOW
        DATA_TEXTt="Release Year: " + json_data['Year']+"          "
        LABELr=Label(FRAME3,text=DATA_TEXTt,
                                                font="helvetica 15 bold",
                                                bg="#252425",
                                                fg="white")
        
        LABELr.pack(side=LEFT)
        LABELr.configure(text=DATA_TEXTt)
        LABELr['text']=DATA_TEXTt



        #FRAME-4
        FRAME4= customtkinter.CTkFrame(root, bg_color="blue")
        FRAME4.place(anchor = "nw",
                                   relx = 0.01,
                                   rely = 0.23)

        #LOADING OF RATED DATA FROM JSON TO WINDOW
        DATA_TEXTt="Rated: " + json_data['Rated']+"          "
        LABELrt=Label(FRAME4,text=DATA_TEXTt,
                                                 font="helvetica 15 bold" ,
                                                 bg="#252425",
                                                 fg="white")
                            
        LABELrt.pack(side=LEFT)
        LABELrt.configure(text=DATA_TEXTt)
        LABELrt['text']=DATA_TEXTt



        #FRAME-5
        FRAME5= customtkinter.CTkFrame(root, bg_color="blue")
        FRAME5.place(anchor = "nw",
                                     relx = 0.01,
                                     rely = 0.30)

        #LOADING OF RUNTIME/DURATION DATA FROM JSON TO WINDOW
        DATA_TEXTt="Runtime: " + json_data['Runtime']+"          "
        LABELd=Label(FRAME5,text=DATA_TEXTt,
                                                    font="helvetica 15 bold",
                                                    bg="#252425",
                                                    fg="white")
        
        LABELd.pack(side=LEFT)
        LABELd.configure(text=DATA_TEXTt)
        LABELd['text']=DATA_TEXTt


        #FRAME-6
        FRAME6= customtkinter.CTkFrame(root, bg_color="blue")
        FRAME6.place(anchor = "nw",
                                     relx = 0.01,
                                     rely = 0.37)

        #LOADING OF GENRE DATA FROM JSON TO WINDOW
        DATA_TEXTt="Genre: " + json_data['Genre']+"                  "
        LABELg=Label(FRAME6,text=DATA_TEXTt,
                                                    font="helvetica 15 bold",
                                                    bg="#252425",
                                                    fg="white")
        
        LABELg.pack(side=LEFT)
        LABELg.configure(text=DATA_TEXTt)
        LABELg['text']=DATA_TEXTt


        #FRAME-7
        FRAME7= customtkinter.CTkFrame(root,
                                                                          bg_color="blue",
                                                                          height=10)
        
        FRAME7.place(anchor = "nw",
                                     relx = 0.01,
                                     rely = 0.44)

        #LOADING OF COUNTRY DATA FROM JSON TO WINDOW
        DATA_TEXTt="Country: " + json_data['Country']+"                                     "
        LABELc=Label(FRAME7,text=DATA_TEXTt,
                                                    font="helvetica 15 bold" ,
                                                    bg="#252425",
                                                    fg="white")
        
        LABELc.pack(side=LEFT)
        LABELc.configure(text=DATA_TEXTt)
        LABELc['text']=DATA_TEXTt



        #FRAME-8
        FRAME8= customtkinter.CTkFrame(root, bg_color="blue",
                                                                                width=100,
                                                                                height=10)
        
        FRAME8.place(anchor = "nw",
                                     relx = 0.01,
                                     rely = 0.51)

        #LOADING OF LANGAUGE DATA FROM JSON TO WINDOW
        DATA_TEXTt="Language: " + json_data['Language']+"                                                              "
        LABELl=Label(FRAME8,text=DATA_TEXTt,
                                                font="helvetica 15 bold",
                                                wraplength=450,
                                                justify="left",
                                                bg="#252425",
                                                fg="white")
        
        LABELl.pack(side=LEFT)
        LABELl.configure(text=DATA_TEXTt)
        LABELl['text']=DATA_TEXTt


        #FRAME-9
        FRAME9= customtkinter.CTkFrame(root)
        FRAME9.place(anchor = "nw",
                                     relx = 0.01,
                                     rely = 0.62)

        #LOADING OF PLOT DATA FROM JSON TO WINDOW
        DATA_TEXTP="Plot: "  + json_data['Plot']+"                    "
        LABELpl=Label(FRAME9,text=DATA_TEXTP,
                                                 font="helvetica 15 bold",
                                                 wraplength=500,
                                                 justify="left" ,
                                                 bg="#252425" ,
                                                 fg="white" )
        
        LABELpl.pack(side=LEFT, fill="x")
    except KeyError:
            messagebox.showinfo("Please Input Correct Name","An Error Ocuured Due to Wrong Input Of Movies or Series")


#Bind the Enter Key to Call an event
root.bind('<Return>',search)


#FRAME-13
FRAME13= customtkinter.CTkFrame(root,  
                                                                  width=100,
                                                                  height=10,
                                                                  border_color ="#252425",
                                                                  fg_color="#252425")

FRAME13.place(anchor = "center",
                              relx = 0.5,
                              rely = 0.93)

#TEXT LABEL FOR "ENTER MOVIES OR SERIES"
DATA=customtkinter.CTkLabel(FRAME13, text="Enter Movie or Series: ",
                                                                            font=("helvetica", 20),
                                                                            bg_color="#252425")

DATA.grid(row=0, column=0)

#WHITE SPACE
space=customtkinter.CTkLabel(FRAME13, text=" ",
                                                                            font=("helvetica", 17),
                                                                            bg_color="#252425")

space.grid(row=0, column=3)

#MOVIES OR SERIES NAME DATA ENTRY
DATAVALUE=StringVar()
DATAENTRY= customtkinter.CTkEntry(FRAME13,
                                                                     textvariable=DATAVALUE,
                                                                     corner_radius=15,
                                                                     fg_color="transparent",
                                                                     font=("helvetica" ,14))

DATAENTRY.grid(row=0, column=2)

#SEARCH BUTTON
DATAimg=customtkinter.CTkImage(Image.open("search_logo.png"),size=(33, 33))
DATABUTTON=customtkinter.CTkButton(FRAME13, image=DATAimg,
                                                                                            text="",
                                                                                            width=4,
                                                                                            height=4,
                                                                                            corner_radius=15,
                                                                                            fg_color="transparent",
                                                                                            hover=False,
                                                                                            command=search)

DATABUTTON.grid(row=0, column=4)

#MAINLOOP FOR MAIN WINDOW SO THAT THE MAIN WINDOW WILL NOT CLOSE
root.mainloop()
