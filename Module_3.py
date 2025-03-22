#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

try:
    fname = input("Enter file name: ")
    # You might need to adjust this path according to where your words.txt is located
    fh = open(fname, encoding='utf-8')
    
    # Read each line and convert to upper case
    for line in fh:
        line = line.rstrip().upper()
        print(line)
    fh.close()
except FileNotFoundError:
    print(f"Error: The file '{fname}' was not found.")
    print("Make sure the file exists in the current directory.")

