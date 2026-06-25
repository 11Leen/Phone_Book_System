import datetime

def load_notes(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_notes(filename, notes):
    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")

def show_notes(notes):
    if not notes:
        print("No notes yet.")
    else:
        print(f"\n📋 You have {len(notes)} notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

notes = load_notes("notes.txt")

while True:
    print("\nOptions: 1-Add  2-Show  3-Delete  4-Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_note = input("Enter new note: ")
    # نضيف التاريخ والوقت مع الملاحظة
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_with_time = f"{new_note} (added on {timestamp})"
    # التعديل هنا: نُضيف المتغير الذي يحتوي على الوقت والتاريخ
        notes.append(note_with_time) 
        save_notes("notes.txt", notes)
        
    elif choice == "2":
        show_notes(notes)

    elif choice == "3":
        show_notes(notes)
        num = int(input("Enter note number to delete: "))
        if 1 <= num <= len(notes):
            notes.pop(num - 1)
            save_notes("notes.txt", notes)

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice, try again.")
