import bcrypt

passord = "passord123".encode('utf-8')
hashed = bcrypt.hashpw(passord, bcrypt.gensalt())

print("Original password:", passord)
print("Hashed password:", hashed)

passordInput = input("Skriv inn passordet: ").encode('utf-8')
if bcrypt.checkpw(passordInput, hashed):
    print("Passordet stemmer!")
else:
    print("Feil passord!")