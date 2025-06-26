# --- Quiz Project ---


# TODO: Create 5 quiz questions with prompts and answers
questions = [
   {"prompt": "What is 5*6?\n", "answer": "30"},
   {"prompt": "What is this programming language?\n", "answer": "python"},
   {"prompt": "What is a popular handheld gaming console with an iconic red-blue-black scheme?\n", "answer": "nintendo switch"},
   {"prompt": "What is the national bird of the U.S.?\n", "answer": "bald eagle"},
   {"prompt": "What do you get when you combine flour and eggs?\n", "answer": "pasta"},
   # Example format:
   # {"prompt": "What is 2 + 2?", "answer": "4"},
   # {"prompt": "Capital of France?", "answer": "Paris"}
]


# Initialize score
score = 0


# Loop through each question
for q in questions:
   # Ask the user the question
   user_input = input(q["prompt"] + "Your answer: ").strip().lower()


   # TODO: Handle blank input
   while user_input.strip() == "":
       user_input = input("You must enter an answer: ").strip().lower()




   # TODO: Check if the user's answer is correct
  
   if user_input == q["answer"].lower():
       score += 1
       print(f"correct!")
   else:
       print(f"incorrect")
  
 
# Show final score
print(f"You got {score} out of {len(questions)} correct!")

