# File Creation
try:
    # Create a new text file in write mode
    with open("my_file.txt", 'w') as file:
        # Write three lines of text
        file.write("Hello Grace!\n")
        file.write("Registrarion number 12345\n")
        file.write("PLP Program\n")
        print("File created and initial content written successfully.")
except Exception as e:
    print(f"Error occurred while creating the file: {e}")

# File Reading and Display
try:
    # Open the file in read mode
    with open("my_file.txt", 'r') as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print(f"Error occurred while reading the file: {e}")

# File Appending
try:
    # Open the file in append mode
    with open("my_file.txt", 'a') as file:
        # Append three additional lines of text
        file.write("IST Program\n")
        file.write("Reg no 67890\n")
        file.write("NIST Framework\n")
    print("Additional content appended to my_file.txt.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print(f"Error occurred while appending to the file: {e}")

with open("my_file.txt", 'r') as file:
        # Read and display the contents of the appended file
        print("Contents of appended my_file.txt:")
        print(file.read())

