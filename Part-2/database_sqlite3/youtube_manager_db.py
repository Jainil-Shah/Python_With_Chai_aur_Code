import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    duration TEXT NOT NULL
)
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print("\n")
    print("ID - Title - Duration")
    print("-------------------------------")
    for row in cursor.fetchall():
        print(f"{row[0]} - {row[1]} - {row[2]}")
    print("-------------------------------")

def add_video(title, duration):
    cursor.execute("INSERT INTO videos (title, duration) VALUES (?, ?)", (title, duration))
    con.commit()

def update_video(index, new_title, new_duration):
    cursor.execute("UPDATE videos SET title = ?, duration = ? WHERE id = ?", (new_title, new_duration, index))
    con.commit()

def delete_video(index):
    cursor.execute("DELETE FROM videos WHERE id = ?", (index,))
    con.commit()

def main():
    while True:
        print("\nYoutube video manager app with DB")
        print("1. List videos")
        print("2. Add video")
        print("3. Update videos")
        print("4 Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        match(choice):
            case '1':
                list_videos()
            case '2':
                title = input("Enter video title: ")
                duration = input("Enter video duration: ")
                add_video(title, duration)
            case '3':
                index = int(input("Enter video index: "))
                title = input("Enter video new title: ")
                duration = input("Enter video new duration: ")
                update_video(index, title, duration)
            case '4':
                index = int(input("Enter video index: "))
                delete_video(index)
            case '5':
                print("Exiting the Application")
                break
            case _:
                print("Invalid choice")
                continue

    print("\nClosing the connection")
    
    con.close()   
        
if __name__ == '__main__':
    main()