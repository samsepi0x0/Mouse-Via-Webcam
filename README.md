# Mouse-Via-Webcam
Control Mouse via webcam using just python!

### Overview:
This is a simple python script that uses [opencv](opencv.org) libraries to track fingers from webcam and move mouse accordingly.
[MediaPipe](https://opensource.google/projects/mediapipe) is a python module developed by Google, which can track both hands for us and
gives us 20 marks points on each hand.

With the help of these libraries, we can control the mouse on the basis of the movement of the hand.

### Requirements:
The code works on [Python 3.7](). The dependencies can be installed via pip:
```bash
  $ pip install mediapipe numpy autopy opencv-python
```

### Installation:
If you don't have git installed on your local machine, download the repo as zip file, extract it and move to the respective folder.
If you have git installed on your system, follow the steps below:

  Clone the repo and change to the respective folder.
  ```bash
    $ git clone https://github.com/samsepi0x0/Mouse-Via-Webcam.git
    $ cd Mouse-Via-Webcam
  ```

Run  `app.py` to launch webcam and move the mouse.
  ```bash
    $ python app.py
  ```
  
### Usage:
The webcam launches a 640x480 window, which shows the output of the webcam. Only one hand is detected at a time.
When a hand is detected in the frame, the white box appears which represents the boundary of the screen. Relative position of the index finger 
represents the absolute position of mouse according to that point.
Move the index finger to move the mouse (Keep the other fingers folded).
To click, raise the middle finger and quickly bring it close to the index finger (Release the finger immediately if you want to change the mouse position again).
Refer to the output section below for demonstration.

Exit the program by pressing CTRL+C on the terminal. (For some mysterious reason, pressing 'q' on the frame window doesn't close it) :-)

### Output:
The output of running the code on my local machine.
(Apologies for the GIF quality, I know it sucks.)
<p align="center">
  <img src="output.gif" alt="Output.gif">
</p>

### Note:
I had some trouble running this code in Linux(Ubuntu), and as of now, this code runs only on windows.
If anyone knows how to make autopy run in Linux(Ubuntu), or knows an alternative to that, do inform me.

Contributors are as always welcomed.
