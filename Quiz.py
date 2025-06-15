# --- Quiz Project ---

# TODO: Create 5 quiz questions with prompts and answers
questions = [
    {"prompt": "Question 1 goes here...\n", "answer": "answer1"},
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
    
    # TODO: Check if the user's answer is correct
    
    # TODO: Provide feedback (correct/incorrect) — optional

# Show final score
print(f"You got {score} out of {len(questions)} correct!") 