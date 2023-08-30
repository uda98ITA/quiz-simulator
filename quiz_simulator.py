import random

# Define the questions, options, and correct answers
quiz_data = [
    {
        'question': 'Qual e principio stabilisce che le imposte devono essere pro- porzionali alle capacità contributive dei cittadini?',
        'options': ['Principio di legalità', 'Principio di progressività', 'Principio di capacità contributiva', 'Principio di uguaglianza'],
        'correct_answer': 'c'
    },
    {
        'question': 'Qual è l’agenzia governativa responsabile della riscossione delle imposte in Italia?',
        'options': ['Agenzia delle Entrate', 'Agenzia delle Imposte', 'Agenzia Fiscale Italiana', 'Agenzia di Riscossione'],
        'correct_answer': 'a'
    },
    {
        'question': 'In quale categoria rientra l’IVA?',
        'options': ['Imposta diretta', 'Imposta indiretta', 'Imposta patrimoniale', 'Imposta progressiva'],
        'correct_answer': 'b'
    },
    {
        'question': 'Chi è responsabile del pagamento dell’IVA?',
        'options': ["L’azienda che produce beni o offre servizi", 'Il consumatore finale', 'Il governo', 'L’Agenzia delle Entrate'],
        'correct_answer': 'b'
    },
    {
        'question': 'Cos’è l’evasione fiscale?',
        'options': ['Il pagamento delle tasse in ritardo', 'La dichiarazione accurata dei redditi', 'L’omissione dolosa del pagamento delle tasse', 'L’elusione fiscale legale'],
        'correct_answer': 'c'
    },
    {
        'question': 'In quale categoria rientra l’IRPEF (Imposta sul Reddito delle Persone Fisiche)?',
        'options': ['Imposta diretta', 'Imposta indiretta', 'Imposta progressiva', 'Imposta patrimoniale'],
        'correct_answer': 'a'
    },
    {
        'question': 'Quale principio stabilisce che i cittadini devono pagare le tasse in base ai loro mezzi finanziari?',
        'options': ['Principio di capacità contributiva', 'Principio di uguaglianza', 'Principio di legalità', 'Principio di solidarietà'],
        'correct_answer': 'c'
    },
    {
        'question': 'Qual è l’obbligo fondamentale del contribuente nei confronti dell’amministrazione fiscale?',
        'options': ['Pagare le tasse in ritardo', 'Presentare la dichiarazione dei redditi', 'Chiedere l’esonero fiscale', 'Investire in beni patrimoniali'],
        'correct_answer': 'b'
    },
    {
        'question': 'Cos’è l’elusione fiscale?',
        'options': ['Il pagamento delle tasse in ritardo', 'L’omissione dolosa del pagamento delle tasse', 'L’uso legale di strategie per ridurre l’imposta dovuta', 'L’omissione accidentale del pagamento delle tasse'],
        'correct_answer': 'c'
    },
    {
        'question': "Qual è l’aliquota standard dell’IVA in Italia?",
        'options': ['18%', '20%', '22%', '24%'],
        'correct_answer': 'c'
    }
]

# Randomly select 5 questions from the quiz_data list
selected_questions = random.sample(quiz_data, 5)

# Function to start the quiz
def start_quiz(questions):
    correct_answers = 0
    for i, question in enumerate(questions):
        print(f"Domanda {i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{chr(ord('a') + j)}. {option}")
        answer = input("La tua risposta (a/b/c/d): ")
        if answer == question['correct_answer']:
            correct_answers += 1
            print("Corretto!")
        else:
            print("Sbagliato.")
        print()
    print(f"Hai risposto correttamente a {correct_answers} domande su 5.")

# Start the quiz with the selected questions
start_quiz(selected_questions)
