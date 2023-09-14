class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number} has the category of: {current_question.category}, the question is: ")
        answer = input(f" {current_question.text} (True/False): ")
        self.check_answer(current_question.answer, answer)


    def still_has_questions(self):

        return self.question_number < len(self.question_list)
    

    def check_answer(self, question_answer, user_answer):

        if question_answer.lower() == user_answer.lower():
            self.score += 1
            print(f"Correct! Your score is now {self.score}/{self.question_number}")
        else:
            print(f"Incorrect! Your score is now {self.score}/{self.question_number}")
        print("")