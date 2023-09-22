
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        self.user_answer = None

    def check_answer(self):
        if self.user_answer is None:
            return None
        return self.user_answer.lower() == self.answer.lower()
