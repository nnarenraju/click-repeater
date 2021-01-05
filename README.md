# simon-says

Dependancies
------------
Simon is a mouse click simulation and repetition package. Mandatory dependancies 
have been stated below:

 1. It can only be used alongside a Windows operating system
    Currently no support has been provided for any alternate OS. 
    
 2. The code can only be run on a python3+ environment.
 
 3. Packages within are dependant on being run from the command line. Any other 
    external environement will lead to NULL results.


Usage
-----
Assuming the above conditions have been met:
 
 1. Open command-prompt and 'cd' to package directory
 2. Run the code using 'python simon.py'

End-user interface:

 1. "Set a quit flag..."   - Enter a key on your keyboard that will be used to start/stop message recording
                             DO NOT set the key as either 'Alt' or 'Tab'. Alphanumeric characters are prefered.
 
 2. "Key captured."        - Indicates that the above key has been captured.
 
 3. "Waiting for flag..."  - Code waits for user to click on 'flag' to start the recording.
 
 4. "Key confirmed."       - Indication that flag key has been entered by user.
 			      Nothing happens when other keys/mouse-clicks are performed at this point.
 
 5. "Recording started..." - Indication that any mouse click from this point will be recorded.
 			      Moving the mouse does not affect the result. ONLY left mouse clicks are recorded.
 
 6. "Left Button {action}" - Indicates whether left mouse button is clicked or released.
 
 7. Before clicking on the flag again to stop the recording, use Alt+Tab to move to the 'cmd' screen. Any clicks
    used to move to the 'cmd' screen will be recorded otherwise. As 'Alt' and 'Tab' keys are not set as flag keys,
    they do not affect the recording in any way. 
    Click on flag key again to stop the recording. Displays "Message has been recorded!" once flag is detected.
 
 8. Message is then replayed after a 5 second interval. Do not move your mouse at this time for optimum results.
 
 9. "Interval between click index {a} and {b}" - Input the interval in seconds between adjacent clicks.
     						   Starts at interval between click 0 and click 1.
 
 10. "Enter interval (in seconds):"		 - Enter the integer interval in seconds. Floats not supported.
 
 11. Enter the interval between repetitions. This is the interval between click 'n' and click '0'. 
 
 12. "Start repeat mode (y or n)?" - Enter 'y' or 'Y' to start the repeat mode.
 
 13. Number of repeats can be any integer (set as -1 to repeat indefinitely). Indefinite is defined as 999999.
 
 14. Once the number of repeats are entered, repeat mode starts in 30 seconds.
 
 15. If successfully completed, you should see "Cycles completed!" and "End" on command line.
 
 
Ideal Output (comments added for clarity within {})
-----------------------------------------

C:\Users\Admin\Desktop\Other Work>python simon.py
Set a quit flag...     {Enter 'q' on keyboard}
Key captured.
Waiting for flag...    {Enter 'q' again to start recording}
Key confirmed.
Recording started...   {Use Alt+Tab to go to required screen. DO NOT use mouse click.}
Left Button Pressed	{First Registered click}
Left Button Released
Left Button Pressed    {Second Registered Click}
Left Button Released
Left Button Pressed    {Third Registered Click}
Left Button Released
Left Button Pressed    {Fourth Registered Click}
Left Button Released
Message has been recorded!
Replaying message in 5 seconds...  {Do not move mouse. Message will replay automatically.}
Recording successful!

Interval between click index 0 and 1  {Interval between click 1 and click 2}
Enter interval (in seconds):    2

Interval between click index 1 and 2  {Interval between click 2 and click 3}
Enter interval (in seconds):    5

Interval between click index 2 and 3  {Interval between click 3 and click 4}
Enter interval (in seconds):    1

Enter interval between repetitions (in seconds):        6    {Interval between click 4 and click 1}

Start repeat mode (y or n)?     y
Number of repeats can be any integer (set as -1 to repeat indefinitely)   {Indefinite is 999999 times}
Enter the number of repeats: 2

Repeat mode starts in 30 seconds...
Repeat mode starting
Cycles completed!
End


