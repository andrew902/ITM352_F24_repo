from flask import Flask, render_template, request, redirect, url_for
import json
import random
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Reset global variables when restarting the quiz
    global score, question_num, user_answers, shuffled_questions, incorrect_answers
    score = 0
    question_num = 0
    incorrect_answers = 0  # Initialize the incorrect answers counter
    user_answers = []  # Resets user answers

    # Shuffle questions randomly
    # I asked chatgpt how to randomize the questions
    shuffled_questions = random.sample(question_list, len(question_list))  
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global question_num, score, user_answers, shuffled_questions, incorrect_answers

    feedback = None  # Initialize feedback variable

    if request.method == 'POST':
        # Capture the user’s selected answer
        user_answer = request.form.get("answer", "").strip() if request.form.get("answer") else "" # "answer" matches the name in the HTML form
        correct_answer = shuffled_questions[question_num][1]["answer"]

        print(f"User Answer: {user_answer}")

        # Check if the answer is correct and update the score
        # I asked chatgpt how to add live feedback
        if user_answer and user_answer == correct_answer:
            score += 1
            feedback = "Correct! 🥳"
            print(f"Correct! Updated Score: {score}")
        else:
            incorrect_answers += 1  # Increment incorrect answers counter
            feedback = f"Incorrect 😔. The correct answer was: {correct_answer}."
            print(f"Incorrect. Score Remains: {score}")

        # Store the user's answer for later review (if needed)
        user_answers.append(user_answer)

        # Move to the next question or go to results if done
        # I asked chatgpt how to use the time module and how to format it
        question_num += 1
        if question_num >= len(shuffled_questions):  # If all questions are answered
            # Capture the time when the quiz is completed
            quiz_completed_at = datetime.datetime.now().strftime("%I:%M:%S %p")
            return redirect(url_for('result', score=score, total_questions=len(shuffled_questions), user_answers=user_answers, quiz_completed_at=quiz_completed_at, incorrect_answers=incorrect_answers))

    # Load the current question and options (shuffled)
    current_question = shuffled_questions[question_num]
    question = current_question[0]
    options = current_question[1]["options"]

    # Randomize the answer options
    # I asked chatgpt how to radomize the questions and answers
    random.shuffle(options)

    # Pass feedback and score to the template
    return render_template('quiz.html', question=question, options=options, feedback=feedback, score=score)

@app.route('/result') 
def result():
    global score
    score = int(request.args.get('score', 0))  # Ensure score is passed correctly
    user_answers = request.args.get('user_answers')  # Retrieve user's answers
    total_questions = int(request.args.get('total_questions', 0))  # Get the total number of questions
    quiz_completed_at = request.args.get('quiz_completed_at')  # Retrieve the time the quiz was completed
    incorrect_answers = int(request.args.get('incorrect_answers', 0))  # Get the number of incorrect answers
    return render_template('result.html', score=score, total_questions=total_questions, user_answers=user_answers, quiz_completed_at=quiz_completed_at, incorrect_answers=incorrect_answers)

# Load questions from a JSON file
with open("questions.json") as question_file:
    questions = json.load(question_file)
question_list = list(questions.items())  # Convert questions into a list of tuples

# Initialize housekeeping variables
score = 0
question_num = 0
incorrect_answers = 0  # Initialize the incorrect answers counter

if __name__ == "__main__":
    app.run(debug=True)
