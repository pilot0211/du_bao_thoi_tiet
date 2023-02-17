import requests
import tkinter
import datetime
from PIL import ImageTk, Image
from tkinter import Frame
giao_dien = tkinter.Tk()
giao_dien.title("Weather Application")
giao_dien.geometry('800x700')
font = ("Comic Sans MS",15)


#line
horizontal =Frame(giao_dien, bg='#191970', height=4,width=800)
horizontal.place(relx = 0, rely = 0.4)


#img
img1= (Image.open("D:/hocthem/du_bao_thoi_tiet/weather.jpg"))
resized_img1= img1.resize((200,200), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(resized_img1)

img2= (Image.open("D:/hocthem/du_bao_thoi_tiet/cloud.jpg"))
resized_img2= img2.resize((100,100), Image.ANTIALIAS)
image2 = ImageTk.PhotoImage(resized_img2)

img3= (Image.open("D:/hocthem/du_bao_thoi_tiet/temp.jpg"))
resized_img3= img3.resize((100,100), Image.ANTIALIAS)
image3 = ImageTk.PhotoImage(resized_img3)

img4= (Image.open("D:/hocthem/du_bao_thoi_tiet/water.jpg"))
resized_img4= img4.resize((100,100), Image.ANTIALIAS)
image4 = ImageTk.PhotoImage(resized_img4)

img5= (Image.open("D:/hocthem/du_bao_thoi_tiet/wind.jpg"))
resized_img5= img5.resize((100,100), Image.ANTIALIAS)
image5 = ImageTk.PhotoImage(resized_img5)
#def
def search():
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    city = tb1.get().lower().replace(" ","").strip()
    api_key = 'fe53bfd100e8ca1c2ca47f202a2e9b9c'
    url_getapi = url + city + "&appid=" + api_key
    data = requests.get(url_getapi).json()
    lb2.set(data['name']+','+data['sys']['country'])
    lb10.set(data['weather'][0]['main'])
    lb11.set(data['main']['temp'])
    lb12.set(data['main']['humidity'])
    lb13.set(data["wind"]['speed'])


#label
Font_tuple = ("Comic Sans MS", 15, "bold")
label1 = tkinter.Label(giao_dien,text="Weather Report" ,fg='white',font=Font_tuple, bg="#191970",width=800,height=2)
label1.place(relx = 0.5, rely = 0.05, anchor = 'center')

lb2 = tkinter.StringVar(value='NA-/')
label2 = tkinter.Label(giao_dien,fg='white',font=font,bg="#191970",textvariable=lb2)
label2.place(relx = 0.05, rely = 0.03)

lb3 = tkinter.StringVar(value=datetime.date.today())
label3 = tkinter.Label(giao_dien,fg='white',font=font,bg="#191970",textvariable=lb3)
label3.place(relx = 0.8, rely = 0.03)

label4 = tkinter.Label(giao_dien,fg='white',image=image1)
label4.place(relx = 0.01, rely = 0.1)

label5 = tkinter.Label(giao_dien,text="City or Country Name",font=Font_tuple, fg="#191970")
label5.place(relx = 0.32, rely = 0.15)

label6 = tkinter.Label(giao_dien,fg='white',image=image2)
label6.place(relx = 0.11, rely = 0.5)

label7 = tkinter.Label(giao_dien,fg='white',image=image3)
label7.place(relx = 0.34, rely = 0.5)

label8 = tkinter.Label(giao_dien,fg='white',image=image4)
label8.place(relx = 0.57, rely = 0.5)

label9 = tkinter.Label(giao_dien,fg='white',image=image5)
label9.place(relx = 0.8, rely = 0.5)

lb10 = tkinter.StringVar(value='NA-/')
label10 = tkinter.Label(giao_dien,fg='black',font=font,textvariable=lb10)
label10.place(relx = 0.14, rely = 0.7)

lb11 = tkinter.StringVar(value='NA-/')
label11 = tkinter.Label(giao_dien,fg='black',font=font,textvariable=lb11)
label11.place(relx = 0.37, rely = 0.7)

lb12 = tkinter.StringVar(value='NA-/')
label12 = tkinter.Label(giao_dien,fg='black',font=font,textvariable=lb12)
label12.place(relx = 0.6, rely = 0.7)

lb13 = tkinter.StringVar(value='NA-/')
label13 = tkinter.Label(giao_dien,fg='black',font=font,textvariable=lb13)
label13.place(relx = 0.83, rely = 0.7)


#text box
tb1 = tkinter.StringVar()
text_box1 = tkinter.Entry(giao_dien,textvariable=tb1,fg='black',font = ("Comic Sans MS",15))
text_box1.place(relx = 0.32,rely = 0.25,height=30,width=350)


#button
btn1 = tkinter.Button(giao_dien,font = font,text='search',bg='white',command=search)
btn1.place(relx = 0.8, rely = 0.25,width=80,height=30)



giao_dien.mainloop()
