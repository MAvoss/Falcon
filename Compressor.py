import tkinter as tk
from tkinter import filedialog
import json
import zlib
import base64

class FileCompressorGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("File Compressor")
        self.pack()
        self.create_widgets()
        self.compressed_files = []
        self.load_compressed_files()
        
    

    def create_widgets(self):
         # Ask user for file to compress
        def select_and_compress():
            self.choose_file()
            self.compress_file()

        self.file_button = tk.Button(self, text="Select file to compress", command=select_and_compress)
        self.file_button.pack()
        # Ask user for file to compress
        #self.file_button = tk.Button(self, text="Select file to compress", command=self.choose_file)
        #self.file_button.pack()

        # Compress and save file as Base64-encoded string in JSON file
        #self.compress_button = tk.Button(self, text="Compress file", command=self.compress_file)
        #self.compress_button.pack()

        # Show list of compressed files in JSON file
        self.file_listbox = tk.Listbox(self)
        self.file_listbox.pack()

        # Ask user for JSON file to decompress
        #self.json_button = tk.Button(self, text="Select JSON file", command=self.choose_json)
        #self.json_button.pack()

        # Decompress selected file from JSON file
        self.decompress_button = tk.Button(self, text="Decompress selected file", command=self.decompress_file)
        self.decompress_button.pack()

    def choose_file(self):
        self.filepath = filedialog.askopenfilename()

    def compress_file(self):
        with open(self.filepath, "rb") as f:
            compressed_data = zlib.compress(f.read())
        data = {"filename": self.filepath.split("/")[-1], "data": base64.b64encode(compressed_data).decode("utf-8")}
        self.compressed_files.append(data)
        with open("compressed_files.json", "w") as f:
            json.dump(self.compressed_files, f)
        self.update_listbox()

    def choose_json(self):
        self.json_filepath = "compressed_files.json"
        with open(self.json_filepath, "r") as f:
            self.compressed_files = json.load(f)
        self.update_listbox()

    def decompress_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.compressed_files[selected_index[0]]
            compressed_data = base64.b64decode(selected_file["data"])
            filename = selected_file["filename"]
            with open(filename, "wb") as f:
                f.write(zlib.decompress(compressed_data))

    def load_compressed_files(self):
        try:
            with open("compressed_files.json", "r") as f:
                self.compressed_files = json.load(f)
                self.update_listbox()
        except FileNotFoundError:
            pass

    def update_listbox(self):
        self.file_listbox.delete(0, tk.END)
        for file in self.compressed_files:
            self.file_listbox.insert(tk.END, file["filename"])

root = tk.Tk()
app = FileCompressorGUI(master=root)
app.mainloop()
