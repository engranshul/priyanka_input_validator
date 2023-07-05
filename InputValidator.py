class InputValidator:
    def __init__(self, input_string):
        self.input_string = input_string

    def validate_input(self):
        if isinstance(self.input_string, str) and not self.input_string.isdigit():
            if '@' in self.input_string:
                # Input is an email address
                result = "Input is an email address."
                print(result)
                return result;
                # Add your email validation logic here
                # You can use regular expressions or libraries like 'email-validator' to perform email validation
            else:
                # Input is a domain name
                result = "Input is a domain name." 
                print(result)
                return result;
                # Add your domain validation logic here
                # You can use libraries like 'tldextract' to extract the domain name components and perform validation
        else:
            # Invalid input
            result = "Invalid input." 
            print(result)
            return result;