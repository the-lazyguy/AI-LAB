import random

data = [
    {"name": "Neymar", "description": "Footballer", "followers": 210},
    {"name": "Khloé Kardashian", "description": "Reality TV personality", "followers": 310},
    {"name": "Real Madrid CF", "description": "Football club", "followers": 130},
    {"name": "9GAG", "description": "Social media platform", "followers": 60},
    {"name": "Cristiano Ronaldo", "description": "Footballer", "followers": 600},
    {"name": "Instagram", "description": "Social media platform", "followers": 650},
    {"name": "YouTube", "description": "Video platform", "followers": 450},
    {"name": "National Geographic", "description": "Magazine", "followers": 280},
]


def higher_lower_game():
    score = 0
    game_on = True

    while game_on:
        item1, item2 = random.sample(data, 2)

        print("Compare the following two items:")
        print(f"1. {item1['name']}: {item1['description']} with {item1['followers']} followers")
        print(f"2. {item2['name']}: {item2['description']} with {item2['followers']} followers")

        user_guess = input("Which one has more followers? (Enter 1 or 2): ")

        if (user_guess == "1" and item1['followers'] > item2['followers']) or (
                user_guess == "2" and item2['followers'] > item1['followers']):
            score += 1
            print("Correct! Your score is now:", score)
        else:
            print("Wrong guess! The game is over.")
            print("Your final score is:", score)
            game_on = False


higher_lower_game()
