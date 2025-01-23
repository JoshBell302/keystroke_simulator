# Keystroke Simulator Bot

This is a very simple bot where you can easily write a script of keystrokes and run them in the same program.

## How to Run the Program
Once you download the repository, go into where you have downloaded it and run the "*keystroke_simulator.py*" file and a terminal should appear running the program.

Once you start this pytrhon program the program will ask you to if you would either write a script or if you wanna run a script so lets discuss each of them.

## Writing a Script

If you would like to write a script type in "m" and enter that input. Then it will ask you what you would like to call the script, the script name may change depending on if there is an invalid character and it will update the name for you. Once you have the name it will give a short countdown and then will start reading your inputs.
> Depending on the use of the bot, make sure to input slower than normal so that the bot properly recognizes the inputs!

When you are done with your script press the "End" key and the program will stop and you can check your script found in the same common working directory.

The program writes the keystroke alongside the time it was selected, these combine to create the script this program runs on. 

## Running a Script

If you would like to write a script type in "r" and the enter that input. The program will then list the scripts that are available (found in the same common working directory). Once you input the corresponding value to the script, the program will gather the script from that csv file. After the data is collected it will give you a countdown and then will start on its own. 
While running there are a few inputs you can press to change or view information...

- "**Q**": This will set the script to end after the next full cycle, you can press this again to remove the quit and the script will continue as normal.
- "**P**": This will set the script to pause after the next full cycle, you can press this again to remove the pause and the script will continue as normal. While paused the program will send a Pause mesage and wait for you to unpause the script. Once you do, the program will give you another countdown and it will continue. 
- "**I**": This will show in the program terminal if the script is set to quit, pause, and how many cycles there have been.
> If you need to end the program immediately, click in the terminal and hit "*Ctrl+C*" to end the run.
