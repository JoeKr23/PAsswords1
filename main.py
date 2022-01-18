from password import Passwords

_password = Passwords.generate_random_password(5,2,1)
[hashed_password,salt] = Passwords.salt_hash(_password)
print(Passwords.verify_password(_password,hashed_password,salt))
print(_password,hashed_password,salt)
