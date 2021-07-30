from tkinter import*


app =Tk()
app.title("Weather_App")
app.geometry('700x350')

city_test = StringVar()
city_entry = Entry(app, textvariable=city_test)
city_entry.pack()





app.mainloop()

