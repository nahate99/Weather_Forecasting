from tkinter import*
from PIL import ImageTk
from PIL import Image
import w
import requests
class MyWeather:
   
        
    def __init__(self,root):
        self.root=root
        self.root.title("Weather App")
        self.root.geometry("350x400+450+100")
        self.root.config(bg="white")
       #==icon==
        self.search_icon=Image.open("icon/search.png") 
        self.search_icon=self.search_icon.resize((30,30),Image.ANTIALIAS)
        self.search_icon=ImageTk.PhotoImage(self.search_icon)
        
       #==variable== 
        self.var_search=StringVar()
        
        title=Label(self.root,text="Weather_forecast",font=("goudy old style",25,"bold"),bg="#575757",fg="white").place(x=0,y=0,relwidth=1,height=60)
        lbl_city=Label(self.root,text="City Name",font=("goudy old style",12),bg="#033958",fg="white",anchor="w",padx=5).place(x=0,y=60,relwidth=1,height=40)
        txt_city=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow",fg="#262626").place(x=100,y=68,width=200,height=25)
        btn_search=Button(self.root,cursor="hand2",image=self.search_icon,bg="#033958",activebackground="#033958",bd=0,command=self.get_weather).place(x=310,y=65,width=30,height=30)
        
        
        #====result=====
        self.lbl_city=Label(self.root,font=("goudy old style",12),bg="white",fg="green")
        self.lbl_city.place(x=0,y=110,relwidth=1,height=20)
        
        self.lbl_icon=Label(self.root,font=("goudy old style",12),bg="white")
        self.lbl_icon.place(x=0,y=135,relwidth=1,height=100)
        
        self.lbl_temp=Label(self.root,font=("goudy old style",12),bg="white",fg="darkorange")
        self.lbl_temp.place(x=0,y=240,relwidth=1,height=20)
        
        self.lbl_wind=Label(self.root,font=("goudy old style",12),bg="white",fg="blue")
        self.lbl_wind.place(x=0,y=265,relwidth=1,height=20)
        
        
        self.lbl_error=Label(self.root,font=("goudy old style",12),bg="white",fg="red")
        self.lbl_error.place(x=0,y=285,relwidth=1,height=20)

        
        
        
        
        #=====footer====
        lbl_footer=Label(self.root,text="Developed_by_Harish",font=("goudy old style",10),bg="#575757",fg="black",pady=5).pack(side=BOTTOM,fill=X)
        
    def get_weather(self):   
        api_key=w.api_key 
        complete_url=f"https://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
        
        #cityname,countryname,icons,temp_c,temp_f,wind
        if self.var_search.get()=="":
            self.lbl_city.config(text="")
            self.lbl_icon.config(image="")
            self.lbl_temp.config(text="")
            self.lbl_wind.config(text="")
            self.lbl_error.config(text="City name Required")
        else:
            result=requests.get(complete_url)
            if result:
               json=result.json()
               city_name=json["name"]
               country=json["sys"]["country"]
               icons=json["weather"][0]["icon"]
               temp_c=json["main"]["temp"]-273.15
               wind=json["weather"][0]["main"]
            
               self.lbl_city.config(text=city_name+" , "+country)
            #===newicon===
               self.search_icon2=Image.open(f"icon/{icons}.png") 
               self.search_icon2=self.search_icon2.resize((100,100),Image.ANTIALIAS)
               self.search_icon2=ImageTk.PhotoImage(self.search_icon2)
               self.lbl_icon.config(image=self.search_icon2)
               deg=u"\N{DEGREE SIGN}"
               self.lbl_temp.config(text=str(round(temp_c,2))+deg+"C | ")
               self.lbl_wind.config(text=wind)
               self.lbl_error.config(text="")
            else:
                  self.lbl_city.config(text="")
                  self.lbl_icon.config(image="")
                  self.lbl_temp.config(text="")
                  self.lbl_wind.config(text="")
                  self.lbl_error.config(text="Invalid City Name")               
root=Tk()
obj=MyWeather(root)
root.mainloop()        