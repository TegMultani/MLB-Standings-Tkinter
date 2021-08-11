import threading
from tkinter import *
import requests
import json
from getStats import getStandings, getSchedule


class Client:

    def __init__(self):
        data = getStandings()
        gui_thread = threading.Thread(target=self.standings_page, args=(data,))
        gui_thread.start()


    def standings_page(self, data):
        self.win = Tk()
        self.win.configure(bg='lightgray')
        self.win.title("MLB Standings")
        self.win.iconbitmap("baseball-bat.ico")
        self.toplabel = Label(self.win, text="Standings", bg='lightgray', font=("Century Schoolbook", 18, "bold"))
        self.toplabel.grid(row=0, column=6)

        self.win.grid_columnconfigure(0, minsize=30)
        self.win.grid_columnconfigure(6, minsize=100)
        self.win.grid_columnconfigure(12, minsize=30)

        def show_schedule(self):
            self.schedule = Tk()
            self.schedule.configure(bg='lightgray')
            self.schedule.title("Blue Jays Schedule")   
            self.schedule.iconbitmap("baseball-bat.ico")
            
            data2 = getSchedule('08', '141', '2021')
            
            height = 5
            width = 7
            for i in range(height):
                for j in range(width):
                    b = Text(self.schedule, text="", font=("Segoe UI", 12), cursor='arrow', height=6, width=6)
                    b.insert(0, 'HEY')
                    b.config(state=DISABLED)
                    b.grid(row=i+1, column=j+1)
            

            self.schedule.mainloop()

        def insert_division(id, data, rowconfigure, addToRows, addToColumns, labelrow, labelcolumn, division):
            self.league_label = Label(self.win, text=division, bg='lightgray')
            self.league_label.config(font=("Segoe UI", 12, "bold"))
            self.league_label.grid(row=labelrow, column=labelcolumn)

            height = 6
            width = 5
            for i in range(height): #Rows
                for j in range(width): #Columns
                    if j == 0:
                        b = Entry(self.win, text="", font=("Segoe UI", 12), cursor='arrow', justify=CENTER, disabledbackground='gray1', disabledforeground='ghost white', state=DISABLED, width=3)
                        b.grid(row=i+addToRows, column=j+addToColumns)
                        if i == 0:
                            b.config(state=NORMAL, font=("Segoe UI", 12, "bold"))
                            b.config(text="")
                            b.insert(0, '#')
                            b.config(state=DISABLED)
                        if i == 1:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, '1')
                            b.config(state=DISABLED)
                        if i == 2:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, '2')
                            b.config(state=DISABLED)
                        if i == 3:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, '3')
                            b.config(state=DISABLED)
                        if i == 4:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, '4')
                            b.config(state=DISABLED)
                        if i == 5:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, '5')
                            b.config(state=DISABLED)                  
                    elif j == 1:
                        b = Entry(self.win, text="", font=("Segoe UI", 12), cursor='arrow', justify=CENTER, disabledbackground='ghost white', disabledforeground='gray1', state=DISABLED, width=20)
                        b.grid(row=i+addToRows, column=j+addToColumns)
                        if i == 0:
                            b.config(state=NORMAL, font=("Segoe UI", 12, "bold"))
                            b.config(text="")
                            b.insert(0, 'Team')
                            b.config(state=DISABLED)
                        if i == 1:
                            b.config(state=NORMAL, cursor='hand2')
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['name'])
                            b.config(state=DISABLED)
                        if i == 2:
                            b.config(state=NORMAL, cursor='hand2')
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['name'])
                            b.config(state=DISABLED)
                        if i == 3:
                            b.config(state=NORMAL, cursor='hand2')
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['name'])
                            b.config(state=DISABLED)
                        if i == 4:
                            b.config(state=NORMAL, cursor='hand2')
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['name'])
                            b.config(state=DISABLED)
                        if i == 5:
                            b.config(state=NORMAL, cursor='hand2')
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['name'])
                            b.config(state=DISABLED)
                    elif j == 2:
                        b = Entry(self.win, text="", font=("Segoe UI", 12), cursor='arrow', justify=CENTER, disabledbackground='ghost white', disabledforeground='gray1', state=DISABLED, width=6)
                        b.grid(row=i+addToRows, column=j+addToColumns)
                        if i == 0:
                            b.config(state=NORMAL, font=("Segoe UI", 12, "bold"))
                            b.config(text="")
                            b.insert(0, 'Record')
                            b.config(state=DISABLED)
                        elif i == 1:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['recordOverall'])
                            b.config(state=DISABLED)
                        elif i == 2:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['recordOverall'])
                            b.config(state=DISABLED)
                        elif i == 3:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['recordOverall'])
                            b.config(state=DISABLED)
                        elif i == 4:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['recordOverall'])
                            b.config(state=DISABLED)
                        elif i == 5:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['competitor']['recordOverall'])
                            b.config(state=DISABLED)
                    elif j == 3:
                        b = Entry(self.win, text="", font=("Segou UI", 12), cursor='arrow', justify=CENTER, disabledbackground='ghost white', disabledforeground='gray1', state=DISABLED, width=5)
                        b.grid(row=i+addToRows, column=j+addToColumns)
                        if i == 0:
                            b.config(state=NORMAL, font=("Segoe UI", 12, "bold"))
                            b.config(text="")
                            b.insert(0, 'GB')
                            b.config(state=DISABLED)
                        if i == 1:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['gamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)
                        if i == 2:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['gamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)
                        if i == 3:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['gamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)
                        if i == 4:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['gamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)
                        if i == 5:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['gamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)                    
                    elif j == 4:
                        b = Entry(self.win, text="", font=("Segou UI", 12), cursor='arrow', justify=CENTER, disabledbackground='ghost white', disabledforeground='gray1', state=DISABLED, width=6)
                        b.grid(row=i+addToRows, column=j+addToColumns)
                        if i == 0:
                            b.config(state=NORMAL, font=("Segoe UI", 12, "bold"))
                            b.config(text="")
                            b.insert(0, 'WCGB')
                            b.config(state=DISABLED)
                        if i == 1:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['wcGamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')                        
                            b.config(state=DISABLED)
                        if i == 2:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['wcGamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            if '-' in b.get():
                                # if b.get() == '-':
                                #     pass
                                # else:
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)
                        if i == 3:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['wcGamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            if '-' in b.get():
                                # if b.get() == '-':
                                #     pass
                                # else:
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)
                        if i == 4:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['wcGamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)
                        if i == 5:
                            b.config(state=NORMAL)
                            b.config(text="")
                            b.insert(0, data[id]['competitorStats'][i-1]['stats']['wcGamesBack'])
                            if b.get() == '0':
                                b.delete(0, 'end')
                                b.insert(0, '-')
                            b.config(state=DISABLED)

            self.win.grid_rowconfigure(rowconfigure, minsize=30)

        insert_division(0, data, 9, 2, 1, 1, 2, 'AL East')
        insert_division(1, data, 17, 11, 1, 10, 2, 'AL Central')
        insert_division(2, data, 25, 19, 1, 18, 2, 'AL West')
        insert_division(3, data, 9, 2, 7, 1, 8, 'NL East')
        insert_division(4, data, 17, 11, 7, 10, 8, 'NL Central')
        insert_division(5, data, 25, 19, 7, 18, 8, 'NL West')



        self.win.mainloop()

    
    




client = Client()

