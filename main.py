print("Welcome to this little game!")
print("\nThe principle is very simple, you will have multiple choice questions and you must find the right answer!")

score = 0

questions = [
    ("What is the average distance between the Earth and the Sun?" , ["93 million miles", "150 million kilometers", "250 million miles", "300 million kilometers"], "150 million kilometers"),
    ("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
    ("How many planets in our solar system have rings?", ["1", "2", "3", "4"], "4"),
    ("What is the main component of the air we breathe?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"], "Nitrogen"),
    ("What is the longest river in the world?", ["Nile", "Amazon", "Yangtze", "Mississippi"], "Amazon"),
    ("What is the greatest raptor in the world?", ["Golden Eagle", "Peregrine Falcon", "Griffon Vulture", "Condor of the Andes"], "Condor of the Andes"),
    ("What is the smallest country in the world in terms of area?", ["Monaco", "Nauru", "San Marino", "Vatican"], "Vatican"),
    ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"], "Pacific Ocean"),
    ("What is the largest island in the world in area?", ["Australia", "Greenland", "Borneo", "Sumatra"], "Greenland"),
    ("What is the largest desert in the world?", ["Sahara Desert", "Gobi Desert", "Antarctica", "Atacama Desert"], "Antarctica")
]

for question_number, (question_text, choices, correct_answer) in enumerate(questions, start=1):
    print(f"Question {question_number}: {question_text}")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        user_answer = input("Your answer (enter the answer number): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(choices):
            user_answer_index = int(user_answer) - 1
            if choices[user_answer_index].lower() == correct_answer.lower():
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {correct_answer}\n")
            break
        else:
            print("Invalid input. Please enter a valid answer number.")

print(f"Quiz over! Your score is {score}/{len(questions)}.")
print("\nThank you for playing!")
