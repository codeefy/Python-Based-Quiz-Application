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


class Question: # Base class for all questions in the quiz  
    def __init__(self): # Constructor for the Question class
        self.points = 0 # Points for the question 
        self.correct_answer = "" # Correct answer for the question 
        self.text = "" # Text of the question
        self.is_correct = False # Flag to indicate if the question was answered correctly


class QuestionTF(Question): # True/False question class 
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

    def ask(self): # Method to ask the question
        while (True): # Loop to keep asking the question until a valid response is given
            print(self.text) # Print the question to the console
            for a in self.answers: # Loop through the answers and print them to the console
                print(f"{a.name}) {a.text}") # Print the answer to the console

            response = input("? ") # Get the response from the user 

            if (len(response) == 0): # Check to see if no response was entered
                print("Sorry, that's not a valid response. Please try again") # Print an error message to the console
                continue # Skip the rest of the loop and start over 

            response = response.lower() # Convert the response to lowercase 
            if response[0] == self.correct_answer: # Check to see if the response is correct 
                self.is_correct = True # Mark the question as correct

            break # Exit the loop    


class Answer: # Answer class   
    def __init__(self): # Constructor for the Answer class
        self.text = "" # Text of the answer 
        self.name = "" # Name of the answer


if __name__ == "__main__":
    qz = Quiz()
    qz.name = "Sample Quiz"
    qz.description = "This is a sample quiz!"

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
