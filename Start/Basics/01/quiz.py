# The Quiz and Question classes define a particular quiz



class Question: # Base class for all questions in the quiz 
    def __init__(self): # Constructor for the Question class 
        # TODO: define the Question fields , todo: is a comment that is used to mark the location of a task in the code
        pass


class QuestionTF(Question): # True/False question class 
    def __init__(self): # Constructor for the QuestionTF class
        super().__init__() # Call the constructor of the base class 

    # TODO: define the ask method
    def ask(self): # Method to ask the question  
        while (True): # Loop to keep asking the question until a valid response is given
            print(f"(T)rue or (F)alse: {self.text}") # Print the question to the console 
            response = input("? ") # Get the response from the user  
 
            # TODO: Check to see if no response was entered

            # TODO: Check to see if either T or F was given

            # TODO: mark this question as correct if answered correctly

            break


class QuestioncMC(Question): # Multiple choice question class
    def __init__(self):
        super().__init__()
        # TODO: define the answers for this question

    # TODO: define the ask method
    def ask(self): # Method to ask the question  
        while (True): # Loop to keep asking the question until a valid response is given 
            # TODO: Present the question and possible answers

            response = input("? ") # Get the response from the user 

            # TODO: Check to see if no response was entered

            # TODO: mark this question as correct if answered correctly

            break


class Answer: # Answer class 
    def __init__(self): # Constructor for the Answer class
        pass
        # TODO: define the Answer fields


# if __name__ == "__main__":
#     q1 = QuestionTF()
#     q1.text = "Broccoli is good for you"
#     q1.points = 5
#     q1.correct_answer = "t"
#     q1.ask()
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
#     q2.ask()

#     print(q1.is_correct)
#     print(q2.is_correct)
