import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64


def encrypt_des(plaintext, key):
    """Encrypt plaintext using DES."""
    try:
        cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        padded_text = pad(plaintext.encode('utf-8'), DES.block_size)
        encrypted_text = cipher.encrypt(padded_text)
        encrypted_base64 = base64.b64encode(encrypted_text).decode('utf-8')
        return encrypted_base64
    except Exception as e:
        messagebox.showerror("Error", f"Encryption Failed: {str(e)}")
        return None


def decrypt_des(ciphertext, key):
    """Decrypt ciphertext using DES."""
    try:
        cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        decoded_data = base64.b64decode(ciphertext)
        decrypted_text = unpad(cipher.decrypt(decoded_data), DES.block_size).decode('utf-8')
        return decrypted_text
    except Exception as e:
        messagebox.showerror("Error", f"Decryption Failed: {str(e)}")
        return None


def encrypt_action():
    plaintext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if len(key) != 8:
        messagebox.showerror("Error", "Key must be exactly 8 characters long!")
        return

    if plaintext == "":
        messagebox.showerror("Error", "Input text cannot be empty!")
        return

    encrypted = encrypt_des(plaintext, key)
    if encrypted:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)


def decrypt_action():
    ciphertext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    if len(key) != 8:
        messagebox.showerror("Error", "Key must be exactly 8 characters long!")
        return

    if ciphertext == "":
        messagebox.showerror("Error", "Input text cannot be empty!")
        return

    decrypted = decrypt_des(ciphertext, key)
    if decrypted:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)


# GUI Setup
app = tk.Tk()
app.title("DES Encryption/Decryption")
app.geometry("700x500")
app.resizable(False, False)
app.configure(bg="#222831")

# Title
title_label = tk.Label(
    app,
    text="Data Encryption Standard (DES)",
    font=("Arial", 20, "bold"),
    fg="#EEEEEE",
    bg="#222831",
)
title_label.pack(pady=10)

# Key Input
key_frame = tk.Frame(app, bg="#222831")
key_frame.pack(pady=5)
key_label = tk.Label(
    key_frame, text="Key (8 characters): ", font=("Arial", 14), fg="#00ADB5", bg="#222831"
)
key_label.pack(side=tk.LEFT, padx=5)
key_entry = tk.Entry(key_frame, font=("Arial", 14), width=20, bg="#393E46", fg="#FFFFFF", insertbackground="#FFFFFF")
key_entry.pack(side=tk.LEFT, padx=5)

# Input Text
input_label = tk.Label(app, text="Input Text:", font=("Arial", 14), fg="#00ADB5", bg="#222831")
input_label.pack(pady=5)
input_text = scrolledtext.ScrolledText(
    app, wrap=tk.WORD, width=70, height=5, font=("Arial", 12), bg="#393E46", fg="#FFFFFF", insertbackground="#FFFFFF"
)
input_text.pack(pady=5)

# Buttons
button_frame = tk.Frame(app, bg="#222831")
button_frame.pack(pady=10)
encrypt_button = tk.Button(
    button_frame, text="Encrypt", font=("Arial", 14), bg="#00ADB5", fg="#FFFFFF", activebackground="#007F91", command=encrypt_action
)
encrypt_button.pack(side=tk.LEFT, padx=10)
decrypt_button = tk.Button(
    button_frame, text="Decrypt", font=("Arial", 14), bg="#00ADB5", fg="#FFFFFF", activebackground="#007F91", command=decrypt_action
)
decrypt_button.pack(side=tk.LEFT, padx=10)

# Output Text
output_label = tk.Label(app, text="Output Text:", font=("Arial", 14), fg="#00ADB5", bg="#222831")
output_label.pack(pady=5)
output_text = scrolledtext.ScrolledText(
    app, wrap=tk.WORD, width=70, height=5, font=("Arial", 12), bg="#393E46", fg="#FFFFFF", insertbackground="#FFFFFF"
)
output_text.pack(pady=5)

# Footer
footer_label = tk.Label(
    app,
    text="DES Encryption/Decryption Tool - Created with ❤️",
    font=("Arial", 10, "italic"),
    fg="#EEEEEE",
    bg="#222831",
)
footer_label.pack(pady=10)

# Run the application
app.mainloop()