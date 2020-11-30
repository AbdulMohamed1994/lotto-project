from tkinter import *
from random import sample
import random
from tkinter import messagebox
from datetime import *

lottery = Tk()
lottery.title("Lottery Application")
lottery.geometry("280x100")
lottery.config(bg="yellow")

age_lbl= Label(lottery, text='Please enter your age:')
age_lbl.place(x=30, y=0)

age_entry = Entry(lottery, width=20)
age_entry.place(x=30, y=30)

#defining the age
def play():
    try:
        if int(age_entry.get()) < 18:
            messagebox.showinfo("You are too Young", "You need to be over 18 to play this game")
    except ValueError:
            messagebox.showinfo("Numbers Only!!", "Please enter a number")

    if int(age_entry.get()) >= 18:
        lottery.destroy()

        def choose():
            nums = random.sample(range(1, 49), 6)
            winning_nums = [nums[0],nums[1],nums[2],nums[3],nums[4],nums[5]]
            print(winning_nums)
            message = Label(root ,text="Todays winning numbers are")
            message.grid(row=6, column=1)

            disp_win_label['text'] = winning_nums
            disp_win_label.grid(row=6, column=9)
            getBtn.configure(state=NORMAL)



        root = Tk()
        root.title("lottery")
        root.geometry("700x700")
        root.config(bg="yellow")


        now = datetime.now()
        date = now.strftime("%d %B %Y")
        current_time = now.strftime("%H:%M %p")
        text = date+"\n"+current_time
        print(text)

        ent_lbl = Label(root,text='Enter your lucky numbers: ')
        ent_lbl.grid(row=1, column=1)
        disp_win_label = Label(root)
        disp_win_label.grid(row=3,column=1)
        lbl1 = Entry(root, relief='groove', width=2)

        lbl2 = Entry(root,  width=2)
        lbl3 = Entry(root, width=2)
        lbl4 = Entry(root, width=2)
        lbl5 = Entry(root, width=2)
        lbl6 = Entry(root, width=2)
        getBtn = Button(root, command=choose)
        time_label = Label(root, text = text)

        reset = Button(root)

        #geometry
        time_label.grid(row=10, column=1)
        time_label.grid(row=10, column=1)
        lbl1.grid(row=1, column=2, padx=10)
        lbl2.grid(row=1, column=3, padx=10)
        lbl3.grid(row=1, column=4, padx=10)
        lbl4.grid(row=1, column=5, padx=10)
        lbl5.grid(row=1, column=6, padx=10)
        lbl6.grid(row=1, column=7, padx=10)
        getBtn.grid(row=2, column=6, columnspan=2)

        #static
        root.title('lotto generator')
        root.geometry('650x200')
        getBtn.configure(text='Im feeling lucky')
        getBtn.grid (column=0, row=4)
        reset.configure(text='reset', command=quit)

        # buttons
        # close button function
        def close():
            quit(root)

        # close button
        closeb = Button(root)
        closeb.configure(text="Close", fg='black', bg='red')
        closeb.grid(row=9, column=3, columnspan=6, pady=7)
        closeb.configure(command=close)

        # defining the reset function
        def die():
            print("die")
            lbl1.delete(0, 'end')
            lbl2.delete(0, 'end')
            lbl3.delete(0, 'end')
            lbl4.delete(0, 'end')
            lbl5.delete(0, 'end')
            lbl6.delete(0, 'end')
            disp_win_label['text'] = ""

        # Reset
        reset = Button(root, width=10, text="Reset", command=die)
        reset.configure(fg='black', bg='green')
        reset.grid(row=9, column=1, padx=5, pady=7)

        f = open("results.txt", "a+")
        text= "Date: "+date+"\ntime: "+current_time+"Win nums: "
        f.write(text)
        f.close()


        from random import sample


        root.mainloop()



playbtn = Button(lottery, text = 'Play', command = play)
playbtn.place(x=30, y=60)

lottery.mainloop()
