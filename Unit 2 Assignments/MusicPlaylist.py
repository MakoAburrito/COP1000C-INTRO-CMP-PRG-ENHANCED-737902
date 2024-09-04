#Assignment Title: Music Playlist Generator
#Author by: Melissa De Jesus
#Student number: M16004939
#Class: COP 1000C Intro-Cmp-prg-enhanced-737902

#Opening print statement gives the user a general idea of what the program will be about.
print("Hello! Welcome to the Music Playlist Generator")
#This input should be a string containing the music genre
musicGenre = input("What is your favorite music genre? :")
#This input should be a number containing the num of songs in the playlist only integers.
musicCount = int(input("What is the number of songs you want in your playlist? :"))
#This input should be a number containing the num of minutes in the total playlist only integers
musicDuration = int(input("What will the duration of the playlist be in minutes? :"))
#This calculates the average from the songs played and makes sure that it only displays the minutes,only integers.
musicAverage = int(musicDuration / musicCount)
#This print is using f string allows for multiple variables to be placed in the same line making it easier to output all variables.
print(f"Hello, your personalized {musicGenre} playlist will have {musicCount} songs, each with an average duration of {musicAverage} minutes.\nWith an overall playlist time of {musicDuration}")