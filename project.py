"""
simple math quize python program do the following
- print a simple math quize
- if the user answers true his score increase by one else decrease
- if no answer is given socre is also decreased by one
- user can exit
- problems will be addition and multiplication only
"""

import sys
import os
import random
<<<<<<< HEAD
import cowsay
=======
>>>>>>> 4af84464792bf129ce13d4ddd81bb11720ddb087

right_answer = 0
score = 0


def main():
    state = 1
    score = 0
    while state == 1:
        left, op, right = Generate_Problem()
        print(f"Choose the answer of {left} {op} {right}  = ", end="")
        print(Generate_chocies(left, op, right))
        try:
            answer = int(input("your Choice: "))
            if Check_Answer(answer):
                os.system("clear")
                score += 1
<<<<<<< HEAD
                print(f"Right Answer👌🤩\n")
                os.system(f"cowsay -c tux -t {score}")
=======
                print(f"Score:{score}👌🤩\n")
>>>>>>> 4af84464792bf129ce13d4ddd81bb11720ddb087
                state = int(input(("1- Play again\n2- Exit\n")))
                os.system("clear")
            else:
                score -= 1
                os.system("clear")
<<<<<<< HEAD
                print("Wrong Answer")
                os.system(f"cowsay -c trex -t {score}")
=======
                print(f"Score:{score}☹️ ☹️\n")
>>>>>>> 4af84464792bf129ce13d4ddd81bb11720ddb087
                state = int(input(("1- Try again\n2- Exit\n")))
                os.system("clear")
        except ValueError:
            print("Invalid Answer")
            pass
        if state != 1:
<<<<<<< HEAD
            
            ccc = 'Your Final score is' + str(score) 
            os.system("cowsay -c stegosaurus -t Thank_You ")
            sys.exit()
=======
            sys.exit(f"Your final score is {score}\nThank you..👋")
>>>>>>> 4af84464792bf129ce13d4ddd81bb11720ddb087


def Generate_Problem():
    return (random.randint(0, 101),
            random.choice(["+", "*"]),
            random.randint(0, 101))


def Generate_chocies(left, op, right):
    global right_answer
    right_answer = left + right if op == "+" else left * right
    choices = [
        right_answer,
        random.randint(0, 101) * random.randint(0, 101),
        random.randint(0, 101) + random.randint(0, 101),
    ]
    return random.sample(choices, len(choices))


def Check_Answer(answer):
    return True if answer == right_answer else False


if __name__ == "__main__":
    main()
