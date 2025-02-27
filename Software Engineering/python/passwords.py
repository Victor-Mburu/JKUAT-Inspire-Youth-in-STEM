import hashlib
import os

# File to store the passwords and site names
FILENAME = 'passwords.txt'

# Function to hash the password
def hash_password(password):
    """Hash a password for storing"""
    return (hashlib.sha256(password.encode()).hexdigest())

# Function to save the password
def save_password(site, password):
    """Save a password for a site"""
    hash_password = hash_password(password)
    with open(FILENAME, 'a') as file:
        file.write(f'{site} {hash_password}\n')
    print(f'Password for {site} saved successfully')

# Function to get the password
def get_password(site):
    """Retrieve a password for a site"""
    if not os.path.exists(FILENAME):
        print('No passwords saved yet')
        return
    with open(FILENAME, 'r') as f:
        for line in f:
            stored_site, stored_password, stored_hash = line.strip().split(" ")
            if stored_site == site:
                return stored_password
        print(f'No password saved for {site} ')
        return None
    
    def main():
        if not os.path.exists(FILENAME):
            with open(FILENAME, 'w') as f:
                pass # Create the file if it doesn't exist

        action = input( 'Enter "save" to save a password or "get" to retrieve a password: ')

        if action == 'save':
            site = input('Enter the site name: ')
            if site_exists(site): # type: ignore
                print('Site already exists')
                overwrite = input('Do you want to update the password? (y/n): ')
                if overwrite  != 'y':
                    print('Password not updated')
                    return
             
    
            import string
            import random
            # Generate a random password
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choices(characters, k=10))
            print(f'Generated password: {password}')
            save_password(site, password)
        elif action == 'get':
            site = input('Enter the site name: ')
            password = get_password(site)
            if password:
                print(f'The password for {site} is {password}')
        else:
            print('Invalid action')

    if __name__ == '__main__':
        main()

