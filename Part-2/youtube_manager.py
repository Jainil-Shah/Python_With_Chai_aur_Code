import json

def load_data():
    try:
        with open ("youtube.txt", "r") as file:
            json.load(file)
    except Exception as e:
        print("Error: ", e)
        return []
    

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']}")
        
def add_video(videos):
    title = input("Enter the title of the video: ")
    time = input("Enter the video duration: ")
    videos.append({"title": title, "time": time})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager")
        print("1. List all Videos")
        print("2. Add Video")
        print("3. Update Video Details")
        print("4. Delete Video")
        print("5. Exit The Application")
        
        choice = int(input("Enter your choice: "))
        
        print(f"\nDEBUGING:\n")
        print(f"Videos: {videos}\n")
        
        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                print("Exiting the Application")
                break
            case _:
                print("Invalid Choice")
                
    print("\nThank you for using Youtube Manager!")

if __name__ == "__main__":
    main()
    