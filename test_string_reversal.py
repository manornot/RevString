import subprocess

def run_test(input_string):
    # Prepare the input
    input_text = f"{input_string}\n"
    # Expected output
    expected_output = f"Reversed: {input_string[::-1]}"
    # Run the compiled program, feeding it the input text
    process = subprocess.run(['./string_reversal'], input=input_text, capture_output=True, text=True, stdin=subprocess.PIPE)
    output = process.stdout.strip()
    # Assert to check if the actual output matches the expected reversed string
    assert expected_output in output, f"Test failed for input '{input_string}'. Expected '{expected_output}', got '{output}'"

def compile_program():
    # Compile the C program to a binary named 'string_reversal'
    compile_process = subprocess.run(['gcc', 'string_reversal.c', '-o', 'string_reversal'], capture_output=True, text=True)
    if compile_process.returncode != 0:
        print("Compilation failed.")
        print(compile_process.stderr)
        exit(1)

def main():
    compile_program()
    # Define a list of test strings
    test_strings = ["hello", "12345", "A man a plan a canal Panama", "", "racecar"]
    # Run tests for each string
    for test_string in test_strings:
        run_test(test_string)
    
    print("All tests passed successfully.")

if __name__ == "__main__":
    main()
