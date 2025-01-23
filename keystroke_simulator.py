# Importing necessary libraries
from pynput.keyboard import Key, Controller
from pynput import keyboard

from lambda_keys import lambda_key_inputs

import time
import random
import csv
import os
import glob

# Special cases and helpful functions -------------------------------------------------------------
countdown = 3
line = "----------------------------------------------------"

def start_bot_delay():
    print(f"{line}\n| Starting in...")

    # Create a count down for the bot to start and continue
    for i in range(countdown):
        print(f"| {countdown-i}")
        time.sleep(1)
    print("| START\n")
 
def reload_page():
    # Alert the terminal for the reload and begin reload
    print("| RELOADING ----------------------------------------")
    keyboard_controller.press(Key.ctrl_l)
    keyboard_controller.press('r')
    keyboard_controller.release(Key.ctrl_l)
    keyboard_controller.release('r')

def print_info():
    global paused
    global stop_script
    global times_ran
    print("--------------------")
    print(f"| (p) | Pause: {paused}")
    print(f"| (q) | Quit: {stop_script}")
    print(f"| Times Ran: {times_ran}")
    print("--------------------")


# Preparing Bot Functions -------------------------------------------------------------------------
script_to_make = None

def write_to_script(key):
    # Append to the csv file
    with open(script_to_make, "a", newline="") as file:
        writer = csv.writer(file)
        fixed_key = str(key).replace("'", "")
        writer.writerow([fixed_key, time.time()])
    print(f"| {fixed_key}\t\t\t{time.time()}")

def get_script_name():
    # Have a string of invalid chars
    invalid_file_chars = '<>:"/\|?*' + "'"
    print(line)

    # Gather the script name from the user
    user_name = input("What would you like to name this script: ")

    # Check to see if the name has invalid chars
    user_name = user_name.replace(" ", "_")
    if any(char in user_name for char in list(invalid_file_chars)):
        # Remove the invalid chars and notify user of new name
        name_table = str.maketrans(user_name, user_name, invalid_file_chars)
        new_name = user_name.translate(name_table)
        print(f"Invalid characters found. Updated script name to: '{new_name}'")
        return new_name
    else:
        print(f"Script to be made called: '{user_name}'")
        return user_name

def user_input():
    # Figure out what the user wants to do, and loop until there is a valid input
    assignment = False
    while assignment == False:
        assignment, choice = decision()
    return choice

def decision():
    # Ask whether the user wants to make a script or run a script
    print( "---------------KEYSTROKE SIMULATOR BOT--------------")
    print(f"| Would you like to...\n| Make a script (Enter: 'm')\n| Run a script (Enter: 'r')\n|")
    choice = input("| What would you like to do: ")

    # Figure out if this is a valid input
    if choice == "m" or choice == "r":
        print(f"{line}\n")
        return True, choice
    print("| Invalid input, please try again (Wait for reload)")
    time.sleep(2)
    os.system("cls")
    return False, None

def choose_script():
    # Get the path of the project and all csv files in the working directory
    cwd = os.getcwd()
    csv_files = glob.glob(cwd + "/*.csv")
    
    # List all csv files
    if len(csv_files) == False:
        raise SystemExit(f"{line}\nNo scripts found, please make a script and try again!")

    # List the scripts and have the user select which to run
    while True:
        print(f"{line}\n| Which of the following scripts would you like to run?")
        for i in range(len(csv_files)):
            print(f"| {os.path.basename(csv_files[i])} (Enter: '{i}')")
        
        # Validate the user input
        try:
            valid_input = True
            script_input = int(input(f"| Which would you like to run: "))
        except ValueError:
            valid_input = False
            print("| Invalid Input, please try again")

        # Check if valid int is within the range
        if valid_input:
            if script_input in range(len(csv_files)):
                # Within range, return script to run
                print(f"|\n| You have selected '{os.path.basename(csv_files[script_input])}'\n{line}")
                return os.path.basename(csv_files[script_input])
            else:
                # Out of range, alert user and end bot
                print(f"| Integer not within range, please try again!\n")


# Keyboard listner functions ----------------------------------------------------------------------
keyboard_controller = Controller()
reload_key = keyboard.Key.home
end_script_key = keyboard.Key.end
quit_script_key = keyboard.KeyCode(char='q')
info_script_key = keyboard.KeyCode(char='i')
pause_script_key = keyboard.KeyCode(char='p')

writing_script = False
paused = False
stop_script = False
times_ran = 0

