from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample quiz data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', quiz_data=quiz_data)

@app.route('/submit', methods=['POST'])
def submit():
    total_questions = len(quiz_data)
    correct_answers = 0

    for i, question in enumerate(quiz_data):
        selected_answer = request.form.get(f'question-{i}')
        if selected_answer == question['answer']:
            correct_answers += 1

    score = (correct_answers / total_questions) * 100
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
