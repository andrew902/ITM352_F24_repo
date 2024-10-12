# Interactive quiz game where each question has four possible answers

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr": ["12","11","8","14"],
    "What is the capital of Texas": ["Austin", "San Antonio", "Dallas", "Houston"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Rembrand", "Picasso", "Michealangelo"]
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives [0]
    for alternative in sorted (alternatives):
        print(f" - {alternative}")
    answer = input(f"{question}? ")

    if answer == correct_answer:
            print("Correct!")
    else:
            print(f"The correct answer is {correct_answer!r}, not (answer!r)")