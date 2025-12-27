import re

# Function to handle internship related queries
def internship_chatbot(user_text):

    user_text = user_text.lower()

    # greeting
    if re.search("hi|hello|hey", user_text):
        return "Hello! How can I help you regarding the internship?"

    # about internship
    elif re.search("internship", user_text):
        return "We offer an AI internship focused on basic concepts and practical tasks."

    # duration
    elif re.search("duration|time|period", user_text):
        return "The internship duration is usually between 4 to 8 weeks."

    # eligibility
    elif re.search("eligibility|eligible|who can apply", user_text):
        return "Students from any background with basic programming knowledge can apply."

    # skills
    elif re.search("skills|required skills", user_text):
        return "Basic Python knowledge is enough to start this internship."

    # stipend
    elif re.search("stipend|paid|salary", user_text):
        return "This internship is mainly learning-based. Stipend details depend on performance."

    # mentor
    elif re.search("mentor|guidance|trainer", user_text):
        return "Yes, mentors are available to guide interns during the internship."

    # certificate
    elif re.search("certificate", user_text):
        return "A certificate will be provided after successful completion."

    # exit
    elif re.search("bye|exit|quit", user_text):
        return "Thank you for your interest. Goodbye!"

    # fallback
    else:
        return "Please ask questions related to the internship."

# start chat
print("Internship Enquiry Chatbot Started")
print("Ask me internship-related questions. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    reply = internship_chatbot(user_input)
    print("Bot:", reply)

    if user_input.lower() == "bye":
        break
