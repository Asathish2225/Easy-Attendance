import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from jsonrpclib import Server
from PIL import Image, ImageTk
import socket


def create_attendance_ui():
    root = tk.Tk()
    root.title("Attendance System")

    # Set fullscreen mode
    root.state('zoomed')  # On Windows

    # Get screen width and height
    screen_width = root.winfo_screenwidth()

    # Image_logo
    image_path = "srm new.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize((350, 100))
    image = ImageTk.PhotoImage(resized_image)

    # Create a label to display the image
    image_label = ttk.Label(root, image=image)
    image_label.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')  # Adjust pady as needed

    # Heading_1 and Heading_2
    text_label1 = ttk.Label(root, text="FACULTY OF SCIENCE AND HUMANITIES", font=("Georgia", 20, "bold"),
                            foreground='#00008B')
    text_label1.grid(row=1, column=0, columnspan=4, pady=0)  # Adjust pady as needed

    text_label2 = ttk.Label(root, text="Department Of Computer Applications", font=("Georgia", 15, "bold"))
    text_label2.grid(row=2, column=0, columnspan=4, pady=0)  # Adjust pady as needed

    # # This function should return the list of subjects for the given department and semester
    def get_subjects_for_department_and_semester(department, semester, regulation):
        subjects_data = {
            "2020": {
                "Others": {
                    "Not Applicable": ["Not Applicable"]
                },
                "MCA I": {
                    "1": ["Programming Using Java", "Operating System", "Database Technology",
                          "Advanced Web Application Development", "Cyber Security", "Software Engineering",
                          "IT Infrastructure Management"],
                    "2": ["Python Programming", "Computer Networks", "Optimization Techniques",
                          "Android Applications Development", "Programming using C#", "Software Testing",
                          "Data Analysis Using R"]
                },
                "MCA II": {
                    "3": ["Object Oriented Analysis and Design", "Artificial Intelligence and Machine Learning",
                          "Cloud Computing", "Internet of Things (IoT)", "Mini Project Work"],
                    "4": ["Project Work "]
                },
                "M.Sc ADS I": {
                    "1": ["Data Analysis Fundamentals", "Machine Learning for Data Science"],
                    "2": ["Data Visualization and Concepts", "Building Machine Learning Pipelines",
                          "Artificial Intelligence"]
                },
                "M.Sc ADS II": {
                    "3": ["Deep Learning for Data Science", "Cloud Computing", "Exploratory Data Analysis",
                          "Social Media and Text Analytics", "Mini Project Work"],
                    "2": ["Project Work "]
                },
                "BCA (CA) I": {
                    "1": ["Programming for Problem Solving", "Digital  Logic Fundamentals"],
                    "2": ["Object Oriented Programming", "Data Structures and Algorithms", "Go Programming"]
                },
                "BCA (CA) II": {
                    "3": ["Programming in Java", "Operating Systems", "Web development using Node JS and Mongo",
                          "Web development using React JS and Mongo", "Web development using Angular JS and Mongo"],
                    "4": ["Windows Programming using VB.NET", "Database Systems", "Multimedia and Animation",
                          "Artificial Intelligence"]

                },
                "BCA (CA) III": {
                    "5": ["Web Programming", "Computer Networks ", "Software Engineering and Testing",
                          "Lua Programming", "Statistical Package for Social Sciences"],
                    "6": ["Python Programming", "Multimedia Design Principles and Applications",
                          "Object Oriented Analysis and Design", "Internet of  Things", "Project Work "]

                },
                "BCA (DS) I": {
                    "1": ["Introduction to Advanced Computing"],
                    "2": ["Introduction to Data Science", "Advanced Computing With Distributed Data Processing"],

                },
                "BCA (DS) II": {
                    "3": ["Introduction to Deep Learning", "Advanced Computing With Python and GCP",
                          "Introduction to Natural Language Processing", "Data Engineering for Enterprise"],
                    "4": ["Deep Learning for Enterprise", "Introduction to Computer Vision", "Working with Big Data",
                          "Data Science for Enterprise"],

                },
                "BCA (DS) III": {
                    "5": ["Intelligent Automation", "Real-World Computer Vision Applications",
                          "Advanced Analytics and Data Visualization for Enterprise",
                          "Machine Learning for Enterprise"],
                    "6": ["Intelligent Automation for Enterprise", "Project Work"],

                },
                # Add subjects for other departments if needed
            },
            "2023": {
                "Others": {
                    "Not Applicable": ["Not Applicable"]
                },
                "MCA I": {
                    "1": ["Programming Using Java", "Operating System", "Database Technology",
                          "Advanced Web Application Development", "Cyber Security", "Software Engineering",
                          "IT Infrastructure Management"],
                    "2": ["Python Programming", "Computer Networks", "Optimization Techniques",
                          "Android Applications Development", "Programming using C#", "Software Testing",
                          "Data Analysis Using R"]
                },
                "MCA II": {
                    "3": ["Object Oriented Analysis and Design", "Artificial Intelligence and Machine Learning",
                          "Cloud Computing", "Internet of Things (IoT)", "Mini Project Work"],
                    "4": ["Project Work "]
                },
                "M.Sc ADS I": {
                    "1": ["Data Analysis Fundamentals", "Machine Learning for Data Science"],
                    "2": ["Data Visualization and Concepts", "Building Machine Learning Pipelines",
                          "Artificial Intelligence"]
                },
                "M.Sc ADS II": {
                    "3": ["Deep Learning for Data Science", "Cloud Computing", "Exploratory Data Analysis",
                          "Social Media and Text Analytics", "Mini Project Work"],
                    "2": ["Project Work "]
                },
                "BCA (CA) I": {
                    "1": ["Programming for Problem Solving", "Digital  Logic Fundamentals"],
                    "2": ["Object Oriented Programming", "Fundamentals of Data Structures and Algorithms"]
                },
                "BCA (CA) II": {
                    "3": ["Programming in Java", "Database Management System", "Fundamentals of Data Science",
                          "Web Programming"],
                    "4": ["Open Source Technologies", "Operating System", "Serverless Database Techniques",
                          "Go Programming"]

                },
                "BCA (CA) III": {
                    "5": ["Python Programming", "Computer Networks ", "Object Oriented Analysis and Design",
                          "Windows Programming using VB.NET", "Data Analysis using R",
                          "Web development using Angular JS and MongoDB", "Basics of Android", "Lua Programming"],
                    "6": ["Software Engineering and Testing", "Wireless Communication and Mobile Computing",
                          "Research Methodology", "Introduction to Animation", "Introduction to Computer Vision",
                          "Programming Using C#", "Introduction to Machine Learning", "Mini Project"]

                },
                "BCA (CA) IV": {
                    "7": ["Cloud Computing", "Web Development using Node JS and MongoDB", "Cyber Security",
                          "Data Visualization and Exploring Models", "Basics of  IOS",
                          "Project Phase-I"],
                    "8": ["Big Data Analytics", "Blockchain Technology",
                          "Internet of Things", "E-Commerce", "Artificial Intelligence",
                          "Data Wrangling", "Project Phase-II"]

                },
                "BCA (DS) I": {
                    "1": ["Programming Using Java", "Programming Using Java", "Role of Mathematics in AI"],
                    "2": ["Introduction to Computing With Distributed Data Processing",
                          "Fundamentals of Data Structures and Algorithms", "Role of Statistics in AI"],

                },
                "BCA (DS) II": {
                    "3": ["Role of Statistics in AI", "Data Base Management System",
                          "Machine Learning", "Data Wrangling", "UDS23S03L	Web Programming"],
                    "4": ["Deep Learning", "Advanced Computing With Python and GCP",
                          "Fundamentals of Natural Language Processing",
                          "Office Automation with Advanced Excel", "Go Programming"],

                },
                "BCA (DS) III": {
                    "5": ["Deep Learning with Keras and Tensorflow", "Big Data Analytics with Applications",
                          "Intelligent Automation", "Data Warehousing and Data Mining",
                          "Introduction to Cloud Computing", "No-Code Applications", "Lua Programming"],
                    "6": ["Introduction to Computer Vision", "Advanced Analytics and Data Visualization for Enterprise",
                          "Research Methodology", "Machine Learning for Enterprise", "Blockchain Technology",
                          "Introduction to Animation", "Mini Project"],

                },
                "BCA (DS) IV": {
                    "7": ["Data Science for Business Analytics", "Digital Transformation",
                          "Real World Computer Vision Applications", "Digital Marketing",
                          "Introduction to Internet of Things", "Project Phase-I"],
                    "8": ["AI and Intelligent Automation for Enterprise",
                          "Technology Leadership and Innovation Management",
                          "Social Media and Text Analytics", "Statistical Analysis and Business Applications",
                          "Blockchain Technology",
                          "Applications of Edge IoT and ML", "Basics of Cyber Security", "Project Phase-II"],

                },

            },
        }
        return subjects_data.get(regulation, {}).get(department, {}).get(semester, [])

    # Function to get available semesters for a given department
    def get_semesters_for_department(department):
        semesters_data = {
            "Others": ["Not Applicable"],
            "MCA I": ["1", "2"],
            "MCA II": ["3", "4"],
            "M.Sc ADS I": ["1", "2"],
            "M.Sc ADS II": ["3", "4"],
            "BCA (CA) I": ["1", "2"],
            "BCA (CA) II": ["3", "4"],
            "BCA (CA) III": ["5", "6"],
            "BCA (CA) IV": ["7", "8"],
            "BCA (DS) I": ["1", "2"],
            "BCA (DS) II": ["3", "4"],
            "BCA (DS) III": ["5", "6"],
            "BCA (DS) IV": ["7", "8"],
            # Add semesters for other departments if needed
        }
        return semesters_data.get(department, [])

    def is_valid_reg_number(reg_number):
        return len(reg_number) == 15 and reg_number.startswith("RA")

    # User-Interface to get data
    def send_attendance():
        lab_room = lab_room_var.get()
        name = name_entry.get()
        reg_number = reg_number_entry.get()
        subject = subject_var.get()
        department = department_var.get()
        section = section_var.get()
        selected_semester = semester_var.get()
        client_hostname = socket.gethostname()

        if not (lab_room and name and reg_number and department and subject and section):
            tk.messagebox.showerror("Error", "All fields must be filled.")
        elif not is_valid_reg_number(reg_number):
            tk.messagebox.showerror("Error",
                                    "Invalid registration number. It must be 15 characters long and start with 'RA'.")
        else:
            response = conn.add_attendance(lab_room, name, reg_number, department, selected_semester, section,
                                           subject, client_hostname)
            messagebox.showinfo('Attendance Status', response)
            root.destroy()

    # lab room
    ttk.Label(root, text="Lab Room:", font=("Georgia", 12)).grid(row=3, column=1, sticky='e', padx=(0, 100))
    lab_dropdown = ttk.Combobox(root, values=["Lab 401", "Lab 402", "Lab 403", "Lab 404", "Lab 503", "Lab 504", "Lab 708", "Lab 908", "Poly-1", "Poly-2"], font=("Georgia", 10))
    lab_dropdown.grid(row=3, column=2, pady=10, sticky='w')
    lab_dropdown.set("Select Lab")
    lab_room_var = tk.StringVar(root)
    lab_room_var.set("Select Lab Room")

    # Name

    ttk.Label(root, text="Name:", font=("Georgia", 12)).grid(row=4, column=1, pady=10, sticky='e', padx=(0, 100))
    name_entry = ttk.Entry(root, width=33)
    name_entry.grid(row=4, column=2, pady=10, sticky='w')

    # Register number
    ttk.Label(root, text="Register Number:", font=("Georgia", 12)).grid(row=5, column=1, pady=10, sticky='e', padx=(0, 100))
    reg_number_entry = ttk.Entry(root, width=33)
    reg_number_entry.grid(row=5, column=2, pady=10, sticky='w')

    # Regulation
    ttk.Label(root, text="Regulation:", font=("Georgia", 12)).grid(row=6, column=1, pady=10, sticky='e', padx=(0, 100))
    regulation_dropdown = ttk.Combobox(root, values=["2020", "2023"], font=("Georgia", 10))
    regulation_dropdown.grid(row=6, column=2, pady=10, sticky='w')
    regulation_var = tk.StringVar(root)
    regulation_var.set("Select Regulation")

    # Department
    ttk.Label(root, text="Department:", font=("Georgia", 12)).grid(row=7, column=1, pady=10, sticky='e', padx=(0, 100))
    department_var = tk.StringVar(root)
    department_var.set("Select Class")
    department_dropdown = ttk.Combobox(root, values=["Others", "MCA I", "MCA II", "M.Sc ADS I", "M.Sc ADS II", "BCA (CA) I", "BCA (CA) II", "BCA (CA) III", "BCA (DS) I", "BCA (DS) II", "BCA (DS) III"], font=("Georgia", 10))
    department_dropdown.grid(row=7, column=2, pady=10, sticky='w')

    semester_var = tk.StringVar(root)
    semester_var.set("Select Semester")

    # Function to update semesters based on the selected department
    def update_semesters(*args):
        selected_department = department_var.get()
        semester_var.set("Select Semester")  # Clear current selection
        if selected_department != "Select Class":
            semesters = get_semesters_for_department(selected_department)
            semester_dropdown['values'] = semesters
            semester_dropdown.set("Select Semester")  # Set default selection

    # # Use trace to call update_semesters when department_var changes
    # department_var.trace_add('write', lambda *args: update_semesters(department_var.get()))
    # Bind the update_semesters function to the department dropdown
    department_dropdown.bind("<<ComboboxSelected>>", update_semesters)
    #  Semester
    semesters = ["1", "2", "3", "4", "5", "6"]
    ttk.Label(root, text="Semester:", font=("Georgia", 12)).grid(row=8, column=1, pady=10, sticky='e', padx=(0, 100))

    semester_dropdown = ttk.Combobox(root, values=semesters, font=("Georgia", 10))
    semester_dropdown.grid(row=8, column=2, pady=10, sticky='w')

    # Section
    ttk.Label(root, text="Section:", font=("Georgia", 12)).grid(row=9, column=1, pady=10, sticky='e', padx=(0, 100))
    section_dropdown = ttk.Combobox(root, values=["A", "B", "C", "D", "E", "F", "G", "H"], font=("Georgia", 10))
    section_dropdown.grid(row=9, column=2, pady=10, sticky='w')
    section_var = tk.StringVar(root)
    section_var.set("Select Section")

    # Subject
    ttk.Label(root, text="Subject:", font=("Georgia", 12)).grid(row=10, column=1, pady=10, sticky='e', padx=(0, 100))
    subject_var = tk.StringVar(root)
    subject_var.set("Select Subject")
    subject_options = ["Select Subject"]
    subject_dropdown = ttk.Combobox(root,  values=subject_options, font=("Georgia", 10))
    subject_dropdown.grid(row=10, column=1, padx=(0, 500), pady=10, sticky='e')

    # Function to update subjects based on Department, Semester, and Regulation
    def update_subjects(selected_department, selected_semester, selected_regulation):
        subject_var.set("Select Subject")  # Clear current selection
        if selected_department != "Select Class" and selected_semester != "Select Semester" and selected_regulation in ["2020", "2023"]:
            subjects = get_subjects_for_department_and_semester(selected_department, selected_semester, selected_regulation)
            subject_options = subjects
            subject_dropdown['values'] = subject_options
            subject_dropdown.set("Select Subject")  # Set default selection
        else:
            # Handle the case where an invalid combination is selected
            subject_dropdown.set("Select Subject")
            subject_dropdown['values'] = ["Invalid Selection"]

    # Set the update_subjects function as the callback for department, semester, and regulation dropdowns
    department_dropdown.bind("<<ComboboxSelected>>", lambda event: update_subjects(department_var.get(), semester_var.get(), regulation_var.get()))
    semester_dropdown.bind("<<ComboboxSelected>>", lambda event: update_subjects(department_var.get(), semester_var.get(), regulation_var.get()))
    regulation_dropdown.bind("<<ComboboxSelected>>", lambda event: update_subjects(department_var.get(), semester_var.get(), regulation_var.get()))

    # Add Canvas with Text
    canvas_height = 8*10
    canvas = tk.Canvas(root, bg="orange", width=screen_width, height=canvas_height)
    canvas.grid(row=13, column=0, columnspan=4, sticky='nsew')

    about_text = (
        "Welcome to Easy Lab Attendance Maintenance System\n"
        "Enjoy your Student Life & Excel at SRM\n"
        "Developed By\nSathish & Team - MCA'24\n"
        "Copyright © Department of Computer Applications, SRM IST"
    )

    # Add Text to Canvas
    center_x = screen_width // 2
    line_height = 10

    for i, line in enumerate(about_text.split('\n')):
        y_coordinate = i * line_height + 15
        canvas.create_text(center_x, y_coordinate + i * line_height, text=line, font=("Georgia", 10, 'bold'), fill="black",
                           anchor='n')

    # Load the livewire image
    original_logo = Image.open("LW1.png")
    resized_logo = original_logo.resize((300, 125))  # Adjust the size as needed
    logo_image = ImageTk.PhotoImage(resized_logo)

    original_logo2 = Image.open("logo slim.png")
    resized_logo2 = original_logo2.resize((200, 100))  # Adjust the size as needed
    logo_image2 = ImageTk.PhotoImage(resized_logo2)

    # Add the image to the canvas
    canvas.create_image(1, 0, image=logo_image, anchor='nw')  # Adjust coordinates as needed
    canvas.create_image(screen_width - 50, 1, image=logo_image2, anchor='ne')  # Adjust coordinates as needed

    # Configure row and column weights for resizing
    root.grid_rowconfigure(12, weight=1)
    root.grid_rowconfigure(13, weight=1)

    conn = Server('http://10.1.121.93:2509')
    root.mainloop()
create_attendance_ui()
