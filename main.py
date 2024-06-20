# --------------------------------
# MAIN SCRIPT
# --------------------------------

# Import required modules
import pandas as pd # Dataframes
from random import randint # Random number generator
from flask import Flask, render_template # Web UI
import tkinter as tk # Local GUI, no browser

# Read the .csv file containing the words
df_words = pd.read_csv("core_files/german_words.csv")

# Note: To replace correct times: 
# df_words.iloc[index, 2 or 3 (depending on g2e or e2g respectively)] = [your int]

# GUI

def local_gui():
    global option
    option = 2

    win = tk.Tk()

    window_height = 100
    window_width = 300
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    tk.Label(text="German Words Practice").pack()

    def e2g_option():
        global option
        option = 1
        win.destroy()
    tk.Button(text="English to German",command=e2g_option).pack()

    def g2e_option():
        global option
        option = 0
        win.destroy()
    tk.Button(text="German to English",command=g2e_option).pack()
    
    win.mainloop()

    if option != 2:
        global index
        index = randint(0,len(df_words))
        global backup_option

        win = tk.Tk()
        
        window_height = 100
        window_width = 300
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        def random_index():
            global index
            global option
            while True:
                index = randint(0,len(df_words))
                if randint(0,df_words.iloc[index,option+2]) == 1 or df_words.iloc[index,option+2]<0:
                    break


        l1 = tk.Label(text=df_words.iloc[index,option])
        l1.pack()

        backup_option = option
        def showdef():
            global option
            if option == 0:
                l1.config(text=df_words.iloc[index,0])
                option = 1
            elif option == 1:
                l1.config(text=df_words.iloc[index,1])
                option = 0
        tk.Button(text="Show Definition", command=showdef).pack()

        def correct():
            global index
            global backup_option
            global option
            df_words.iloc[index,backup_option+2] += 1
            index = randint(0,len(df_words)-1)
            option = backup_option
            showdef()
        tk.Button(text="Correct",command=correct).pack()

        def wrong():
            global index
            global backup_option
            global option
            df_words.iloc[index,backup_option+2] -= 1
            index = randint(0,len(df_words)-1)
            option = backup_option
            showdef()
        tk.Button(text="Wrong",command=wrong).pack()

        win.mainloop()
        
        df_words.to_csv("core_files/german_words.csv", index=0)
local_gui()