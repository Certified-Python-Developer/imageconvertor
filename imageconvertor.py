import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Function to handle PNG to JPEG conversion
def convert_to_jpeg(png_path, jpeg_path):
    try:
        img = Image.open(png_path)
        img = img.convert("RGB")
        img.save(jpeg_path)
        status_label.config(text="Conversion successful!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

# Function to handle file upload
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        png_entry.delete(0, tk.END)
        png_entry.insert(0, file_path)

# Function to handle JPEG download
def download_jpeg():
    png_path = png_entry.get()
    if not png_path:
        status_label.config(text="Please upload a PNG file first", fg="orange")
        return
    
    jpeg_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
    if jpeg_path:
        convert_to_jpeg(png_path, jpeg_path)

# Creating the main window
root = tk.Tk()
root.title("PNG to JPEG Converter")
root.geometry("400x200")
root.configure(bg="#b0e0e6")  # Pastel blue background color

# Labels
tk.Label(root, text="Upload PNG Image:", bg="#b0e0e6").pack(pady=10)
png_entry = tk.Entry(root, width=40)
png_entry.pack()

# Buttons
upload_button = tk.Button(root, text="Upload PNG", command=upload_file)
upload_button.pack(pady=10)

convert_button = tk.Button(root, text="Convert to JPEG", command=download_jpeg)
convert_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="", bg="#b0e0e6")
status_label.pack(pady=10)

root.mainloop()
