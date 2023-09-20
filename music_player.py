import pygame
import os

pygame.init()

music_directory = "D:/Music/"

music_files = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if file.endswith((".mp3", ".wav"))]

pygame.mixer.init()

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def list_music():
    for i, file in enumerate(music_files):
        print(f"{i+1}. {os.path.basename(file)}")

while True:
    print("\nMusic Player Menu:")
    print("1. Play")
    print("2. Pause")
    print("3. Unpause")
    print("4. Stop")
    print("5. List Music")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        list_music()
        song_choice = int(input("Enter the number of the song to play: ")) - 1
        if 0 <= song_choice < len(music_files):
            play_music(music_files[song_choice])
        else:
            print("Invalid choice.")
    elif choice == "2":
        pause_music()
    elif choice == "3":
        unpause_music()
    elif choice == "4":
        stop_music()
    elif choice == "5":
        list_music()
    elif choice == "6":
        pygame.quit()
        break
    else:
        print("Invalid choice. Please enter a valid option.")
