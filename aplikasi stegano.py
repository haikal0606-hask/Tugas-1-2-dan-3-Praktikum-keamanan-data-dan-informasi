import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Steganografi")
        self.root.geometry("500x350")
        self.root.configure(bg="#e8f4f8")

        # Header
        header = tk.Label(root, text="Aplikasi Steganografi", font=("Arial", 14, "bold"), bg="#63b3ed", fg="white")
        header.pack(fill=tk.X)

        # Canvas untuk menampilkan gambar
        self.canvas = tk.Canvas(root, bg="lightgray", width=350, height=250, highlightthickness=1, highlightbackground="#63b3ed")
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # Panel tombol
        button_frame = tk.Frame(root, bg="#e8f4f8")
        button_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        self.image = None

        # Tombol-tombol
        open_button = tk.Button(button_frame, text="Open Image", command=self.open_image, width=12, bg="#63b3ed", fg="white", font=("Arial", 10))
        open_button.pack(pady=5)

        save_button = tk.Button(button_frame, text="Save Image", command=self.save_image, width=12, bg="#63b3ed", fg="white", font=("Arial", 10))
        save_button.pack(pady=5)

        hide_button = tk.Button(button_frame, text="Hide Data", command=self.hide_data, width=12, bg="#63b3ed", fg="white", font=("Arial", 10))
        hide_button.pack(pady=5)

        show_button = tk.Button(button_frame, text="Show Data", command=self.show_data, width=12, bg="#63b3ed", fg="white", font=("Arial", 10))
        show_button.pack(pady=5)

        exit_button = tk.Button(button_frame, text="Exit", command=root.quit, width=12, bg="#ff6b6b", fg="white", font=("Arial", 10))
        exit_button.pack(pady=5)

    def open_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not filepath:
            return

        self.image = Image.open(filepath)
        self.display_image()

    def save_image(self):
        if self.image is None:
            messagebox.showwarning("Warning", "No image to save.")
            return

        filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if filepath:
            self.image.save(filepath)
            messagebox.showinfo("Success", "Image saved successfully.")

    def hide_data(self):
        if self.image is None:
            messagebox.showwarning("Warning", "No image loaded.")
            return

        data = filedialog.askstring("Input Data", "Enter the data to hide:")
        if not data:
            return

        encoded_image = self.image.copy()
        width, height = encoded_image.size
        pixels = encoded_image.load()

        data += "***"  # Marker to indicate end of data
        data_index = 0
        binary_data = ''.join(format(ord(char), '08b') for char in data)

        for y in range(height):
            for x in range(width):
                if data_index < len(binary_data):
                    r, g, b = pixels[x, y]
                    r = (r & ~1) | int(binary_data[data_index])  # Modify LSB
                    pixels[x, y] = (r, g, b)
                    data_index += 1
                else:
                    break

        self.image = encoded_image
        self.display_image()
        messagebox.showinfo("Success", "Data hidden in image.")

    def show_data(self):
        if self.image is None:
            messagebox.showwarning("Warning", "No image loaded.")
            return

        width, height = self.image.size
        pixels = self.image.load()

        binary_data = ""
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                binary_data += str(r & 1)

        data = "".join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
        if "***" in data:
            data = data[:data.index("***")]
            messagebox.showinfo("Hidden Data", f"Data found: {data}")
        else:
            messagebox.showinfo("Hidden Data", "No hidden data found.")

    def display_image(self):
        resized_image = self.image.resize((350, 250))
        tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
