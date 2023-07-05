from InputValidator import InputValidator 

class Main:
    def __init__(self):
        self.run()

    def run(self):
        # Getting input from the user
        user_input = input("Enter a domain name or email address: ")

        # Creating an instance of InputValidator and validating the input
        validator = InputValidator(user_input)
        validator.validate_input()


# Creating an instance of the Main class to run the program
main = Main()