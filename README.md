# pyfiles

The main directory for files using the WebCam is the Python folder
The numbered files named openCV use a webcam in some form.
There are other folders in the Python Folder that contain images for use in some of the openCV files

There is also included a certificates folder that contains certs to prove work done on tutorials either on AWS or with Python

There are also 2 folders with other python work:
pythonBasics folder contains some files that are just some basics of using python
vPython are python based animations using different shapes and techniques
In the IDE you will need to switch from the Python Folder to the vPython/pythonBasics folders to run these files

IMPORTANT: there are also python environments setup as we may need to switch between different versions of python when running the openCV files or the vPython files
To change the virtual environment, open powershell - run as administrator
navigate to where the Python Directory is saved (eg. cd C:\Users\Niall\Python) 
enter the line: pyAI3.6/Scripts/activate hit enter
if we need to open the other environments available use pyAI3.11/Scripts/activate or pyAI3.9/Scripts/activate (use 3.9 for the vPython folder)


openCV file descriptions
press the Q keyboard key to exit any video windows that are run

openCV1.py - opens 4 camera frames each with different image colour gradings (eg. grayscale)

openCV3.py - resizes the camera frame that appears on the window and opens muplie frames filling the comouter screen

openCV4.py - in ther terminal enter how many rows and columns you want and this will display that number of webcam windows on the screen

openCV5.py - we manipulate the colouring on in the webcam frame creating a checkerboard effect

openCV6.py - we manipulate the colouring on in the webcam frame creating a checkerboard effect this time accepting inputs for window size and number of squares

openCV7.py - adds text and shapes to a live webcam feed

openCV8.py - rougly calculates and display the current frame rate on a live webcam

openCV9.py - selects a square in the middle of the live feed and has altered this section to grayscale

openCV10.py - live webcam in grayscale with a colour square moving about the live window (look closely depending on lighting)

openCV11.py - click on live webcam window, displays a circle and returns position and event to terminal

openCV12.py - With the main webcam window open click and drag to select subsection region of interest to open in new window - For this to work: when running need to hold left click down then drag across the webcam window before releasing

openCV13.py - created trackbars that manipulate a circle animation within the live webcam feed and can then change its size and position

openCV14.py - uses trackbars to maipulate the size and position of the live webcam window itself

openCV15.py - click on the live webcam feed, a new window will appear displaying the colour and rgb code of the colour within the specific pixel that was clicked

openCV16.py - works on and display HSV colours (instead of using rgb)

openCV17.py - need a brightly coloured object - use the high and low value trackers and the smaller webcam windows to change the valeus so only the coloured object appears - this can be used later to track by colour

openCV18.py - need 2 different brightly coloured objects - use multiple high and low value trackers and the smaller webcam windows to change the values so only the coloured objects appears - this can be used later to track by colour

openCV19.py - (may take time to load) - using a brightly coloured object adjust the trackers so only the coloured object appears on the lower webcam feeds - will highlight the object using squares to highlight the object of interest

openCV20.py - using a brightly coloured object adjust the trackers so only the coloured object appears on the lower webcam feeds - the main webcam window will move across your monitor based on the motion of the object you are holding

openCV21.py - using the classifiers we highlight face or eye features in the webcam

openCV22.py - using the classifiers we highlight both face and eye features in the webcam

openCV23.py - using demo images and text we highlight and identify specific peoples faces

openCV24.py - in the demo images folder added our own images and coded to recognise people i know with the webcam 
# NOTE: removed pics other than my own from the demo image folder
# NOTE: image is sluggish would need to use GPU for better performance

openCV25.py - file manipulation - unfinished

openCV21.py - 


