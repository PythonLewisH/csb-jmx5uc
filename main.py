import tkinter
from tkinter import *
import math
from tkinter import messagebox
# ---------------------------- Variables ------------------------------- #

# Set constant variables for ease of use and reading later.
LIGHT_GREEN = "#B6FFCE"
FONT = "Apple Braille"

# Setting of empty cariables that will need to be adjested and tapped into later
total_salaries = []
total_attendees = []
attendee_no = 1
meeting_time = 0
final_time = 0
enable_counter = True
final_meeting_cost = 00.00

# ---------------------------- Functions ------------------------------- #


# Function for when start button is clicked. Changes title label, places the label, removes start button and adds in a
# spinbox.
def start_button_clicked():
    title_label.config(text="How many attendees in your meeting?")
    title_label.place(x=25, y=200)
    start_button.pack_forget()
    start_button.destroy()
    spinbox.place(x=220, y=240)
    next_button.place(x=275, y=239)


# Function when submit button is clicked. Adds 1 to global attendee no variable (keeps track of no attendees whose
# salary has been entered)
def submit_button_clicked():
    global attendee_no
    attendee_no += 1
    # Checks to make sure the user entered a valid number, if not shows error messagebox and clears box so they can try
    # again.
    if not salary_entry.get().isdigit():
        salary_entry.delete(first=0, last=END)
        messagebox.showerror("Error", "Please enter valid numbers only")
        return
    else:
        # Saves salary entered into a list of salaries
        salary = int(salary_entry.get())
        total_salaries.append(salary)
        # checks if there are any more attendees to enter their salary. If so, clears the entry box and asks them to
        # enter the salary of next attendee.
        if attendee_no <= (int(total_attendees[0])):
            title_label.config(text=f"What is the salary of person {attendee_no}?")
            salary_entry.delete(0, 'end')
        #     If it was the last attendee. Deletes everything on screen and shows a start meeting button.
        else:
            title_label.pack_forget()
            title_label.destroy()
            dollar_label.pack_forget()
            dollar_label.destroy()
            salary_entry.pack_forget()
            salary_entry.destroy()
            submit_button.pack_forget()
            submit_button.destroy()
            print(total_salaries)
            print(total_attendees)
            start_meeting_button.place(x=225, y=230)


# function for what happens when next button is clicked. Places a label asking for the salary of first attendee, updates
# global attendee_no variable to the value from the spinbox, deletes boxes from previous screens and places salary
# entry and submit buttons. Moves cursor into the salary entry box.
def next_button_clicked():
    global attendee_no
    title_label.config(text=f"What is the salary of person {attendee_no}?")
    title_label.place(x=80, y=200)
    total_attendees.append(spinbox.get())
    spinbox.pack_forget()
    spinbox.destroy()
    next_button.pack_forget()
    next_button.destroy()
    dollar_label.place(x=180, y=245)
    salary_entry.place(x=200, y=250)
    submit_button.place(x=305, y=250)
    salary_entry.focus()


# function for when start meeting button is clicked. Removes start meeting button, replaces with an end meeting button.
# Places the canvas which holds the meeting timer onto the screen. Starts the count_up function.
def start_meeting():
    start_meeting_button.pack_forget()
    start_meeting_button.destroy()
    end_meeting_button.place(x=215, y=380)
    canvas.place(x=140, y=20)
    count_up(0)


# function for when end_meeting button is clicked. Switches enable_counter to False - stopping the CountUp Function.
# Removes end meeting button, changes label to show the final cost of the meeting.
def end_meeting():
    global enable_counter
    global final_time
    global final_meeting_cost
    enable_counter = False
    end_meeting_button.pack_forget()
    end_meeting_button.destroy()
    final_meeting_cost_label.config(text=f"This meeting has cost ${final_meeting_cost:.2f}, I hope it was worth it.")
    final_meeting_cost_label.place(x=40, y=400)

# ---------------------------- Counter ------------------------------- #


# Function that counts up in seconds. It also works out the cost the meeting each second by taking into account the
# total salaries and dividing it by the working hours per year / hours / seconds.
def count_up(count):
    global final_time
    global enable_counter
    global final_meeting_cost
    # Checks if enable_counter still true and should still be counting (end_meeting has not been pressed). If false
    # stops counter.
    if not enable_counter:
        return
    # Else, the below works out how many seconds have passed and displated the current count in a minute:second format.
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"Time elapsed {count_min}:{count_sec}")
    # The below calculates cost per second and displays the current cost of meeting.
    cost_per_second = sum(total_salaries) / 1984 / 60 / 60
    final_meeting_cost = cost_per_second * count
    # Printing for easier debugging
    print(final_meeting_cost)
    money_canvas.place(x=150, y=80)
    money_canvas.itemconfig(money_count, text=f"${final_meeting_cost:.2f}")
    # logs the current count into global final time variable. waits 1 second then runs Count_up function again,
    # adding 1 to the starting count value argument.
    final_time = count
    window.after(1000, count_up, count + 1)

# ---------------------------- UI SETUP ------------------------------- #

# Configures size, title and bg of the GUI window
window = Tk()
window.title("Meeting Calculator")
window.minsize(width=500, height=500)
window.config(bg=LIGHT_GREEN)

# Below Create all the elements to be used in the GUI as we move through the functions.

#  Title
title_label = tkinter.Label(text="Meeting Calculator", font=(FONT, 24), bg=LIGHT_GREEN)
title_label.place(x=150, y=200)


# Start Button
start_button = tkinter.Button(text="Start", command=start_button_clicked, highlightthickness=0, borderwidth=0)
start_button.place(x=235, y=240)

# Spinbox
spinbox = Spinbox(from_=2, to=20, width=3, highlightthickness=0, borderwidth=0 )

# next button
next_button = tkinter.Button(text="Next", command=next_button_clicked, highlightthickness=0, borderwidth=0)

# Dollar Label
dollar_label = tkinter.Label(text="$", font=("Cambria", 18, "bold"), bg=LIGHT_GREEN)

# Salary entry
salary_entry = tkinter.Entry(width=10, highlightthickness=0, borderwidth=0)

# submit button
submit_button = tkinter.Button(text="Submit", command=submit_button_clicked, highlightthickness=0, borderwidth=0)

# start meeting button
start_meeting_button = tkinter.Button(text="Start Meeting", command=start_meeting)

# end meeting button
end_meeting_button = tkinter.Button(text="End Meeting", command=end_meeting)

# Meeting timer
canvas = Canvas(width=200, height=50, bg=LIGHT_GREEN, highlightthickness=0)
timer_text = canvas.create_text(120, 20, text="Time elapsed 00:00", fill="black", font=(FONT, 16))


# Running_meeting_cost
running_meeting_cost = tkinter.Label(text=f"Current meeting cost ${round(final_meeting_cost, 2)}", font=(FONT, 24), bg=LIGHT_GREEN)


# Final Meeting Cost
final_meeting_cost_label = tkinter.Label(font=(FONT, 16), bg=LIGHT_GREEN)

money_canvas = Canvas(width=220, height=300, bg=LIGHT_GREEN, highlightthickness=0)
money_img = PhotoImage(file="assets/bag.png")
money_canvas.create_image(110, 150, image=money_img)
money_count = money_canvas.create_text(105, 210, text=f"${round(final_meeting_cost, 2)}", fill="white", font=(FONT, 24))





window.mainloop()


# ---------------------------- Notes ------------------------------- #