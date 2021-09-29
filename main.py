from command_line import Game
import pyfiglet

CLI = Game()

# Startup
print(pyfiglet.figlet_format("Welcome", font = 'banner3-D'))
print(
    'This game is all about guessing numbers in different difficulties.\nTo check what changing difficulty would do to make it harder, enter "info:difficulty"\nNow you would ask me how do I start playing this game right? DW, I got you!\nTo play the game you either enter "start:[difficulty]" or only "start". It will ask you to enter the difficulty later if you enter only "start".'
)
print(
    'To check the other commands, you may enter "help" or "help:[command_name]" for more information about a specific command.'
)

# Command Line
CLI.main_menu()
