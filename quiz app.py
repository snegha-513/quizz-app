import tkinter as tk
from tkinter import messagebox

questions = [
 {
  "question": "What does AI stand for?",
  "options": ["Artificial Intelligence", "Automated Info", "Advanced Internet", "None"],
  "answer": "Artificial Intelligence"
 },
 {
  "question": "Which library is used for data analysis?",
  "options": ["NumPy", "Pandas", "Matplotlib", "All of the above"],
  "answer": "All of the above"
 },
 {
  "question": "Which algorithm is used for classification?",
  "options": ["Linear Regression", "K-Means", "Decision Tree", "Apriori"],
  "answer": "Decision Tree"
 },
 {
  "question": "What is supervised learning?",
  "options": ["No data", "Unlabeled data", "Labeled data", "Random data"],
  "answer": "Labeled data"
 },
 {
  "question": "Which metric measures accuracy?",
  "options": ["Loss", "Precision", "Accuracy", "Recall"],
  "answer": "Accuracy"
 },
 {
  "question": "Which library is used for machine learning?",
  "options": ["Scikit-learn", "Flask", "Django", "Tkinter"],
  "answer": "Scikit-learn"
 },
 {
  "question": "What is overfitting?",
  "options": ["Good performance", "High bias", "Poor generalization", "Fast training"],
  "answer": "Poor generalization"
 },
 {
  "question": "Which is not a Python library?",
  "options": ["TensorFlow", "Keras", "React", "PyTorch"],
  "answer": "React"
 },
 {
  "question": "What is Big Data?",
  "options": ["Small data", "Structured data", "Large & complex data", "Only text"],
  "answer": "Large & complex data"
 },
 {
  "question": "Which technique reduces dimensions?",
  "options": ["PCA", "KNN", "Naive Bayes", "SVM"],
  "answer": "PCA"
 }
]


current_q = 0
score = 0

# ✅ FIRST create root window
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

# ✅ THEN create StringVar
selected_option = tk.StringVar()

def load_question():
    selected_option.set(None)
    q = questions[current_q]
    question_label.config(text=q["question"])
    for i in range(4):
        options[i].config(text=q["options"][i], value=q["options"][i])

def next_question():
    global current_q, score
    if selected_option.get() == questions[current_q]["answer"]:
        score += 1

    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        messagebox.showinfo("Result", f"Your Score: {score}/{len(questions)}")
        root.destroy()

question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=20)

options = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_option, font=("Arial", 12))
    rb.pack(anchor="w")
    options.append(rb)

next_btn = tk.Button(root, text="Next", command=next_question)
next_btn.pack(pady=20)

load_question()
root.mainloop()
