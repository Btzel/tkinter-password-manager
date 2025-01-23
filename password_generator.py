letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random

class PasswordGenerator:
    def __init__(self,nr_letters,nr_numbers,nr_symbols):
        self.nr_letters = nr_letters
        self.nr_numbers = nr_numbers
        self.nr_symbols = nr_symbols

    def generate_password(self):
        password_letters = [random.choice(letters) for _ in range(self.nr_letters)]
        password_numbers = [random.choice(numbers) for _ in range(self.nr_numbers)]
        password_symbols = [random.choice(symbols) for _ in range(self.nr_symbols)]
        password_list = password_letters + password_numbers + password_symbols
        random.shuffle(password_list)
        password = ''.join(password_list)
        return password






















