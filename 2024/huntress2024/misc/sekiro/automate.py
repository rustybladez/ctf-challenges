from pwn import *
import re
import time

# Connection details (replace with actual IP and port)
HOST = "challenge.ctf.games"
PORT = 32120

# Move mappings (to counter the opponent's move)
move_mapping = {
    "strike": "block",
    "block": "advance",
    "advance": "retreat",
    "retreat": "strike"
}

def play_game():
    try:
        # Connect to the server
        conn = remote(HOST, PORT)
        buffer = b''  # To store incoming data
        while True:
            try:
                # Read a chunk of data (you can adjust the size for efficiency)
                data = conn.recv(4096)
                if not data:
                    print("No more data. Connection might be closed.")
                    break

                # Append the data to the buffer
                buffer += data
                print(f"Data received: {data.decode(errors='ignore')}")

                # If the buffer contains "Opponent move:", extract and respond
                while b"Opponent move:" in buffer:
                    # Extract everything up to the next line with "Opponent move"
                    opponent_move_line, buffer = buffer.split(b'\n', 1)
                    decoded_line = opponent_move_line.decode(errors='ignore')
                    print(f"Received: {decoded_line.strip()}")

                    if "Opponent move:" in decoded_line:
                        # Extract the opponent's move
                        opponent_move = decoded_line.split("Opponent move: ")[1]
                        print(f"Opponent move: {opponent_move}")

                        # Get the counter-move
                        if opponent_move in move_mapping:
                            my_move = move_mapping[opponent_move]
                            print(f"My move: {my_move}")

                            # Send your move back to the server
                            conn.sendline(my_move)
                        else:
                            print("Unknown move received. Exiting.")
                            return

                # Check if we received the flag or any final message
                if b"flag{" in buffer.lower():
                    print(f"Flag found: {buffer.decode(errors='ignore')}")
                    break

                # Short delay to avoid overloading the server (optional)
                time.sleep(0.1)

            except EOFError:
                print("Connection closed by the server.")
                break
            except Exception as e:
                print(f"Error: {e}")
                break

    except Exception as e:
        print(f"Failed to connect or an error occurred: {e}")

if __name__ == "__main__":
    play_game()
