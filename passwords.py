# Save this code as encrypt_password.py

from cryptography.fernet import Fernet

def encrypt_password(password):
    key = Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)
    fernet = Fernet(key)
    token = fernet.encrypt(password.encode())
    encrypted_password = token.decode()
    return encrypted_password

def decrypt_password(encrypted_password):
    with open('key.key', 'rb') as file:
        key = file.read()
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
    return decrypted_password

if __name__ == "__main__":
    password = "my_password"
    encrypted_password = encrypt_password(password)
    decrypted_password = decrypt_password(encrypted_password)
    print("Encrypted password:", encrypted_password)
    print("Decrypted password:", decrypted_password)