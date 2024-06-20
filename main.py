# --------------------------------
# MAIN SCRIPT
# --------------------------------

# Import required modules
import pandas as pd # Dataframes
from random import randint # Random number generator
import tkinter as tk # Local GUI, no browser

# Read the .csv file containing the words
df_words = pd.read_csv("core_files/german_words.csv")

# Note: To replace correct times: 
# df_words.iloc[index, 2 or 3 (depending on g2e or e2g respectively)] = [your int]

# GUI

def local_gui():


    ### Starting window - choose English to German or vice versa
    global option
    option = 2

    win = tk.Tk()


    # Center window
    window_height = 100
    window_width = 300
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


    # Label for title
    tk.Label(text="German Words Practice").pack()


    # Button for English to German option
    def e2g_option():
        global option
        option = 1
        win.destroy()
    tk.Button(text="English to German",command=e2g_option).pack()


    # Button for German to English option
    def g2e_option():
        global option
        option = 0
        win.destroy()
    tk.Button(text="German to English",command=g2e_option).pack()
    
    win.mainloop()


    # If user hasn't closed the window before pressing a button...
    if option != 2:
        global index
        index = randint(0,len(df_words))
        global backup_option


        ### Actual flashcard testing window
        win = tk.Tk()
        

        # Center window
        window_height = 100
        window_width = 300
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


        # Depending on user score (call it "n") on option chosen, a word has a 1/n chance of being picked.
        def random_index():
            global index
            global option

            while True:
                index = randint(0,len(df_words))
                if randint(0,df_words.iloc[index,option+2]) == 1 or df_words.iloc[index,option+2]<0:
                    break


        # Label showing word.
        l1 = tk.Label(text=df_words.iloc[index,option])
        l1.pack()


        # Button that switches word for its translation
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


        # Button pressed if user gets word correct
        def correct():
            global index
            global backup_option
            global option

            df_words.iloc[index,backup_option+2] += 1
            index = randint(0,len(df_words)-1)
            option = backup_option
            showdef()
        tk.Button(text="Correct",command=correct).pack()


        # Button pressed if user gets word wrong
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
        

        # Writes scores on each word in file
        df_words.to_csv("core_files/german_words.csv", index=0)


# Uncomment to test local Tkiner GUI
#local_gui()

#------------------------

# Flask app in /app/app.py