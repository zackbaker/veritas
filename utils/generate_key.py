from cryptography import fernet

def generate_encryption_key():
    key = fernet.Fernet.generate_key()
    print(f'Set variable VERITASDB_ENCRYPTION_KEY in .env to: {key.decode()}')

if __name__ == '__main__':
    generate_encryption_key()
