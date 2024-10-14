import random

QUESTIONS = {
    "What is the name of the character played by Leonardo Dicaprio in the movie Titanic": {
        "options": ["Jack Dawson", "Caledon Hockley", "Fabrizio De Rossi", "Jack the Ripper"],
        "correct_answer": "Jack Dawson",
        "hint": "He's a poor artist who wins a ticket aboard the Titanic at a lucky hand at poker...a very lucky hand."
    },
    "In the movie Your Name what is the town where Mitsuha lives called": {
        "options": ["Tokyo", "Kyoto", "Itomori", "Narita"],
        "correct_answer": "Itomori",
        "hint": "The town is fictional and doesn't exist in real life, unlike some of the other options."
    },
    "What is the name of the character played by Edward Norton in the movie Fight Club": {
        "options": ["Tyler Durden", "Joe Goldberg", "Patrick Bateman", "He doesn't have a name"],
        "correct_answer": "He doesn't have a name",
        "hint": "The character is referred to as 'The Narrator.'"
    },
    "What is the name of the character in the movie Superbad that buys the alcohol": {
        "options": ["Evan", "John", "Steve", "McLovin"],
        "correct_answer": "McLovin",
        "hint": "He has a fake ID with only one name that kind of sounds like he's trying to be an Irish R&B singer."
    },
    "Who directed the movies Avatar, Titanic, and The Terminator": {
        "options": ["James Cameron", "Steven Spielberg", "Quentin Tarantino", "Martin Scorsese"],
        "correct_answer": "James Cameron",
        "hint": "He is known for groundbreaking visual effects and directed the 1st, 3rd, and 4th highest grossing movies of all time."
    },
    "What actress played Adam Sandler's love interest in 50 First Dates": {
        "options": ["Drew Barrymore", "Jennifer Aniston", "Salma Hayek", "Jessica Alba"],
        "correct_answer": "Drew Barrymore",
        "hint": "She was a child actor and was also in the movie Blended with Adam Sandler."
    }
}

import json

# Specify the name of the JSON file
filename = "myquiz2.0.json"

# Open the file in write mode and save the dictionary as JSON
with open(filename, "w") as DictFile:
    json.dump(QUESTIONS, DictFile, indent=4)

    print(f"Data has been written to {filename}")


letters = ['a', 'b', 'c', 'd']
score = 0

for question, details in QUESTIONS.items():
    alternatives = details["options"]
    correct_answer = details["correct_answer"]
    hint = details["hint"]
    
    # Display the question and answer choices
    print(question)
    for label, alternative in zip(letters, alternatives):
        print(f"{label}: {alternative}")
    
    # Ask the user if they want a hint after showing the question and options
    use_hint = input("Would you like a hint for this question? (yes or no): ").lower()
    if use_hint == 'yes':
        print(f"Hint: {hint}\n")
    
    # Get the user's answer
    while True:
        answer_label = input("Your answer? (Choose a, b, c, or d): ").lower()
        if answer_label in letters:
            answer_index = letters.index(answer_label)
            answer = alternatives[answer_index]
            break
        else:
            print("Invalid input. Please choose a valid option (a, b, c, or d).")
    
    # Check if the answer is correct
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_answer!r}, not {answer!r}")
    
    print("\n" + "-" * 50 + "\n")  # Separator between questions

# Display final score
print(f"Quiz complete! You got {score} out of {len(QUESTIONS)} correct.")

# Write the score to a file
with open("score_history.txt", "a") as file:
    file.write(f"Score: {score}/{len(QUESTIONS)}\n")

print("Your score has been recorded.")

