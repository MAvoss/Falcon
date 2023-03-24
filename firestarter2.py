import os

from tkinter import *
from tkinter import filedialog

class FireStarter:
    def __init__(self, master):
        self.master = master
        master.title("FireStarter")
        
        # Create a label to display output
        self.label = Label(master, text="Output:")
        self.label.pack()

        # Create a text box to display output
        self.text = Text(master, height=10, width=40)
        self.text.pack()

        # Create a button to connect to ADB
        self.button_connect = Button(master, text="Connect", command=self.connect)
        self.button_connect.pack()

        # Create a button to start ADB server
        self.button_start_server = Button(master, text="Start Server", command=self.start_server)
        self.button_start_server.pack()

        # Create a button to kill ADB server
        self.button_kill_server = Button(master, text="Kill Server", command=self.kill_server)
        self.button_kill_server.pack()

        # Create a button to install an APK
        self.button_install_apk = Button(master, text="Install APK", command=self.install_apk)
        self.button_install_apk.pack()

        # Create a button to reboot the device
        self.button_reboot = Button(master, text="Reboot", command=self.reboot)
        self.button_reboot.pack()

    # Method to run an ADB command and display its output
    def run_command(self, command):
        # Clear the output text box
        self.text.delete('1.0', END)
        # Open a new process to run the command
        process = os.popen(command)
        # Read the output of the process
        output = process.read()
        # Insert the output into the text box
        self.text.insert(END, output)

    # Method to connect to ADB
    def connect(self):
        # Construct the ADB command to connect to the device
        command = 'adb connect ' + self.textbox.get()
        # Run the ADB command and display its output
        self.run_command(command)

    # Method to start the ADB server
    def start_server(self):
        # Construct the ADB command to start the server
        command = 'adb start-server'
        # Run the ADB command and display its output
        self.run_command(command)

    # Method to kill the ADB server
    def kill_server(self):
        # Construct the ADB command to kill the server
        command = 'adb kill-server'
        # Run the ADB command and display its output
        self.run_command(command)

    # Method to install an APK
    def install_apk(self):
        # Open a file dialog to select the APK file
        filename = filedialog.askopenfilename(initialdir='C:\\', title='Select your APK..', filetypes=(('APK files', '*.apk'),))
        # If a file was selected
        if filename:
            # Construct the ADB command to install the APK
            command = 'adb install "' + filename + '"'
            # Run the ADB command and display its output
            self.run_command(command)
            # Display a message box to indicate that the APK was installed
            messagebox.showinfo(title=None, message='.APK is Installed')

    # Method to reboot the device
    def reboot(self):
        # Construct the ADB command to reboot the device
        command = 'adb reboot'
        # Run the ADB command and display its output
        self.run_command(command)

# Create a new Tkinter window
root = Tk()
# Create a new instance of the FireStarter class
