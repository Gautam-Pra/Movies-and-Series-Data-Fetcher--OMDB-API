#IMPORTING OF REQUIRED MODULES AND LIBRARIES

import requests
import json
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import io

#INITIALISATION OF WINDOW
root= Tk()

#TITLE OF THE WINDOW
root.title(" Movies and Series- Data Fetcher")

#DIMENSIONS OF THE WINDOW
root.geometry("750x550")
root.maxsize(750,550)
root.minsize(750,550)

#MAIN WINDOW BACKGROUND COLOUR( I TRIED TO PUT AN IMAGE AS BACKGROUND
#COS IT LOOKS COOL BUT THERE IS NO SUCH TRNSPARENT PROPERTY FOR LABEL IN TKINTER)
root.configure(bg="#1c1c1c")

#CANVAS FOR CENTRAL IMAGE SEARCH HERE! IN MAIN WINDOW
canvas= Canvas(root, width= 400,
                     height= 300,
                     bg="#1c1c1c",
                     highlightthickness=0,
                     borderwidth=0,
                     border=0)

canvas.place(anchor = "s",
             relx = .55,
             rely = 0.9)

#LOAD AN IMAGE IN THE MAIN WINDOW
img= ImageTk.PhotoImage(Image.open("srch.png"))

#ADD IMAGE TO CANVAS ITEM
canvas.create_image(8,20,anchor= "nw",image=img)

"""
C = Canvas(root, bg="blue", height=550, width=750)
filename = ImageTk.PhotoImage(file = "bg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
"""

#FIRST TOP LABEL IN THE WINDOW
IMAGE=PhotoImage(file="TITLE.png")
top_label= Label(image=IMAGE,
                 bg="#1c1c1c",
                 padx="300")

top_label.place(anchor = CENTER,
                relx = .5,
                rely = 0.04)


#API KEY FOR DATABASE(PLEASE CHANGE IT ACCORDING TO YOUR NEED AS IT HAVE 1000 DAILY REQUEST LIMIT, DONT USE IT ANYWHERE OTHER THAN THIS PROGRAM)
API_KEY="d7caee7d"

#FUNCTION DEFINITION OF SETTINGS() FOR BUTTON
def SETTINGS():
    #INITIALISATION OF SETTINGS WINDOW
    SET_WINDOW= Tk()
    SET_WINDOW.bell()

    #SETTINGS WINDOW TITLE 
    SET_WINDOW.title("Settings")

    #DIMENSIONS OF THE WINDOW
    SET_WINDOW.geometry("445x300")
    SET_WINDOW.maxsize(450,300)
    SET_WINDOW.minsize(450,300)

    #MAIN WINDOW BACKGROUND COLOUR
    SET_WINDOW.configure(bg="#1c1c1c")
    
    PROJECT_DETAILS_LABEL=Label(SET_WINDOW,text="PROJECT DETAILS:- Helps to know about Movies and Series using API\n",
                                           wraplength=450,
                                           justify="center" ,
                                           font="helvetica 16 bold",
                                           bg="#1c1c1c" ,
                                           fg="white")
    PROJECT_DETAILS_LABEL.pack(side=TOP)
    
    AUTHOR_LABEL=Label(SET_WINDOW,text="AUTHOR:-  ",
                                  wraplength=535,
                                  justify="center" ,
                                  font="Geologica 16 bold",
                                  bg="#1c1c1c" ,
                                  fg="white")
    AUTHOR_LABEL.pack(side=TOP)
    
    API_USED=Label(SET_WINDOW,text="API USED:- OMDB API",
                              wraplength=535,
                              justify="center" ,
                              font="helvetica 8 bold",
                              bg="#1c1c1c" ,
                              fg="white")
    
    API_USED.pack(side=BOTTOM)
    
    SET_WINDOW.mainloop()

#SETTINGS BUTTON CONFIGURATIONS
BUTTON_IMAGE= ImageTk.PhotoImage(file="settings.png")
SETTINGS_BUTTON= Button(root, image=BUTTON_IMAGE,
                              command= SETTINGS ,
                              borderwidth=0,
                              bg="#1c1c1c")

SETTINGS_BUTTON.image=BUTTON_IMAGE
SETTINGS_BUTTON.place(anchor = CENTER,
                      relx = 0.97,
                      rely = 0.04)


