# ben-python-game-collection
This is a library containing python games that I have made which should be ran using my program.

## Installation Instructions:
1. Download the latest version of my program from [realses](https://github.com/BenSmulian/ben-python-game-collection/releases) that fits your software and hardware.
2. place the file in an **empty** folder
3. 
  - On Linux/Mac:
    1. open a terminal in the directory you have placed the newly dwonloaded file
    2. if -
       (for all options, change `your_file_name` to the exact name of the downloaded file without the extention afterwards)
      - logged in to a user, execute the fallowing command:
       ```sh
       sudo chmod +x "your_file_name.sh"
       ```, then type your user password.
      - logged in as root, execute the fallowing command:
       ```sh
       chmod +x "your_file_name.sh"
       ``` (without sudo)
    > Note that for Mac sudo is not needed anyways.
  - On Windows:
    1. double click the file and continue the execution every time windows tells you to stop it if it does.
4. Your all set! see below for more information regaurding installing games from this library

## Installing Games
once the program has run once, you can open a terminal, and from it, execute the program,
typing the exact name of the python file representing the game you want from the games folder in this repository (not including the .py extention)

## Running games
once the program has run once, if you don't provide it with any arguments, it will start the game menu (which are terminal options.)

from there, you can choose the game you'd like to play, or install games
(which is equivelent to the functionality of typing the game name when executing).

after selecting the game you'd like to play, it will ask you to confirm, which if you do, starts the python game in another terminal.

you can kill, stop, or close the opened terminal however you'd like, you can run multiple games at once, or multiple of the same game,
although not all games will allow for multi session.
