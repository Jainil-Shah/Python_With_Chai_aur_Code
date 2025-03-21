import random

def game():
    print("Welcome to the game")
    score = random.randint(1, 100)
    
    with open ("chapter 9 - PS\\Hi-score.txt") as f:
        highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0
            
    print(f"Your score is {score}")
    print(f"High score is {highscore}")
    
    if score > highscore:
        with open("chapter 9 - PS\\Hi-score.txt", "w") as f:
            f.write(str(score))
            
    print("Thanks for playing")
    
    
game()