#FUNCTION DEFINITION OF SEARCH() FOR BUTTON
def search(event=None):

    try:
        
        root.bell()
        
        #REMOVES SEARCH HERE! IMAGE FROM CENTER
        canvas.delete('all')
        
        global title
        title=datavalue.get()
        global response
        response = requests.get(f'http://www.omdbapi.com?t={title}&apikey={API_KEY}')
        response.raise_for_status()
        global json_data
        json_data= json.loads(response.text)
        
        #LOADING OF POSTER IMAGE FROM URL
        global posterurl
        posterurl=json_data['Poster']
        global r
        r = requests.get(posterurl)
       
        global pilImage
        pilImage = Image.open(io.BytesIO(r.content))
      
        pilImage = pilImage.resize((175, 250))
      
        #FRAME-1
        frame1= Frame(root ,bg="#1c1c1c",)
        frame1.place(anchor = "se",
                     relx = 0.99,
                     rely = 0.57)

        #POSTER IMAGE
        poster=ImageTk.PhotoImage(pilImage)      
        label=Label(frame1,image=poster ,
                           bg="#1c1c1c",
                           fg="white")
        
        label.image=poster
        label.grid()

        #USER DEFINED FUNCTION TO DOWNLOAD IMAGE IN LOCAL DEVICE
        def imgdownload():
            img_data = requests.get(posterurl).content
            with open('Poster.jpg', 'wb') as handler:
                 handler.write(img_data)
            messagebox.showinfo("Download Progress","Downloaded")

         
        if json_data['Type']=="series":
            TYPE= json_data['Type']
            TYPE_CAPITAL= TYPE.capitalize()
            
            SEASONS=", Seasons: "+json_data['totalSeasons']
            SEASONS_CAPITAL=SEASONS.capitalize()

            TYPE_SEASONS= TYPE+SEASONS
            
            LABEL_SERIES=Label(root,text= TYPE_SEASONS,
                                    font="helvetica 16 bold",
                                    bg="#1c1c1c",
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
                                   bg="#1c1c1c",
                                   fg="white")

            LABEL_MOVIES.place(anchor = "s",
                               relx = 0.87,
                               rely = 0.62)
            
        
        #BUTTON CONFIG'S
        buttonimage= ImageTk.PhotoImage(file="download_poster.png")
        button1= Button(root, image=buttonimage,
                        command=imgdownload,
                        border=0,
                        bg="#1c1c1c")
        
        button1.image=buttonimage
        button1.place(anchor = "s",
                      relx = 0.88,
                      rely = 0.69)

        #FRAME-2
        frame2= Frame(root)
        frame2.place(anchor = "nw",
                     relx = 0.01,
                     rely = 0.09)

        #LOADING OF TITLE FROM JSON TO WINDOW
        data_textt="Title: " +json_data['Title']+"              "
        
        LABELt=Label(frame2,text=data_textt,
                            font="helvrtica 16 bold",
                            bg="#1c1c1c",
                            fg="white")
        
        LABELt.pack(side=LEFT)
        LABELt.configure(text=data_textt)
        LABELt['text']=data_textt

        #FRAME-3
        frame3= Frame(root, bg="blue")
        frame3.place(anchor = "nw",
                     relx = 0.01,
                     rely = 0.16)

        #LOADING OF RELEASE YEAR FROM JSON TO WINDOW
        data_textt="Release Year: " + json_data['Year']+"          "
        LABELr=Label(frame3,text=data_textt,
                            font="helvetica 15 bold",
                            bg="#1c1c1c",
                            fg="white")
        
        LABELr.pack(side=LEFT)
        LABELr.configure(text=data_textt)
        LABELr['text']=data_textt



        #FRAME-4
        frame4= Frame(root, bg="blue")
        frame4.place(anchor = "nw",
                     relx = 0.01,
                     rely = 0.23)

        #LOADING OF RATED DATA FROM JSON TO WINDOW
        data_textt="Rated: " + json_data['Rated']+"          "
        LABELrt=Label(frame4,text=data_textt,
                             font="helvetica 15 bold" ,
                             bg="#1c1c1c",
                             fg="white")
        
        LABELrt.pack(side=LEFT)
        LABELrt.configure(text=data_textt)
        LABELrt['text']=data_textt



        #FRAME-5
        frame5= Frame(root, bg="blue")
        frame5.place(anchor = "nw",
                     relx = 0.01,
                     rely = 0.30)

        #LOADING OF RUNTIME/DURATION DATA FROM JSON TO WINDOW
        data_textt="Runtime: " + json_data['Runtime']+"          "
        LABELd=Label(frame5,text=data_textt,
                            font="helvetica 15 bold",
                            bg="#1c1c1c",
                            fg="white")
        
        LABELd.pack(side=LEFT)
        LABELd.configure(text=data_textt)
        LABELd['text']=data_textt


        #FRAME-6
        frame6= Frame(root, bg="blue")
        frame6.place(anchor = "nw",
                     relx = 0.01,
                     rely = 0.37)

        #LOADING OF GENRE DATA FROM JSON TO WINDOW
        data_textt="Genre: " + json_data['Genre']+"                  "
        LABELg=Label(frame6,text=data_textt,
                            font="helvetica 15 bold",
                            bg="#1c1c1c",
                            fg="white")
        
        LABELg.pack(side=LEFT)
        LABELg.configure(text=data_textt)
        LABELg['text']=data_textt


        #FRAME-7
        frame7= Frame(root,
                      bg="blue",
                      height=10)
        
        frame7.place(anchor = "nw",
                     relx = 0.01,
                     rely = 0.44)

        #LOADING OF COUNTRY DATA FROM JSON TO WINDOW
        data_textt="Country: " + json_data['Country']+"                                     "
        LABELc=Label(frame7,text=data_textt,
                            font="helvetica 15 bold" ,
                            bg="#1c1c1c",
                            fg="white")
        
        LABELc.pack(side=LEFT)
        LABELc.configure(text=data_textt)
        LABELc['text']=data_textt



        #FRAME-8
        frame8= Frame(root, bg="blue",
                            width=100,
                            height=10)
        
        frame8.place(anchor = "nw",
                     relx = 0.01,
                    rely = 0.51)

        #LOADING OF LANGAUGE DATA FROM JSON TO WINDOW
        data_textt="Language: " + json_data['Language']+"                                                              "
        LABELl=Label(frame8,text=data_textt,
                            font="helvetica 15 bold",
                            wraplength=450,
                            justify="left",
                            bg="#1c1c1c",
                            fg="white")
        
        LABELl.pack(side=LEFT)
        LABELl.configure(text=data_textt)
        LABELl['text']=data_textt


        #FRAME-9
        frame9= Frame(root,
                      bg="blue")
        frame9.place(anchor = "nw",
                     relx = 0.01,
                     rely = 0.62)

        #LOADING OF PLOT DATA FROM JSON TO WINDOW
        data_textt="Plot: "  + json_data['Plot']+"                  "
        LABELpl=Label(frame9,text=data_textt,
                             font="helvetica 15 bold",
                             wraplength=500,
                             justify="left" ,
                             bg="#1c1c1c",
                             fg="white")
        
        LABELpl.pack(side=LEFT, fill="x")

    except KeyError:
         messagebox.showinfo("Please Input Correct Name","An Error Ocuured Due to Wrong Input Of Movies or Series")

