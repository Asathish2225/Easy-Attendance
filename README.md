**Lab Attendance System Using Client Server Architecture**

**Abstract**

The Attendance System is a software application designed to streamline the process of recording and managing attendance for educational institutions. The system consists of two components: a server-side application for authentication and data storage and a client-side graphical user interface (GUI) for users to submit attendance records.

**Important Information**

**Components**

**1.Server Application**

Responsible for authentication and storing attendance data.

Implements RPC (Remote Procedure Call) for communication with the client.

**2.Client GUI**

Allows users to input attendance details, including lab room, student information, and subject.

Utilizes **tkinter** for GUI development and **jsonrpclib** for communication with the server.

Provides a user-friendly interface for attendance submission.

**Project Files**

**Server.py:** Implements server-side functionality for user authentication and attendance data handling.

**ClientUI.py:** Contains the code for the client-side GUI, allowing users to submit attendance records and Executes the attendance UI for the client.

**client.py:** Entry point for the client-side application.

**ServerUI.py:** User interface for server admin login.

**Setup**

Ensure Python is installed.

Install required libraries: **pip install Pillow jsonrpclib-pelix**.

Run the server: **python Server.py**

Run the client: **python client.py**

**Usage**

Launch the client UI using UI_Client.py.

Enter details, including lab room, student information, and subject.

Click "Submit Attendance" to send the data to the server.

View the server console for status messages.

**Contributors**

Sathish (Developer)

**Acknowledgments**

This project was developed for SRM INSTITUTE OF SCIENCE AND TECHNOLOGY at my own interest.
