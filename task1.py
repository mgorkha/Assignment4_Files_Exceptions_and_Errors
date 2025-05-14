
try:
    with open('sample.txt', 'r') as reading_file:
        print("Reading file content:")
        counter = 1
        for line in reading_file:
            print(f"Line {counter}:", line.strip())
            counter += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

