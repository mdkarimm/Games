from tkinter import *
from tkinter import simpledialog, messagebox

main = Tk()
main.title("Quiz on Pakistan")
main.geometry("600x400")


questions = [
    "What is the capital of Pakistan?",
    "Which river is the longest in Pakistan?",
    "What is the national language of Pakistan?",
    "Who was the founder of Pakistan?",
    "Which city is known as the 'City of Lights'?",
    "What is the national sport of Pakistan?",
    "Which mountain range runs through northern Pakistan?",
    "Who was the first female Prime Minister of Pakistan?",
    "In which year did Pakistan gain independence?",
    "Which Pakistani city is famous for its historical site, Mohenjo-Daro?",
    "What is the name of the largest mosque in Pakistan?",
    "Which Pakistani cricketer is known as 'Boom Boom'?",
    "Which Pakistani city is known for its beautiful beaches along the Arabian Sea?",
    "What is the currency of Pakistan?",
    "Which Pakistani singer is famous for his song 'Dil Dil Pakistan'?",
    "What is the name of the largest province by area in Pakistan?",
    "Which Pakistani city is famous for its annual Shandur Polo Festival?",
    "What is the name of the famous monument located in Islamabad, Pakistan?",
    "Which Pakistani actress won the Lux Style Award for Best Actress in 2019?",
    "Which Pakistani university is ranked among the top universities in Asia?"
]

answers = [
    "Islamabad",
    "Indus",
    "Urdu",
    "Jinnah",
    "Karachi",
    "Hockey",
    "Himalayas",
    "Benazir Bhutto",
    "1947",
    "Sindh",
    "Faisal Mosque",
    "Shahid Afridi",
    "Karachi",
    "Rupee",
    "Nazir Ahmed",
    "Balochistan",
    "Chitral",
    "Pakistan Monument",
    "Sajal Aly",
    "LUMS"
]

score = 0
current_question = 0

def ask_question():
    global current_question
    if current_question < len(questions):
        user_answer = simpledialog.askstring("Quiz", questions[current_question])
        if user_answer and user_answer.strip().lower() == answers[current_question].lower():
            messagebox.showinfo("Result", "Correct!")
            global score
            score += 1
        else:
            messagebox.showinfo("Result", f"Wrong! The correct answer was {answers[current_question]}")
        current_question += 1
        if current_question < len(questions):
            ask_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is {score}/{len(questions)}")
            main.quit()
    else:
        main.quit()


start_button = Button(main, text="Start Quiz", command=ask_question, font=("Helvetica", 16))
start_button.pack(pady=20)


main.mainloop()