def on_press(key):
    global writing_script
    global stop_script
    global paused

    # Change hotkeys depending on script writing or running
    if writing_script:

        # Unless the end key is pressed write it to the script
        if key == end_script_key:
            writing_script = False
        else:
            write_to_script(key)

    else:
        # If a special key was pressed using hotkey reload
        if key == reload_key:
            reload_page()
    
        if key == quit_script_key:
            if stop_script:
                print("| STOPPING THE QUIT AND CONTINUING------------------")
                paused = False # Update paused variable to not quit
            else:
                print("| STOPPING SCRIPT AFTER NEXT COMPLETE SCRIPT RUN ---")
                paused = True # Update paused variable to quit
            stop_script = not stop_script

        if key == pause_script_key:
            if paused: 
                print("| UN-PAUSING----------------------------------------")
            else:
                print("| PAUSING AFTER NEXT COMPLETE SCRIPT RUN -----------")
            paused = not paused

        if key == info_script_key:
            print_info()

def on_release(key):
    pass


# Running script function -------------------------------------------------------------------------
def gather_script(file_name):
    # Print the start of gathering the script from the csv file
    print(f"\n{line}\n| Gathering Script...")
    inputs = []
    times = []

    # Open the file and append data to the proper lists and return once the csv file has been gone through
    with open(file_name, mode='r') as file:
        csv_file = csv.reader(file)
        for input, time in csv_file:
            inputs.append(input)
            times.append(time)
    print(f"| Script is Gathered\n{line}\n")
    return inputs, times

def run_input(input):
    # Print the input being ran
    print(f"| Running input: {input}")

    # Press and release the input
    if len(input) in range(2):
        keyboard_controller.press(input)
        keyboard_controller.release(input)
    else:
        run_inputs = lambda_key_inputs.get(input)
        run_inputs()


    # # Gather the lambda function from the dict and the run command
    # inputs_to_run = list_of_valid_inputs.get(input)
    # inputs_to_run()

    if input == "Key.home":
        # Add an extra delay to not interupt input depending on reload time
        print("| RELOAD PAUSE -------------------------------------")
        time.sleep(10)
        print("| RELOAD CONTINUE ----------------------------------")
    

def run_voucher_script(input_script, time_script):
    print("-------------------STARTING SCRIPT------------------")
    for i in range(len(input_script)):
        # Run the input from the input_script
        run_input(input_script[i])

        # Add a delay based on the time_script current and nex input
        if i == (len(input_script)-1):
            time.sleep(1) # Default sleep time if the value of the next time_script is None
        else:
            delay = float(time_script[i+1])-float(time_script[i])
            random_delay = random.random() # Added to prevent being found as a bot (Not sure if needed)
            time.sleep(delay+random_delay)
    
    # Add an extra delay to not interupt input depending on reload time
    time.sleep(10)
    print("---------------------SCRIPT DONE--------------------")


# Main function -----------------------------------------------------------------------------------
if __name__=="__main__":

    # Ask whether the user wants to make a script or run a script:
    os.system("cls")
    choice = user_input()

    if choice == "m":
        # Make script name
        writing_script = True
        script_to_make = get_script_name()

        # Give user warning to prepare for script writing
        script_to_make = script_to_make + ".csv"
        f = open(script_to_make, "x")
        f.close()
        start_bot_delay()

        # Write script
        keyboard_listner = keyboard.Listener(on_press=on_press, on_release=on_release)
        keyboard_listner.start()
        print(line)

        while writing_script:
            time.sleep(0.1)
            pass

        keyboard_listner.stop()

    else:
        # Run script and figure out which script to run
        script_name = choose_script()

        # Gather script of keystrokes
        inputs, times = gather_script(script_name)

        # Give the bot a boot up time to have user time to prepare
        start_bot_delay()

        # Begin listening to inputs
        keyboard_listner = keyboard.Listener(on_press=on_press, on_release=on_release)
        keyboard_listner.start()

        # Loop while both "stop_script" and "paused" are False
        while not stop_script:
            # While not paused continue as normal
            while not paused:
                run_voucher_script(inputs, times)
                times_ran += 1
            # While paused loop a paused statement and when its unpaused run the start_bot_delay function 
            while paused and not stop_script:
                print("PAUSED")
                time.sleep(5)
                if not paused:
                    start_bot_delay()
    
        # Stop script
        keyboard_listner.stop()
        print(f"SCRIPT STOPPED\nTimes Ran: {times_ran}")