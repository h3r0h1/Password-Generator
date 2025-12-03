import customtkinter as ctk
import random
import string

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("520x380")
        self.configure(bg_color="#f9f9f9")

        self.password_label = ctk.CTkLabel(
            self,
            text="Click 'Generate Password' to create a password",
            wraplength=480,
            fg_color=None,
            text_color="black",
            font=("Arial", 18, "bold")
        )
        self.password_label.pack(pady=(30,20))

        length_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_width=0)
        length_frame.pack(pady=5, padx=20, fill="x")

        length_label = ctk.CTkLabel(length_frame, text="Password Length:", fg_color=self.cget("bg"))
        length_label.pack(side="left", padx=(0, 5))

        self.length_entry = ctk.CTkEntry(length_frame, width=60, justify="center")
        self.length_entry.insert(0, "12")
        self.length_entry.pack(side="left")

        option_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_width=0)
        option_frame.pack(pady=10, padx=20, fill="x")

        option_label = ctk.CTkLabel(option_frame, text="Password Type:", fg_color=self.cget("bg"))
        option_label.pack(side="left", padx=(0,5))

        self.option_var = ctk.StringVar(value="Letters + Numbers + Symbols")
        option_menu = ctk.CTkOptionMenu(
            option_frame,
            variable=self.option_var,
            values=["Letters Only","Letters + Numbers","Letters + Numbers + Symbols"]
        )
        option_menu.pack(side="left")

        button_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_width=0)
        button_frame.pack(pady=20)

        generate_button = ctk.CTkButton(
            button_frame,
            text="Generate Password",
            command=self.generate_password,
            fg_color="#4CAF50",
            hover_color="#45a049",
            text_color="white",
            corner_radius=12,
            width=180
        )
        generate_button.pack(side="left", padx=10)

        copy_button = ctk.CTkButton(
            button_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard,
            fg_color="#2196F3",
            hover_color="#1E88E5",
            text_color="white",
            corner_radius=12,
            width=180
        )
        copy_button.pack(side="left", padx=10)

        self.status_label = ctk.CTkLabel(self, text="", fg_color=self.cget("bg"), text_color="green", font=("Arial",14))
        self.status_label.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            self.password_label.configure(text="Please enter a valid number")
            return
        if length <= 0:
            self.password_label.configure(text="Length must be positive")
            return

        letters = string.ascii_letters
        digits = string.digits
        symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"
        choice = self.option_var.get()
        if choice == "Letters Only":
            chars = letters
        elif choice == "Letters + Numbers":
            chars = letters + digits
        else:
            chars = letters + digits + symbols

        pwd = ''.join(random.choice(chars) for _ in range(length))
        self.password_label.configure(text=pwd, text_color="#0b5394", font=("Arial", 24, "bold"))
        self.status_label.configure(text="")

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_label.cget("text"))
        self.status_label.configure(text="Copied to clipboard!")

if __name__ == "__main__":
    app = App()
    app.mainloop()