import tkinter as tk  # tkinter for UI
from tkinter import messagebox  # message box for popup
import Server
from PIL import Image, ImageTk


def get_admin_credentials(callback):
    def validate_credentials():
        # global server
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        # To check if admin Username and Password is not Empty
        if not entered_username or not entered_password:
            tk.messagebox.showerror("Error", "Username and password cannot be empty.")

        else:
            # To Check if the entered username and password match
            if Server.check_admin_credentials(entered_username, entered_password):
                callback(entered_username, entered_password)  # Pass credentials to the callback
                root.destroy()  # Close the UI
                # Show a success message when login is successful
                messagebox.showinfo("Authentication Successful", "Server is ready to accept connections.")

            else:
                # Pop up if authentication failed
                messagebox.showerror("Authentication Failed", "Invalid username or password. Please try again.")

    root = tk.Tk()
    root.title("Server Admin Login")
    root.iconbitmap('256a.ico')

    # Set the window size and position in the center of the screen
    window_width = 500  # Adjust the width as needed
    window_height = 300  # Adjust the height as needed

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Load the top center image
    top_image = Image.open('srm new.png')  # Replace with the actual path
    top_image = top_image.resize((150, 75))
    top_image = ImageTk.PhotoImage(top_image)

    # Create a label to display the top center image
    top_image_label = tk.Label(root, image=top_image)
    top_image_label.image = top_image
    top_image_label.pack(side="top", pady=10)

    # Load the icon image
    icon_image = Image.open('logo bold.png')  # Replace 'path_to_your_icon_image.png' with the actual path
    icon_image = icon_image.resize((120, 60))  # Adjust the size as needed
    icon_image = ImageTk.PhotoImage(icon_image)

    # Create a label to display the icon image in the right bottom corner
    icon_label = tk.Label(root, image=icon_image)
    icon_label.image = icon_image  # To prevent image from being garbage collected
    icon_label.pack(side="right", anchor="se", padx=10, pady=10)

    # Load the icon image
    icon_image2 = Image.open('LW1.png')  # Replace 'path_to_your_icon_image.png' with the actual path
    icon_image2 = icon_image2.resize((120, 60))  # Adjust the size as needed
    icon_image2 = ImageTk.PhotoImage(icon_image2)

    # Create a label to display the icon image in the left bottom corner
    icon_label2 = tk.Label(root, image=icon_image2)
    icon_label2.image = icon_image2  # To prevent image from being garbage collected
    icon_label2.pack(side="left", anchor="sw", padx=10, pady=10)


    username = tk.StringVar()
    password = tk.StringVar()

    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root, textvariable=username)
    username_entry.pack()

    # Create password label and entry
    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, textvariable=password, show="*")
    password_entry.pack()

    # Create login button
    login_button = tk.Button(root, text="Login", command=validate_credentials)
    login_button.pack(pady=10)


    root.mainloop()

if __name__ == "__main__":
    # Used to get credentials from the UI
    def handle_credentials():
        get_admin_credentials(handle_credentials)
