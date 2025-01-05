from pwn import *
import time

HOST = "challenge.ctf.games"
PORT = 32756

move_mapping = {
    "strike": "block",
    "block": "advance",
    "advance": "retreat",
    "retreat": "strike"
}

def play_game():
    try:
        conn = remote(HOST, PORT)
        log_file = open("game_log.txt", "w")  # Open a file to log the game output

        while True:
            try:
                line = conn.recvline(timeout=2).strip().decode()
                print(f"Received: {line}")
                log_file.write(f"Received: {line}\n")  # Log the output

                if "Opponent move:" in line:
                    opponent_move = line.split("Opponent move: ")[1]
                    print(f"Opponent move: {opponent_move}")
                    log_file.write(f"Opponent move: {opponent_move}\n")

                    if opponent_move in move_mapping:
                        my_move = move_mapping[opponent_move]
                        print(f"My move: {my_move}")
                        conn.sendline(my_move)
                        log_file.write(f"My move: {my_move}\n")
                    else:
                        print("Unknown move received. Exiting.")
                        break

                if "忍殺" in line:  # If the special line is received
                    print("Special message received. Waiting for flag.")
                    log_file.write("Special message received. Waiting for flag.\n")
                    time.sleep(0.5)  # Allow some time to receive any additional data

            except EOFError:
                print("Connection closed by the server.")
                log_file.write("Connection closed by the server.\n")
                break
            except Exception as e:
                print(f"Error: {e}")
                log_file.write(f"Error: {e}\n")
                break

    except Exception as e:
        print(f"Failed to connect or an error occurred: {e}")

    finally:
        log_file.close()  # Close the log file

if __name__ == "__main__":
    play_game()
