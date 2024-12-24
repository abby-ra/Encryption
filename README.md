# User Authentication System

This Python script provides a simple command-line interface for user authentication, including sign-up and sign-in functionalities. It uses custom encryption and hashing functions to secure passwords, and stores the data in a CSV file.

## Encryption and Hashing Functions

The program uses custom encryption and hashing functions to secure passwords before storing them.

### Functions

#### `encrypt(password, KEY)`

Encrypts the password using a custom encryption method with a key.

- **Parameters**:
  - `password` (str): The password to be encrypted.
  - `KEY` (str): The key used for encryption.

- **How it Works**:
  - Generates a list of all printable ASCII characters.
  - Creates a mapping of each character to its corresponding ASCII value.
  - Extends the key to match the length of the password.
  - Encrypts each character of the password using a combination of addition and subtraction of ASCII values, based on the character's position (even or odd).

#### `hash(password)`

Generates a hashed version of the password using a custom hashing method.

- **Parameters**:
  - `password` (str): The password to be hashed.

- **How it Works**:
  - Uses a list of alphanumeric characters for the hash.
  - Iterates through each character of the password.
  - Calculates a value based on the ASCII values of the characters.
  - Uses this value to select characters from the alphanumeric list to form the hashed password.

#### `generate_salt()`

Generates a random salt string to be used in hashing passwords.

- **Returns**:
  - `salt` (str): A random string of 10 printable ASCII characters.

#### `get_password(password, salt)`

Combines the encryption and hashing functions to produce a final hashed password that includes the salt.

- **Parameters**:
  - `password` (str): The password to be processed.
  - `salt` (str): The salt to be used in the process.

- **Returns**:
  - `hashed_password` (str): The final hashed password, including the salt.

- **How it Works**:
  - Encrypts the password using the provided salt as the key.
  - Hashes the encrypted password.
  - Hashes the salt.
  - Combines both hashed values to form the final stored password.

## Data Storage

The user credentials (username, hashed password, and salt) are stored in a CSV file named `data.csv`.

### Functions

#### `write_details(username, password)`

Writes the username, hashed password, and salt to the CSV file.

- **Parameters**:
  - `username` (str): The username to be stored.
  - `password` (str): The password to be stored.

- **How it Works**:
  - Generates a random salt using `generate_salt()`.
  - Processes the password using `get_password(password, salt)`.
  - Writes the username, processed password, and salt to `data.csv`.

#### `get_details(username)`

Retrieves the stored password and salt for a given username from the CSV file.

- **Parameters**:
  - `username` (str): The username to search for.

- **Returns**:
  - `[password, salt]` (list): The stored password and salt if found, otherwise `None`.
