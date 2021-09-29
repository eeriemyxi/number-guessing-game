from commands import Commands


class Game(Commands):
    def __init__(self):
        super().__init__()

    def main_menu(self):
        while True:
            user_input = input("==) ").lower().strip(" ")
            command_name = user_input
            if ':' in user_input:
                command_name = user_input.split(':')[0]
            if (instance := self.get(command_name, 'instance')) != KeyError:
                instance(input_text=user_input)
            else:
                print("That command doesn't exist.")
