import pyfiglet
import random

DIFFICULTIES = {
    "easy": {"range": (0, 10), "points": 10, "deduct": 1},
    "normal": {"range": (0, 25), "points": 25, "deduct": 3},
    "hard": {"range": (0, 50), "points": 50, "deduct": 5},
    "insane": {"range": (0, 100), "points": 100, "deduct": 8},
}
fancytext = pyfiglet.figlet_format


def get_hint(number, difficulty):
    max_points = difficulty.get("points")
    random_number = random.randint(2, difficulty.get("points"))
    if number >= random_number:
        return "The number you have to guess is greater than or equal to {} and less than {}".format(
            random_number, max_points
        )
    elif number <= random_number:
        return "The number you have to guess is less than or equal to {}".format(
            random_number
        )


def point_deduct(var, difficulty):
    return var - difficulty.get("deduct")


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
        wrong_guesses = 0
        guess_number = random.randint(*selected_difficulty.get("range"))
        chances = 3
        hints = 3
        won = 0
        protection = True
        points = 0
        round_points = 0
        while True:
            if game_round >= 10:
                print(fancytext("Game complete."))
                print(
                    fancytext(
                        "Total points:\n(  {won} x {max_points_per_round}  ) - (  {deduct} x {wrong_guesses}  )\n= {sum}".format(
                            won=won,
                            max_points_per_round=selected_difficulty.get("points"),
                            deduct=selected_difficulty.get("deduct"),
                            wrong_guesses=wrong_guesses,
                            sum=points,
                        )
                    )
                )
                break
            if chances <= 0:
                game_round += 1
                chances = 3
                points = points + round_points
                round_points = 0
                print(fancytext(f"Round complete! Total points: {points}"))
            game_input = input(f"[{chances} chances and {hints} hints left] Guess: ")
            try:
                game_input = int(game_input)
            except ValueError:
                if game_input in ("cancel", "hint"):
                    if game_input == "cancel":
                        break
                    else:
                        if hints > 0:
                            print(get_hint(guess_number, selected_difficulty))
                            hints -= 1
                        else:
                            print("You have already wasted all your hints.")
                else:
                    if protection:
                        print(
                            "Why are you trying to waste your chances? This is your last warning."
                        )
                        protection = False
                    else:
                        print("Wrong guess.")
                        chances -= 1
                        wrong_guesses += 1
                        round_points = point_deduct(round_points, selected_difficulty)
            else:
                if game_input == guess_number:
                    print("Correct guess!")
                    points = points + round_points + selected_difficulty["points"]
                    game_round += 1
                    chances = 3
                    round_points = 0
                    won += 1
                    print(fancytext(f"Round complete! Total points: {points}"))
                else:
                    print("Wrong guess.")
                    chances -= 1
                    wrong_guesses += 1
                    points += point_deduct(round_points, selected_difficulty)

    def info(self, input_text):
        if ":" not in input_text:
            print("Missing key name. Enter `help` for more info.")
            return
        key_name = input_text.split(":")[1]
        keys = ("difficulty")
        if key_name not in keys:
            print("Invalid key name. Enter `help` for more info.")
            return
        if key_name == "difficulty":
            for difficulty in DIFFICULTIES:
                difficulty_obj = DIFFICULTIES[difficulty]
                print(fancytext(difficulty.title()))
                print("-" * 30)
                print(
                    "The number to guess ranges from {range_1} to {range_2}. You get {max_points} points per round. {deduct} points will be deducted if you fail to guess the number.".format(
                        range_1=difficulty_obj.get("range")[0],
                        range_2=difficulty_obj.get("range")[1],
                        max_points=difficulty_obj.get("points"),
                        deduct=difficulty_obj.get("deduct"),
                    )
                )

    def exit_command(self, input_text):
        exit()
