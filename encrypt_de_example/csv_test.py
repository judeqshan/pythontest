from cryptography.fernet import Fernet
import csv

# Generate a secret key
# key = Fernet.generate_key()
# print(key.decode())
key_raw = "9O3vI3CSc-BVruxGwCKZcC9tTSeqI4_-9Zx5NxjzDIQ="
key = key_raw.encode()
cipher_suite = Fernet(key)
# print(cipher_suite)

# # Read the CSV data from a file
# with open('input_data.csv', 'r', newline='') as file:
#     csv_reader = csv.reader(file)
#     csv_data = [row for row in csv_reader]

# # Convert the CSV data to a string
# csv_str = '\n'.join([','.join(row) for row in csv_data])

# # Encrypt the CSV data
# encrypted_data = cipher_suite.encrypt(csv_str.encode())

# # Store the encrypted data in a file
# with open('encrypted_data.bin', 'wb') as file:
#     file.write(encrypted_data)

# Decrypt the data when needed
with open('encrypted_data.bin', 'rb') as file:
    encrypted_data = file.read()
decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
decrypted_csv_data = [row.split(',') for row in decrypted_data.split('\n')]

# Use the decrypted CSV data
print(decrypted_csv_data)