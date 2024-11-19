import tkinter as tk
from tkinter import filedialog, messagebox


# Function to validate form fields and handle submission
def handle_submit():
    name = name_entry.get()
    age = age_var.get()
    file_path = file_label.cget("text")

    # Validation
    if not name or age == "Select Age" or file_path == "No file selected":
        messagebox.showerror("Error", "Please fill all fields and upload a file.")
        return

    if int(age) <= 0 or int(age) > 120:
        messagebox.showerror("Error", "Age must be between 1 and 120.")
        return

    # Successful submission message
    messagebox.showinfo("Success", f"Submitted:\nName: {name}\nAge: {age}\nFile: {file_path}")


# Function to handle file upload
def handle_file_upload():
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        file_label.config(text=file_path.split("/")[-1])  # Display only the file name


# Create the main window
root = tk.Tk()
root.title("Healthcare Dashboard")
root.geometry("500x400")
root.config(bg="#e8f5e9")

# Header
header = tk.Label(
    root,
    text="Healthcare Dashboard",
    bg="#1565c0",
    fg="white",
    font=("Arial", 18, "bold"),
    pady=10,
)
header.pack(fill="x")

# Card-like Frame
frame = tk.Frame(root, bg="white", padx=20, pady=20, relief="raised", borderwidth=3)
frame.pack(pady=30)

# Name Field
name_label = tk.Label(frame, text="Name:", font=("Arial", 12), bg="white", fg="#333333", anchor="w")
name_label.grid(row=0, column=0, pady=10, sticky="w")
name_entry = tk.Entry(
    frame, width=30, font=("Arial", 12), relief="solid", fg="#000000", bg="white"
)
name_entry.grid(row=0, column=1, pady=10)

# Age Dropdown
age_label = tk.Label(frame, text="Age:", font=("Arial", 12), bg="white", fg="#333333", anchor="w")
age_label.grid(row=1, column=0, pady=10, sticky="w")

age_var = tk.StringVar(value="Select Age")  # Default value for the dropdown
age_options = [str(i) for i in range(1, 121)]  # Age options from 1 to 120
age_dropdown = tk.OptionMenu(frame, age_var, *age_options)
age_dropdown.config(font=("Arial", 12), bg="white", fg="#000000", width=20)
age_dropdown.grid(row=1, column=1, pady=10)

# File Upload
file_button = tk.Button(
    frame,
    text="Upload File",
    font=("Arial", 10, "bold"),
    bg="#cccccc",
    fg="black",
    command=handle_file_upload,
)
file_button.grid(row=2, column=0, pady=10, sticky="w")
file_label = tk.Label(
    frame, text="No file selected", font=("Arial", 10), fg="#555555", bg="white", anchor="w"
)
file_label.grid(row=2, column=1, pady=10, sticky="w")

# Submit Button
submit_button = tk.Button(
    frame,
    text="Submit",
    font=("Arial", 12, "bold"),
    bg="#cccccc",
    fg="black",
    command=handle_submit,
)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()