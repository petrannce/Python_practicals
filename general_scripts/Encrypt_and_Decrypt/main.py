from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Encryption Key:", key.decode())

# Create a Fernet cipher object with the key
cipher = Fernet(key)

# Example message to encrypt
message = "Hello, this is a secret message.".encode()

# Encrypt the message
encrypted = cipher.encrypt(message)
print("Encrypted string:", encrypted.decode())

# Decrypt the message
decrypted = cipher.decrypt(encrypted)
print("Decrypted string:", decrypted.decode())