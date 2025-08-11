### TASK1: read a file and handle errors

try:
    file1 = open('sample.txt', 'r')
    result = file1.read()
    print(result)
    file1.close()
except FileNotFoundError:
    print('Error: The file \'sample.txt\' was not found.')

### TASK2: Write and append Data to a file:

n = input("Enter text to write to the file: ")
file2 = open('output.txt', 'w')
result = file2.write(n + '\n')                       # take inputs from n.., then after starts a new line.
print("Data successfully written to output.txt.")

m = input("Enter additional text to append: ")
file2 = open('output.txt', 'a')
result = file2.write(m)
print("Data successfully appended.")

print("Final content of output.txt: ")

file2 = open('output.txt', 'r')
result = file2.read()
print(result)