#Bind the Enter Key to Call an event
root.bind('<Return>',search)


#FRAME-13
frame13= Frame(root,  bg="#1c1c1c",
                      width=100,
                      height=10,
                      border=0)

frame13.place(anchor = "center",
              relx = 0.5,
              rely = 0.93)

#TEXT LABEL FOR "ENTER MOVIES OR SERIES"
data=Label(frame13, text="Enter Movie or Series: ",
                    bg="#1c1c1c",
                    font="helvetica 17 bold",
                    fg="#deddd9",
                    border=1)

data.grid(row=0, column=0)

#WHITE SPACE
data=Label(frame13, text=" ",
                    bg="#1c1c1c",
                    font="helvetica 17 bold",
                    fg="#27292b",
                    border=1)

data.grid(row=0, column=3)

#MOVIES OR SERIES NAME DATA ENTRY
datavalue=StringVar()
dataentry= Entry(frame13,
                 textvariable=datavalue,
                 bg="#1c1c1c",
                 border=1,
                 fg="white",
                 font="helvetica 14 bold")

dataentry.grid(row=0, column=2)

#SEARCH BUTTON
dataimg=PhotoImage(file="search.png")
databutton=Button(frame13, image=dataimg,
                           border=0,
                           bg="#1c1c1c",
                           fg="#1c1c1c",
                           command=search)

databutton.grid(row=0, column=4)

#MAINLOOP FOR MAIN WINDOW SO THAT THE MAIN WINDOW WILL NOT CLOSE
root.mainloop()
