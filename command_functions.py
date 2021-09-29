import pyfiglet
import random

DIFFICULTIES = {
    "easy": {"range": (0, 10), "points": 10, "deduct": 1},
    "normal": {"range": (0, 25), "points": 25, "deduct": 3},
    "hard": {"range": (0, 50), "points": 50, "deduct": 5},
    "insane": {"range": (0, 100), "points": 100, "deduct": 8},
}
fancytext = pyfiglet.figlet_format

# def point_deduct(var, difficulty):
#     return (var + difficulty.get('points')) - difficulty.get('deduct') if var == 0 else var - difficulty.get('deduct')

def point_deduct(var, difficulty):
    return var - difficulty.get('deduct')
def verify_difficulty(difficulty_name):
    if difficulty_name not in DIFFICULTIES:
        print(fancytext("Invalid difficulty"))
        print(
            f"`{difficulty_name}` doesn't match the name of any difficulty. Please enter `info:difficulty` for more info."
        )
        return
    return True


class CommandFunctions:
    def help_command(self, input_text):
        for key in self.command_list:
            print(key)
            print(f'    - {self.get(key, "desc")}')

    def start(self, input_text):
        selected_difficulty = "normal"
        if ":" in input_text:
            splitted_input_text = input_text.split(":")
            selected_difficulty = splitted_input_text[1]
        else:
            print(fancytext("Select Difficulty"))
            selected_difficulty = input("Difficulty ==) ")
        if not verify_difficulty(selected_difficulty):
            return

        selected_difficulty = DIFFICULTIES[selected_difficulty]
        game_round = 0
        guess_number = random.randint(*selected_difficulty.get('range'))
        status = 200
        chances = 3
        won = 0
        protection = True
        points = 0
        while game_round >= 10 or status != 500:
            round_points = 0
            if chances <= 0:
                game_round += 1
                chances = 3
                points = points + round_points

                print(
                    fancytext(f'Round complete! Total points: {points}')
                )
            game_input = input(f'[{chances} chances left] Guess: ')
            try: game_input = int(game_input)
            except ValueError:
                if game_input in ('cancel', 'hint'):
                    if game_input == 'cancel':
                        break
                    else:
                        print('HINT FEATURE IS COMING SOON')
                else:
                    if protection:
                        print("Why are you trying to waste your chances? This is your last warning.")
                        protection = False
                    else:
                        print('Wrong guess.')
                        chances -= 1
                        round_points = point_deduct(round_points, selected_difficulty)

            if game_input == guess_number:
                print(
                    'Correct guess!'
                )
                points = points + round_points + selected_difficulty['points']
                game_round += 1
                chances = 3
                print(
                    fancytext(f'Round complete! Total points: {points}')
                )
            else:
                print('Wrong guess.')
                chances -= 1
                points = points + point_deduct(round_points, selected_difficulty)
                print(points)
    def info(self, input_text):
        print("Called the info funtion!")

    def exit_command(self, input_text):
        exit()
