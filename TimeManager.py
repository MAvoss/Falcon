import tkinter as tk
import csv
import time
import os

class ActivityTracker:
    def __init__(self):
        self.user = os.getlogin()

class ActivityTracker:
    def __init__(self):
        self.user = os.getlogin() # Get the system username
        self.activities = ['Idle', 'Biking', 'Running', 'Swimming', 'Walking']
        self.current_activity = 'Idle'
        self.start_time = time.time()
        self.data = []
        
    def log_activity(self, activity):
        elapsed_time = time.time() - self.start_time
        self.data.append({'user': self.user, 'activity': self.current_activity, 'time': elapsed_time})
        self.current_activity = activity
        self.start_time = time.time()
        
    def save_data(self):
        with open('activity_log.csv', mode='a', newline='') as csv_file:
            fieldnames = ['user', 'activity', 'time']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if csv_file.tell() == 0:
                writer.writeheader() # write header only if the file is empty
            for row in self.data:
                writer.writerow(row)


# GUI setup
root = tk.Tk()
activity_tracker = ActivityTracker()

# Dropdown menu
activity_var = tk.StringVar(root)
activity_var.set(activity_tracker.activities[0]) # set initial value
activity_dropdown = tk.OptionMenu(root, activity_var, *activity_tracker.activities)
activity_dropdown.pack()

# Close button
close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.pack()

# Function to handle activity changes
def on_activity_changed(*args):
    new_activity = activity_var.get()
    activity_tracker.log_activity(new_activity)

activity_var.trace('w', on_activity_changed)

# Start main loop
root.mainloop()

# Save data when program is closed
activity_tracker.save_data()
