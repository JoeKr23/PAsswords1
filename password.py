import string
import random
from flask_scrypt import generate_password_hash, generate_random_salt, check_password_hash

## characters to generate password from
letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

class Passwords():
	def generate_random_password(letters_count: int,numbers_count: int,special_characters_count: int) -> int:

		## initialise the password
		password = []
		
		## pick random letters
		for i in range(letters_count):
			password.append(random.choice(letters))

		## pick random numbers
		for i in range(numbers_count):
			password.append(random.choice(numbers))

		## pick random special characters
		for i in range(special_characters_count):
			password.append(random.choice(special_characters))

		## shuffle the resultant password
		random.shuffle(password)

		## convert the list to string and return it
		return "".join(password)

	def salt_hash(password):
		salt = generate_random_salt()
		return [generate_password_hash(password,salt),salt]

	def verify_password(password,password_hash,salt):
		return check_password_hash(password,password_hash,salt)