from data import question_data as data
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def report(self):
        print(self.text)
        print(self.answer)
