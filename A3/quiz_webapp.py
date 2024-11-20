from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def home():
    # Reset global variables when restarting the quiz
    global score, question_num, user_answers
    score = 0
    question_num = 0
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global question_num, score, user_answers

    if request.method == 'POST':
        # Capture the user’s selected answer
        user_answer = request.form.get("options", "").strip().lower() if request.form.get("options") else "" # "answer" matches the name in the HTML form
        correct_answer = question_list[question_num - 1][1]["answer"]

        print(f"User Answer: {user_answer}")

        
        
        # Check if the answer is correct and update the score
        if user_answer and user_answer == correct_answer:
            score += 1
            print(f"Correct! Updated Score: {score}")
        else:
            print(f"Incorrect. Score Remains: {score}")


        # Move to the next question or go to results if done
        question_num += 1
        if question_num >= len(question_list): #I asked chatgpt how to fix a IndexError: list index out of range
            return redirect(url_for('result', score=score, total_questions=len(question_list)))

    # Load the current question and options
    current_question = question_list[question_num]
    question = current_question[0]
    options = current_question[1]["options"]

    return render_template('quiz.html', question=question, options=options)

@app.route('/result') 
def result():
    global score
    score = int(request.args.get('score', 0)) # I asked chatgpt how to fix the result route causing the score to not be kept
    user_answers = request.args.get('user_answers')
    total_questions = int(request.args.get('total_questions', 0))
    return render_template('result.html', score=score, total_questions=total_questions, user_answers=user_answers)

# Load questions from a JSON file
with open("questions.json") as question_file:
    questions = json.load(question_file)
question_list = list(questions.items())

# Initialize housekeeping variables
score = 0
question_num = 0

if __name__ == "__main__":
    app.run(debug=True)
