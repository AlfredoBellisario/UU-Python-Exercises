from .die import Die

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        
        matches_counter = 0
        wins = 0
        loses = 0
        
        while True:
            runner = cls()

            print("Round {}\n".format(matches_counter))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins += 1
                matches_counter += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                loses += 1
                matches_counter += 1
            print("Wins: {} Loses {}".format(wins, loses))            

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y':
                continue
            if prompt == 'n':
                print('Bye bye!')
                break
            else:
                print('No answer given. Terminating the game... bye!')
                break
