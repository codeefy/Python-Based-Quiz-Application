# The Quiz and Question classes define a particular quiz


class Quiz:  # Base class for all quizzes in the system 
    def __init__(self): # Constructor for the Quiz class 
        #TODO: define the quiz properties
        pass  # Placeholder to avoid an error when the class is empty 

    def print_header(self): # Method to print the quiz header  
        print("\n\n*******************************************")  # it  is a comment that is used to mark the location of a task in the code
        #TODO: print the quiz header
        print("*******************************************\n")

    def print_results(self): # Method to print the quiz results
        print("*******************************************")
        
        print("*******************************************\n")

    def take_quiz(self):
        #TODO: initialize the quiz state

        #TODO: print the header

        #TODO: execute each question and record the result

        #TODO: return the results
        pass


class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while (True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            if (len(response) == 0):
                print("Sorry, that's not a valid response. Please try again")
                continue

            response = response.lower()
            if (response[0] != "t" and response[0] != "f"):
                print("Sorry, that's not a valid response. Please try again")
                continue

            if response[0] == self.correct_answer:
                self.is_correct = True

            break


class QuestioncMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
            print(self.text)
            for a in self.answers:
                print(f"{a.name}) {a.text}")

            response = input("? ")

            if (len(response) == 0):
                print("Sorry, that's not a valid response. Please try again")
                continue

            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True

            break


class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""


# if __name__ == "__main__":
#     qz = Quiz()
#     qz.name = "Sample Quiz"
#     qz.description = "This is a sample quiz!"

#     q1 = QuestionTF()
#     q1.text = "Broccoli is good for you"
#     q1.points = 5
#     q1.correct_answer = "t"
#     qz.questions.append(q1)

#     q2 = QuestioncMC()
#     q2.text = "What is 2+2?"
#     q2.points = 10
#     q2.correct_answer = "b"
#     ans = Answer()
#     ans.name = "a"
#     ans.text = "3"
#     q2.answers.append(ans)
#     ans = Answer()
#     ans.name = "b"
#     ans.text = "4"
#     q2.answers.append(ans)
#     ans = Answer()
#     ans.name = "c"
#     ans.text = "5"
#     q2.answers.append(ans)
#     qz.questions.append(q2)

#     qz.total_points = q1.points + q2.points
#     result = qz.take_quiz()
#     print(result)
