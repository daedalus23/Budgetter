import customtkinter as ctk
from tkinter import Label, Toplevel, Listbox, Scrollbar
from PIL import Image, ImageTk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class TransactionAnalyzerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("Transaction Analyzer")
        self.configure(bg='#2e2e2e')
        self.overrideredirect(True)
        self._create_custom_top_bar()

        # Main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, side=ctk.TOP, fill=ctk.BOTH, expand=True)

        self._build_ui()

    def _build_ui(self):
        self._create_input_frame()
        self._create_button_frame()
        self._create_transaction_list()

    def _create_custom_top_bar(self):
        self.top_bar_color = '#2e2e2e'
        self.top_bar = ctk.CTkFrame(self)
        self.top_bar.pack(fill=ctk.X, padx=5, pady=5, side=ctk.TOP)

        # Load and resize the images
        close_img = Image.open(r".\bin\assets\close_icon.png")
        close_img_resized = close_img.resize((20, 20), Image.LANCZOS)
        self.close_image = ImageTk.PhotoImage(close_img_resized)

        minimize_img = Image.open(r".\bin\assets\minimize_icon.png")
        minimize_img_resized = minimize_img.resize((20, 20), Image.LANCZOS)
        self.minimize_image = ImageTk.PhotoImage(minimize_img_resized)

        # Create the labels with the resized images
        self.close_label = Label(self.top_bar, image=self.close_image, bg=self.top_bar_color, borderwidth=0)
        self.close_label.bind("<Button-1>", lambda e: self.destroy())
        self.close_label.pack(side=ctk.RIGHT, padx=5)

        self.minimize_label = Label(self.top_bar, image=self.minimize_image, bg=self.top_bar_color, borderwidth=0)
        self.minimize_label.bind("<Button-1>", lambda e: self.hide_window())
        self.minimize_label.pack(side=ctk.RIGHT, padx=5)

        # Bind the functions for dragging
        self.top_bar.bind("<ButtonPress-1>", self.on_press)
        self.top_bar.bind("<B1-Motion>", self.on_motion)

    def _create_input_frame(self):
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(pady=10, fill=ctk.X, expand=True)

        self.transaction_label = ctk.CTkLabel(self.input_frame, text="Transaction Description")
        self.transaction_label.pack(side=ctk.LEFT, padx=5)
        self.transaction_entry = ctk.CTkEntry(self.input_frame)
        self.transaction_entry.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=5)

    def _create_button_frame(self):
        self.buttons_frame = ctk.CTkFrame(self.main_frame)
        self.buttons_frame.pack(pady=10, fill=ctk.X, expand=True)

        self.categorize_button = ctk.CTkButton(self.buttons_frame, text="Categorize Transaction",
                                               command=self.categorize_transaction)
        self.categorize_button.pack(side=ctk.LEFT, padx=5, fill=ctk.X, expand=True)

        self.clear_button = ctk.CTkButton(self.buttons_frame, text="Clear List", command=self.clear_list)
        self.clear_button.pack(side=ctk.LEFT, padx=5, fill=ctk.X, expand=True)

    def _create_transaction_list(self):
        self.transaction_list_frame = ctk.CTkFrame(self.main_frame)
        self.transaction_list_frame.pack(pady=10, fill=ctk.BOTH, expand=True)

        self.scrollbar = Scrollbar(self.transaction_list_frame)
        self.scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        self.transaction_listbox = Listbox(self.transaction_list_frame, yscrollcommand=self.scrollbar.set)
        self.transaction_listbox.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        self.scrollbar.config(command=self.transaction_listbox.yview)

    def categorize_transaction(self):
        description = self.transaction_entry.get()
        category = self.categorize_description(description)
        self.transaction_listbox.insert(ctk.END, f"{description} - {category}")
        self.transaction_entry.delete(0, ctk.END)

    @staticmethod
    def categorize_description(description):
        # This is where you integrate the transaction categorization function.
        # For simplicity, I'm returning a dummy category.
        return "Sample Category"

    def clear_list(self):
        self.transaction_listbox.delete(0, ctk.END)

    def on_press(self, event):
        self.x = event.x
        self.y = event.y

    def on_motion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))

    def hide_window(self):
        # Create a new top-level window to restore the main window
        self.temp_win = Toplevel(self)
        self.temp_win.overrideredirect(True)
        self.temp_win.geometry("1x1+0+0")
        self.temp_win.bind("<Button-1>", self.restore_window)
        self.withdraw()

    def restore_window(self):
        self.temp_win.destroy()
        self.deiconify()

    def on_resize_press(self, event):
        self.resize_start_x = event.x
        self.resize_start_y = event.y

    def on_resize_motion(self, event):
        # Calculate the difference in x and y from the start point
        x_diff = event.x - self.resize_start_x
        y_diff = event.y - self.resize_start_y

        new_width = self.winfo_width() + x_diff
        new_height = self.winfo_height() + y_diff

        self.geometry(f"{new_width}x{new_height}")

    def _create_input_frame(self):
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(pady=10, fill=ctk.X, expand=True)

        self.tool_id_label = ctk.CTkLabel(self.input_frame, text="Tool ID")
        self.tool_id_label.pack(side=ctk.LEFT, padx=5)
        self.tool_id_entry = ctk.CTkEntry(self.input_frame)
        self.tool_id_entry.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=5)

        self.lpm_label = ctk.CTkLabel(self.input_frame, text="Load Port Module")
        self.lpm_label.pack(side=ctk.LEFT, padx=5)
        self.lpm_entry = ctk.CTkEntry(self.input_frame)
        self.lpm_entry.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=5)

    def _create_plot_frame(self):
        self.plot_frame = ctk.CTkFrame(self.main_frame)
        self.plot_frame.pack(pady=10, fill=ctk.BOTH, expand=True)

    def add_new_widget(self, widget, frame=None, **pack_params):
        """Method to add a new widget to the main_frame or to a specific frame."""
        if frame:
            widget(frame).pack(**pack_params)
        else:
            widget(self.main_frame).pack(**pack_params)
