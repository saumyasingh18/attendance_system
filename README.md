Objectives
The primary objectives of the Attendance System are:

To automate the process of marking attendance using facial recognition.
To provide a user-friendly interface for starting, stopping, and checking attendance records.
To maintain accurate records of attendance in a CSV file for easy retrieval and analysis.
Tools and Libraries
The following tools and libraries are used in the implementation of the Attendance System:

Python: The main programming language used for developing the system.
OpenCV: A library for computer vision tasks, used for capturing video from the webcam.
face_recognition: A library for facial recognition, used to encode and recognize faces.
Tkinter: A standard GUI library for Python, used to create the user interface.
Pandas: A library for data manipulation and analysis, used for handling attendance records.
System Design
The system is designed with a modular approach, encapsulating different functionalities in separate methods. The main components of the system are:

GUI Components:

Start Attendance Button: Initiates the webcam feed and starts the facial recognition process.
Mark Attendance Button: Marks the attendance of the recognized individual.
Stop Attendance Button: Stops the webcam feed and ends the session.
Check Attendance Menu: Opens a popup window displaying the attendance records.
Facial Recognition Components:

Loading Images and Encoding: Loads images from a specified directory and encodes them for facial recognition.
Capturing and Processing Video: Captures video frames from the webcam, detects faces, and matches them with the encoded faces.
Marking Attendance: Writes the attendance records to a CSV file.
Implementation
The implementation of the Attendance System is divided into several methods within a class called AttendanceSystem. Below is a detailed explanation of each method:

Initialization (_init_ method):

Initializes the main GUI components and variables.
Sets up the menu and buttons for starting, marking, and stopping attendance.
Defines the frame and layout for the GUI.
Loading Images and Encoding (load_images_and_encode method):

Loads images from the images directory.
Encodes the faces in the images using the face_recognition library.
Returns the encoded face list and corresponding person names.
Starting Attendance (start_attendance method):

Captures video from the webcam.
Processes each frame to detect and encode faces.
Compares the encoded faces with the known faces to find matches.
Updates the GUI with the camera feed and face recognition results.
Marking Attendance (mark_attendance method):

Writes the name, time, and date of the recognized individual to the Attendance.csv file.
Displays a message box indicating successful marking of attendance.
Stopping Attendance (stop_attendance method):

Releases the webcam and closes the video window.
Resets the buttons to their initial state.
Opening Attendance Records (open_popup method):

Reads the Attendance.csv file using Pandas.
Displays the attendance records in a popup window using a Treeview widget.
Usage Instructions
To use the Attendance System, follow these steps:

Install Required Libraries:

Install the necessary libraries using pip:
bash
Copy code
pip install opencv-python
pip install face_recognition
pip install pillow
pip install pandas
Prepare the Images:

Create a directory named images in the same directory as the script.
Add images of individuals you want to recognize in the images directory. Name each image as the person's name (e.g., John.jpg).
Run the Script:

Execute the script. The GUI should open with options to start attendance, mark attendance, stop attendance, and check attendance.
Click on "Start Attendance" to start the webcam and begin face recognition.
Click on "Mark Attendance" to mark the recognized face.
Click on "Stop Attendance" to stop the webcam and end the session.
Click on "Check Attendance" to open a popup window displaying the attendance records.
