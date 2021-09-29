from command_functions import CommandFunctions


class Commands(CommandFunctions):
    def __init__(self):
        self.command_list = dict(
            help=dict(desc="Shows this message.", instance=self.help_command),
            start=dict(
                desc='Start playing this game. You can also enter "start:[DIFFICULTY]" to start the game without being asked for the difficulty again.',
                instance=self.start,
            ),
            info=dict(
                desc="Get information about stuff like, difficulty, etc.\n    Keys:\n         difficulty : Get information about different difficulties, their name, What they do to make it harder.",
                instance=self.info,
            ),
            exit=dict(desc="Quit the game.", instance=self.exit_command),
        )

    def get(self, key_name, sub_key):
        if key_name in self.command_list:
            return self.command_list.get(key_name)[sub_key]
        else:
            return KeyError
