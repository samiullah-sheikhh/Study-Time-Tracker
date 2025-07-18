import os

FILE = "study_log.txt"

def load_data():
    data = {}
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                subject, minutes = line.strip().split(":")
                data[subject] = data.get(subject, 0) + int(minutes)
    return data

def save_data(data):
    with open(FILE, "w") as f:
        for subject, minutes in data.items():
            f.write(f"{subject}:{minutes}\n")

def add_study_time(data):
    subject = input("Enter subject name: ").strip()
    try:
        minutes = int(input("Enter time spent (in minutes): "))
        data[subject] = data.get(subject, 0) + minutes
        print(f"✅ Added {minutes} mins to {subject}")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def show_summary(data):
    if not data:
        print("📂 No study data found.")
    else:
        print("\n📊 Study Summary:")
        for subject, mins in data.items():
            hours = mins // 60
            mins_left = mins % 60
            print(f"• {subject}: {hours} hrs {mins_left} mins")

def main():
    data = load_data()
    while True:
        print("\n1. Add Study Time\n2. Show Summary\n3. Exit")
        choice = input("Select: ")
        if choice == "1":
            add_study_time(data)
            save_data(data)
        elif choice == "2":
            show_summary(data)
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
