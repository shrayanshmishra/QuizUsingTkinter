  # our imports
from tkinter import Tk, Frame, Label, Button

# our questions data
data = {
  "question": [
    "Q1. What Indian city is the capital of two states?",
    "Q2. Which city is the capital of India?",
    "Q3. Smallest State of India?",
    "Q4. Where is Taj Mahal Located?"
  ],
  "answer": [
    "A",
    "B",
    "C",
    "B",
  ],
  "options": [

    ["Chandigarh",
      "Kolkata",
      "Delhi",
      "Banglore"
    ],
    ["Jaipur",
      "Delhi",
      "Chennai",
      "Mumbai"
    ],
    ["Rajasthan",
      "Punjab",
      "Goa",
      "Bihar"
    ],
    ["Lucknow",
      "Agra",
      "Bhopal",
      "Delhi"
    ]
  ]
}

# create question class
class Question:
    # initilize  the class
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    # to check if the answer is right or wrong
    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Right!")
            right += 1
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

# func to display question
def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

ques = data["question"]
answers = data["options"]
correct = data["answer"]

# adding question objects to list
questions = []
for i in range(len(ques)):
    new = Question(ques[i], answers[i],correct[i])
    questions.append(new)
    
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
button = Button(window, text="Start", command=askQuestion)
button.pack()
window.mainloop()