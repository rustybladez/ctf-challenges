import subprocess
import string

# Configuration
TESTBENCH_FILE = "EzLogic_tb.v"
OUTPUT_SIM = "EzLogic_tb.vvp"
FLAG_PREFIX = "0ops{"
FLAG_SUFFIX = "}"
FLAG_MIDDLE_LENGTH = 42 - len(FLAG_PREFIX) - len(FLAG_SUFFIX)  # Length of middle part
CHARSET = string.printable  # Includes all printable characters (letters, digits, symbols, etc.)

# Function to modify the flag in the testbench
def update_flag_in_testbench(flag):
    with open(TESTBENCH_FILE, "r") as f:
        lines = f.readlines()

    # Find and replace the FLAG_TO_TEST line
    for i in range(len(lines)):
        if "parameter FLAG_TO_TEST" in lines[i]:
            # Replace the line with the properly formatted flag
            lines[i] = f'    parameter FLAG_TO_TEST = "{flag}";\n'
            break

    # Write the updated content back to the file
    with open(TESTBENCH_FILE, "w") as f:
        f.writelines(lines)

    # Debugging: Print the updated parameter
    print(f"Updated FLAG_TO_TEST: {flag}")

# Function to compile the testbench
def compile_testbench():
    subprocess.run(
        [
            "iverilog",
            "-s", "EzLogic_tb",
            "-o", OUTPUT_SIM,
            "EzLogic_tb.v",
            "EzLogic_top_synth.v",
            "BUFG.v", "CARRY4.v", "FDCE.v", "GND.v",
            "IBUF.v", "LUT1.v", "LUT2.v", "MUXF7.v", "MUXF8.v", "OBUF.v", "VCC.v"
        ],
        check=True
    )

# Function to run the simulation
def run_simulation():
    result = subprocess.run(["vvp", OUTPUT_SIM], capture_output=True, text=True)
    return "Great! You've found the correct flag!" in result.stdout

# Brute-force loop
def brute_force_flag():
    import itertools

    print("Starting brute-force...")
    for middle_tuple in itertools.product(CHARSET, repeat=FLAG_MIDDLE_LENGTH):
        middle_part = "".join(middle_tuple)
        flag = FLAG_PREFIX + middle_part + FLAG_SUFFIX
        print(f"Testing flag: {flag}", end="\r")

        # Update the flag in the testbench
        update_flag_in_testbench(flag)

        try:
            # Compile the testbench
            compile_testbench()

            # Run the simulation
            if run_simulation():
                print(f"\nFlag found: {flag}")
                return flag
        except subprocess.CalledProcessError as e:
            print(f"\nCompilation failed for flag: {flag}")
            continue

    print("\nNo valid flag found.")
    return None

if __name__ == "__main__":
    brute_force_flag()
