class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def has_questions_remaining(self):
        return self.current_question_index < len(self.questions)

    def next_question(self):
        if self.has_questions_remaining():
            return self.questions[self.current_question_index]
        else:
            return None

    def check_answers(self):
        score = 0
        for question in self.questions:
          #  print(question.check_answer())
            if question.check_answer() == True:
                score += 2
            elif question.check_answer() == False:
                score -= 1
            else:
                score += 0
        return score

#main playing the quiz here

    def play(self):
        print("Welcome to the quiz!")
        print(f"Total questions = {len(self.questions)}, +2 for correct and -1 for wrong 0 for skipping")
        #Ready for the quiz or exit
        while True:
            user_choice = input("Enter 'R' for ready or 'E' for exit: ").strip().lower()
            
            if user_choice == 'e':
                print("Exiting the quiz.")
                return
            elif user_choice == 'r':
                break
            else:
                print("Invalid choice. Please enter 'R' to start or 'E' to exit.")

        print("Quiz Started")
        while self.has_questions_remaining():
            current_question = self.next_question()
            
            print(f"Q{self.current_question_index + 1}) {current_question.text}")
            user_choice = input("'T'=>true, 'F'=> false, 'N'=> next, 'P'=> prev,'S'=>submit: ").strip().lower()
            
            if user_choice == 's':
                score = self.check_answers()
                print(f"Quiz completed! Your final score is {score} points.")
                for i, question in enumerate(self.questions, start=1):
                    print(f"Q{i}: Marks Awarded: {2 if question.check_answer() else -1}")
                return
            elif user_choice == 't':
                current_question.user_answer = 'true'
                self.current_question_index += 1
            elif user_choice == 'f':
                current_question.user_answer = 'false'
                self.current_question_index += 1
            elif user_choice == 'n':
                if self.current_question_index == len(self.questions)-1 : 
                    print('nothing after')
                else:
                    self.current_question_index += 1
            elif user_choice == 'p':
                if self.current_question_index > 0:
                    self.current_question_index -= 1
                else:
                    print("You are at the first question.")
            else:
                print("Invalid choice. Please enter 'T', 'F', 'N', 'P', or 'S'.")
        #Quiz ended after Q12 evauation
        score = self.check_answers()
        print(f"Quiz completed! Your final score is {score} points.")
        #This is was for telling which Q were right and which were wrong
        for i, question in enumerate(self.questions, start=1):
                print(f"Q{i}: Marks Awarded: {2 if question.check_answer() else -1 if question.check_answer()==False else 0}")
        return
