from tkinter import *
from tkinter import ttk
import requets
city_name = "badin"
KEY
data = requests.get(https://api.openweathermap.org/data/2.5/weather?id="+city_name+"&appikeyd={API  }}).json
print(data)









win = Tk()
#win.title("Wscube Tech")
win.config(bg="light blue")
win.geometry("500x570")

name_label = Label(win, text="Wscube Weathwer App", 
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450) 

#list_name = #  List of provinces in Pakistan
pakistan_states = [
    "Punjab",
    "Sindh",
    "Khyber Pakhtunkhwa",
    "Balochistan",
    "Islamabad Capital Territory",
    "Gilgit-Baltistan",
    "Azad Jammu and Kashmir"
]

# Print the list
print(pakistan_states)

com = ttk.Combobox(win, text="Wscube Weathwer App",values=list_name 
                   font=("Time New Roman",30,"bold"))
com.place(x=25,y=120,height=50,width=450)

done_button =_Button(win, text="Done",
                   font=("Time New Roman",30,"bold"))
done_button.place(y=190,height=50,width=100,x=200)


w_label = Label(win, text="Weathwer climate", 
                   font=("Time New Roman",20,))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win, text="", 
                   font=("Time New Roman",20,))
w_label1.place(x=250,y=260,height=50,width=210)




wb_label = Label(win, text="", 
                   font=("Time New Roman",17,))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1 = Label(win, text="Weather Discription", 
                   font=("Time New Roman",17,))
wb_label1.place(x=250,y=330,height=50,width=210)


temp_label = Label(win, text="Temperature", 
                   font=("Time New Roman",17,))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win, text="", 
                   font=("Time New Roman",17,))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label = LabeL(win,text="Pressure",
                   font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)
per_label1 = Label(win,text="",
                  font=("Time New Roman",20))
per_label1.place(x=250,y=478,height=50,width=250)




win.mainloop()


