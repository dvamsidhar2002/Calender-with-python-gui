#Importing tkinter module
from tkinter import *
#importing calender module
import calendar

def showCalendar():
    gui = Tk()
    gui.config(background = 'black')
    gui.title("Calender of the year")
    gui.geometry("1000x1000")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()






# Driver Code
if __name__ == '__main__':
    new = Tk()
    new.config(background='black')
    new.title('CALENDER')
    new.geometry("300x300")
    cal = Label(new, text="Calender", bg="grey",font=("times",28,"bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calender', fg='Black', bg='grey', command = showCalendar)
    Exit = Button(new, text='Exit', fg='Black', bg='grey', command = exit)

    cal.grid(row=1, column=1)
    year.grid(row=3, column=1)
    year_field.grid(row=5, column=1)
    button.grid(row=7, column=1)
    Exit.grid(row=9, column=1)
    new.mainloop()

