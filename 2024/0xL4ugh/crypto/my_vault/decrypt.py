import base64
import hashlib
from cryptography.fernet import Fernet
import pycountry

# Function to generate a key from the password
def generate_key(password):
    password_bytes = password.encode('utf-8')
    key = hashlib.sha256(password_bytes).digest()
    return base64.urlsafe_b64encode(key)

# Function to decrypt a file with a given password
def decrypt_file(encrypted_data, password):
    try:
        key = generate_key(password)
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')  # Return the plaintext
    except Exception:
        return None  # Return None if decryption fails

# Generate a list of all possible country names using pycountry
def get_country_list():
    countries = [country.name.lower().replace(" ", "") for country in pycountry.countries]

    # Add some common variations or abbreviations
    countries += [
        "usa", "uk", "uae", "korea", "southkorea", "northkorea", "ivorycoast",
        "czechia", "czechoslovakia", "vietnam", "venezuela", "bolivia", "ae",
        "saudi", "america", "ksa", "iran", "syria", "arabemirates", "palestine",
        "tanzania", "algeria", "bahrain", "mauritania", "sudan", "tunisia", "yemen",
        "morocco", "oman", "saudiarabia", "somalia", "comoros", "djibouti", "egypt",
        "iraq", "jordan", "kuwait", "lebanon", "libya", "turkey", "unitedstatesofamerica",
        "russia"
    ]
    return list(set(countries))  # Remove duplicates

# Brute-force decryption
def brute_force_decrypt(ciphertext_file, years, countries):
    with open(ciphertext_file, "rb") as file:
        encrypted_data = file.read()

    for year in years:
        for country in countries:
            password = year + country
            plaintext = decrypt_file(encrypted_data, password)
            if plaintext:
                print(f"[+] Decryption Successful for {ciphertext_file}!")
                print(f"Password: {password}")
                print(f"Decrypted Content:\n{plaintext}")
                return  # Stop after finding the correct password

    print(f"[-] Decryption Failed for {ciphertext_file}")

# Main function
def main():
    # Limit the year range (2000–2025)
    years = [str(year) for year in range(1900, 2026)]

    # Generate a full list of countries using pycountry
    countries = get_country_list()

    # Ciphertext files to decrypt
    ciphertext_files = ["encrypted_friend1.txt", "encrypted_friend2.txt", "encrypted_friend3.txt"]
    # ciphertext_files = ["encrypted_friend1.txt"]

    # Perform brute-force on each file
    for ciphertext_file in ciphertext_files:
        print(f"[*] Attempting to decrypt {ciphertext_file}...")
        brute_force_decrypt(ciphertext_file, years, countries)

if __name__ == "__main__":
    main()
