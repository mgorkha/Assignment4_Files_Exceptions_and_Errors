import csv

with open("output.txt", 'w') as writing_file:
    line = input("Enter text to write to the file:")
    writing_file.write(line)
    writing_file.write('\n')
    print("Data successfully written to output.txt.")

with open("output.txt", 'a') as appending_file:
    line = input("Enter additional text to append:")
    appending_file.write(line)
    print("Data successfully appended.")

with open("output.txt", 'r') as reading_file:
    print("Final content of output.txt:")
    for line in reading_file:
        print(line.strip())
