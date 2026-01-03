from transformers import pipeline

print("===================================")
print("     AI INTERNSHIP HELP BOT")
print("===================================")
print("Please wait... loading the model\n")

# load model
model = pipeline("question-answering")

print("Bot is ready!")
print("Ask anything about the internship.")
print("Type 'exit' to stop.\n")

info = """
This AI internship is designed for beginners.
It teaches Python, machine learning basics and NLP concepts.
The internship duration is 6 weeks.
Students will receive certificate after completion.
Mentors guide students during the internship.
"""

qno = 1

while True:
    ques = input("Question " + str(qno) + ": ")

    if ques.lower() == "exit":
        print("Thank you for using Internship Help Bot.")
        break

    result = model(question=ques, context=info)

    print("Answer:", result["answer"])
    print()

    qno += 1
