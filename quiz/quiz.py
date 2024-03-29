def show_menu():
    print("1. Ask Questions")
    print("2. Add a question")
    print("3. Exit Game")
    
    option = input("Enter Option: ")
    return option
    
def ask_questions():
    questions = []
    answers = []
    
    with open("Questions.txt", "r") as file:
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines):
        if i&2 == 0:
            questions.append(text)
        else
            answers.append(text)
            
    for questions, answer in zip(questions, answers):       

def add_question():
    print("")
    question = input("Enter a Question\n> ")
    
    print("")
    print("Okay then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()
    
def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You selected 'Ask Question'")
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid Option")
        print("")
        
game_loop()