from InputValidator import InputValidator 

class Test:
    def __init__(self):
        self.run_tests()

    def run_tests(self):
        # Test cases
        test_cases = [
            ("example.com", "Input is a domain name."),
            ("1234", "Invalid input."),
            (1234, "Invalid input.")
        ]

        for input_string, expected_output in test_cases:
            validator = InputValidator(input_string)
            print(f"Testing input: {input_string}")
            actual_output = validator.validate_input()
            print(f"Expected output: {expected_output}")
            print(f"Actual output: {actual_output}")
            print("------------")
            assert actual_output == expected_output, "Test failed!"

# Creating an instance of the Test class to run the tests
test = Test()
