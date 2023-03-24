import datetime
import json

def create_note():
    """Create a new note and save to file"""
    note = input("Enter your note: ")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"time": time, "note": note}
    with open("notes.json", "a") as file:
        json.dump(data, file)
        file.write("\n")
    print("Note saved successfully!")

def view_notes():
    """View all saved notes"""
    with open("notes.json", "r") as file:
        for line in file:
            data = json.loads(line)
            print(f"{data['time']}: {data['note']}")

while True:
    print("\nMenu:")
    print("1. Create a new note")
    print("2. View saved notes")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")
