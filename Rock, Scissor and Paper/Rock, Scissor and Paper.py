from tkinter import *
import random
from tkinter import messagebox

score_computer = 0
score_user = 0
message = ""
computer_choice_option = ["rock", "paper", "scissor"]


def score_reset():
    global score_user, score_computer
    score_computer = 0
    score_user = 0
    label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


def rock():
    global score_user, score_computer, message, computer_choice_option, random_number
    user_choice = "rock"
    random_number = random.randrange(0, 3)
    computer_choice = computer_choice_option[random_number]
    label_user.config(image=image_background)

    label_user_choice.config(image=image_rock)

    if user_choice and (computer_choice == "scissor"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_scissor)
        score_user += 1
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


    elif user_choice and (computer_choice == "rock"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_rock)
        score_user += 0
        score_computer += 0
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")

    elif user_choice and (computer_choice == "paper"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_paper)
        score_computer += 1
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


    else:
        message += "not the option"
        messagebox.showerror("Error", message)


def scissor():
    global score_user, score_computer, message, computer_choice_option, random_number
    user_choice = "scissor"
    random_number = random.randrange(0, 3)
    computer_choice = computer_choice_option[random_number]
    label_user.config(image=image_background)
    label_user_choice.config(image=image_scissor)

    if user_choice and (computer_choice == "paper"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_paper)
        score_user += 1
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


    elif user_choice and (computer_choice == "scissor"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_scissor)
        score_user += 0
        score_computer += 0
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


    elif user_choice and (computer_choice == "rock"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_rock)
        score_computer += 1
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


    else:
        message += "not the option"
        messagebox.showerror("Error", message)


def paper():
    global score_user, score_computer, message, computer_choice_option, random_number
    user_choice = "paper"
    random_number = random.randrange(0, 3)
    computer_choice = computer_choice_option[random_number]
    label_user.config(image=image_background)
    label_user_choice.config(image=image_paper)

    if user_choice and (computer_choice == "rock"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_rock)
        score_user += 1
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


    elif user_choice and (computer_choice == "paper"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_paper)
        score_user += 0
        score_computer += 0
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


    elif user_choice and (computer_choice == "scissor"):
        label_computer.config(image=image_background)
        label_computer_choice.config(image=image_scissor)
        score_computer += 1
        label_score_user_and_computer.config(text=f"{score_user} : {score_computer}")


    else:
        message += "not the option"
        messagebox.showerror("Error", message)


master = Tk()

master.config(background="white")

Canvas(master,
       width=700,
       height=500).pack()

master.resizable(width=False, height=False)

# Frame Up ---------------------------------------------------------------------------------------------------
frame_up = Frame(master,
                 background="white")
frame_up.place(x=0, y=0, relwidth=1, relheight=0.2)

image_reseet = PhotoImage(file="icon\\reset score.png")

btn_refresh_score = Button(frame_up,
                           background="white",
                           text="refresh score",
                           activebackground="white",
                           border=0,
                           image=image_reseet,
                           command=score_reset)

btn_refresh_score.place(anchor="nw", x=460, y=10)

label_text_user = Label(frame_up,
                        text="User ",
                        background="white",
                        foreground="black",
                        font=(("Garamond"), 20, ("bold"), ("italic")))

label_text_user.place(x=10, y=30, anchor="nw")

label_text_computer = Label(frame_up,
                            text="Computer ",
                            background="white",
                            foreground="black",
                            font=(("Garamond"), 20, ("bold"), ("italic")))

label_text_computer.place(x=300, y=30, anchor="nw")

label_score_user_and_computer = Label(frame_up,
                                      text=f"{score_user} : {score_computer}",
                                      background="white",
                                      foreground="black",
                                      font=(("Garamond"), 20, ("bold")))

label_score_user_and_computer.place(x=160, y=30, anchor="nw")

# Frame Balance ---------------------------------------------------------------------------------------------------
frame_balance = Frame(master,
                      background="white")
frame_balance.place(x=0, y=100, relwidth=1, relheight=0.5)

image_rock = PhotoImage(file="icon\\rock.png")
image_paper = PhotoImage(file="icon\\paper.png")
image_scissor = PhotoImage(file="icon\\scissor.png")
image_background = PhotoImage(file="icon\\background show.png")

label_user = Label(frame_balance,
                   image=image_background,background="white")

label_user.place(x=30, y=20, anchor="nw")

label_user_choice = Label(frame_balance,
                          image=image_scissor,
                          background="grey")
label_user_choice.place(x=60, y=60, anchor="nw")

label = Label(frame_balance,
              background="white",
              text=" : ",
              font=("Arial", 70, "bold"))

label.place(x=300, y=50, anchor="nw")

label_computer = Label(frame_balance,
                       image=image_background,background="white")

label_computer.place(x=460, y=20, anchor="nw")


label_computer_choice = Label(frame_balance,
                              image=image_rock,
                              background="grey")
label_computer_choice.place(x=490, y=60, anchor="nw")

# Frame Down ---------------------------------------------------------------------------------------------------
frame_down = Frame(master,
                   background="white")
frame_down.place(x=0, y=350, relwidth=1, relheight=0.3)

# Button Rock
image_btn_rock = PhotoImage(file="icon\\rock btn.png")
btn_rock = Button(frame_down,
                  image=image_btn_rock,
                  border=0,
                  background="white",
                  activebackground="white",
                  command=rock
                  )
btn_rock.place(x=20, y=25,anchor="nw")

# Button Paper
image_btn_paper = PhotoImage(file="icon\\paper btn.png")
btn_paper = Button(frame_down,
                   image=image_btn_paper,
                   border=0,
                   background="white",
                   activebackground="white",
                   command=paper)

btn_paper.place(x=250, y=25,anchor="nw")

# Button Scissor
image_btn_scissor = PhotoImage(file="icon\\scissor btn.png")
btn_scissor = Button(frame_down,
                     image=image_btn_scissor,
                     border=0,
                     background="white",
                     activebackground="white",
                     command=scissor)
btn_scissor.place(x=480, y=25,anchor="nw")

master.mainloop()
