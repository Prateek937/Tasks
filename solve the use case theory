import os
import pyttsx3

pyttsx3.speak("Welcome to the programme ! What's your name ?")
name = input("Your name: ")
print(f"Hello, {name} !")

pyttsx3.speak("Hello sir !, I can perform number of tasks for you.")

print("\n1. You want me to show the menu ? or ")
print("2. you want to write sentences yourself ?")
pyttsx3.speak("Press one to see available choices and, two for manually writing sentences.")

choice = int(input("Enter choice: "))
c = "NULL"
#for repeating again and again
while True:
    #if the user wants to see the menu or just wanna write sentences himself
    if (choice == 1) or (c == "menu"):
        pyttsx3.speak("Here are tasks you can perform.")
        print("\nHere's your menu :\n")
        
        #for operations related to command line
        print("command line:")
        print("1. Open Powershell\t2. Open cmd\n3. Fire a command\n")

        #operations related to chrome or web
        print("Web controls:")
        print("4. Open website on chrome\t5. Open chrome\n")
        
        #Operations related to media
        print("Media controls:")
        print("6. Play a song on youtube\t7. Open spotify\n8. Open vlc player\t\t9. open file exporer\n10. Open a path in file explorer")
        print("11. Open windows medial player  12. Open Youtube\n")
        
        #Operations related to editors
        print("Editors:")
        print("13. Open vscode\t\t\t14. Open Jupyter notebook\n15. Open texeditor(notepad)\t16. Open MS word")
        print("17. open paint\t\t\t18. Open powerpoint\n19. Open Ms Excel\n")
        
        # Other features
        print("Others:")
        print("20. launch Calculator\n")

        print("Press 0 or 'CTRL + C' to exit")
        print("press 'menu' to show the menu again")
        
        # avoinding printing the menu again until the user wants to print again
        choice = 2

    print("\nWhat would you like me to do ?")
    pyttsx3.speak("What would you like me to do next ?")
    c = input(">").lower()

    #keywords for the conditions, User can Enter only even programme name to launch
    bools = ["launch", "open", "run", "play","execute","powershell", "prompt" "cmd", "chrome", "youtube","spotify", "explorer", "computer", "player", "code", "vscode", "notebook", "editor","word", "paint", "powerpoint", "excel", "calculator", "1", "2","4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]

    if [x for x in bools if(x in c)]:
        #powershell
        if (c == "1") or ("powershell" in c):
            os.system("start powershell")
            pyttsx3.speak("Opening windows Powershell")
        #command prompt
        elif (c == "2") or ("cmd" in c) or ("command prompt" in c):
            os.system("start cmd")
            pyttsx3.speak("Opening command prompt")
        #opening a website
        elif (c == "4") or ("search" in c) or ("website" in c) or (".com" in c) or (".in" in c) or (".edu" in c):
            pyttsx3.speak("Enter the website with domain")
            search = input("Enter webite with domain: ")
            url = "start chrome ? " + search
            os.system(url)
            pyttsx3.speak("Taking to website")
        #Chrome
        elif (c == "5") or ("chrome" in c):
            os.system("start chrome")
            pyttsx3.speak("Opening chrome for you")
       
        #Spotify
        elif (c == "7") or ("spotify" in c):
            os.system("start spotify")
            pyttsx3.speak("launching spotify for you")
        #Vlc player
        elif (c == "8") or ("vlc" in c) or ("vlc player" in c) or ("video player" in c):
            os.system("start vlc")
            pyttsx3.speak("Opening vlc media player")
        #File Explorer
        elif (c == "9") or ("explorer" in c) or ("files" in c) or ("computer" in c):
            os.system("start explorer")
            pyttsx3.speak("Opening files")
        #Opening a Path in explorer
        elif (c == "10") or ("path" in c):
            path = "start " + input("paste path here :")
            os.system(path) 
            pyttsx3.speak("going to the path")
        #windows Media palyer
        elif (c == "11") or ("wmplayer" in c) or ("windows" in c):
            os.system("start wmplayer")
            pyttsx3.speak("Opening windows media player.")
        #Youtube
        elif (c == "12") or ("youtube" in c):
            os.system("start chrome ? youtube.com")
            pyttsx3.speak("Opening youtube")
        #Visual Studio Code
        elif (c == "13") or ("visual" in c) or ("code" in c):
            os.system("start code")
            pyttsx3.speak("redirecting to visual studio code")
        #Jupyter notebook
        elif (c == "14") or ("jupyter notebook" in c):
            os.system("start jupyter notebook")
            pyttsx3.speak("Opening jupyter notebook")
        #Notepad
        elif (c == "15") or ("editor" in c) or ("notepad" in c):
            os.system("start notepad")
            pyttsx3.speak("Opening notepad")
        #Microsoft Word
        elif (c == "16") or ("word" in c):
            os.system("start winword") 
            pyttsx3.speak("Opening M S word")
        #Ms Paint
        elif (c == "17") or ("paint" in c):
            os.system("mspaint")
            pyttsx3.speak("Opening microsoft paint")
        #Powerpoint
        elif (c == "18") or ("powerpoint" in c):
            os.system("start powerpnt")
            pyttsx3.speak("Opening powerpoint")
        #Ms Excel
        elif (c == "19") or ("excel" in c):
            os.system("start excel.exe")
            pyttsx3.speak("Opening excel")
        #Calculator
        elif (c == "20") or ("calculator" in c):
            os.system("start calc")
            pyttsx3.speak("Here is your calculator")
         #Playing a song on youtube
        elif (c == "6") or ("song" in c) or ("play" in c): 
            pyttsx3.speak("Which song you want me to play sir?")   
            song = input("Enter song: ")
            youtube =  "start chrome ? https://www.youtube.com/results?search_query=" + song
            os.system(youtube)
            pyttsx3.speak("opening song in youtube")
    #firing a command
    elif c == "3" or ("fire" in c) or ("command" in c):
        pyttsx3.speak("Enter command")
        command = input("Enter the command > ")
        os.system(command)
        pyttsx3.speak("Here we go")
    #showing menu again 
    elif c == "menu":
        continue
    #exit
    elif (c == "0") or ("exit" in c) or ("quit" in c) or ("shut" in c):
        break
    
    else:
        pyttsx3.speak("I'm sorry sir, Looks like I can't do this operation. Try anything else")
        print("Looks like I can't do this operation\nTry anything else !\n")

print(f"Bye {name} !")
print("Seeya soon !")
pyttsx3.speak("Bbye !, Keep coding keep learning, Seeya soon !")
exit()
