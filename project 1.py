import tkinter as tkntr
import random

# Quiz data: questions, options, and correct answers
quiz_data = [
    {
        "question": "Which country has the largest population?",
        "options": ["United States", "China", "India", "Japan"],
        "answer": "India"
        },
    {
        "question": "What is 225 + 247?",
        "options": ["410", "472", "473", "413"],
        "answer": "472"
        },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
        },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
        },
    {
        "question": "Which of the following is not related to china?",
        "options": ["Beijing", "Temple of Heaven", "Summer Palace", "Mount Fuji"],
        "answer": "Mount Fuji"
        },
    {
        "question": "Which city is called the Financial Capital Of India?",
        "options": ["Mumbai", "Chennai", "Benguluru", "Delhi"],
        "answer": "Mumbai"
        },
     {
        "question": "Who is the current Prime Minister of India?",
        "options": ["Narendra Modi", "Droupadi Murmu", "Nirmala Seetharaman", "Rajnath Singh"],
        "answer": "Narendra Modi"
        },
     {
        "question": "What is the percentage of hindus all over the world?",
        "options": ["15%", "25%", "50%", "2%"],
        "answer": "15%"
        },
     {
        "question": "Which continent recieves the heaviest rainfall in the world?",
        "options": ["North America", "South America", "Africa", "India"],
        "answer": "Pacific"
        },
     {
        "question": "Which of the following spice is not grown in India?",
        "options": ["Turmuric", "Asafoetida(hing)", "Black pepper", "Cardamom"],
        "answer": "Asafoetida(hing)"
        },   
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("WELCOME TO MY QUIZ GAME.....HELLO")
        self.score = 0
        self.current_question_index = 0
        self.selected_answer = tkntr.StringVar()        
        # GUI setup
        self.question_label = tkntr.Label(root, text="", font=("calibri", 16), wraplength=500)
        self.question_label.pack(pady=20)        
        self.buttons_frame = tkntr.Frame(root)
        self.buttons_frame.pack(pady=20)        
        self.option_buttons = []
        for _ in range(4):
            button = tkntr.Radiobutton(self.buttons_frame, text="", variable=self.selected_answer, value="", font=("calibri", 14))
            button.pack(anchor="w")
            self.option_buttons.append(button)        
        self.next_button = tkntr.Button(root, text="Next", command=self.next_question, font=("calibri", 10))
        self.next_button.pack(pady=20)        
        self.score_label = tkntr.Label(root, text=f"Score: {self.score}", font=("calibri", 12))
        self.score_label.pack(pady=20)        
        self.load_question()    
    def load_question(self):
        if self.current_question_index < len(quiz_data):
            question_data = quiz_data[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            self.selected_answer.set(None)  # Deselect all options
            
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, value=option)
        else:
            self.end_quiz()
    
    def next_question(self):
        question_data = quiz_data[self.current_question_index]
        if self.selected_answer.get() == question_data["answer"]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        
        self.current_question_index += 1
        self.load_question()
    
    def end_quiz(self):
        self.question_label.config(text="Quiz Over!")
        for button in self.option_buttons:
            button.pack_forget()
        self.next_button.pack_forget()

# Main application
if __name__ == "__main__":
    root = tkntr.Tk()
    app = QuizGame(root)
    root.mainloop()
