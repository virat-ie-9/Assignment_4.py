### TASK1: Read a File and Handle Errors 

1. try:
  Starts a block of code that may cause an error.
  If everything inside works fine, Python won’t run the except part.

2. file1 = open('sample.txt', 'r')

  Tries to open a file named sample.txt in read mode ('r').

  If the file exists → it opens successfully.

  If the file doesn’t exist → Python raises a FileNotFoundError.

3. result = file1.read()
  Reads the entire file content into the variable result.

4. print(result)
  Displays the file’s contents on the console.

5. file1.close()
  Closes the file (important to free system resources).

6. except FileNotFoundError:
  This block runs if any error happens inside try.

7. print('Error: The file \'sample.txt\' was not found.')
  Prints a friendly error message if the file doesn’t exist.



### TASK2: Write and Append Data to a File

1. n = input("Enter text to write to the file: ")
  Asks the user to enter some text.
  Whatever is typed gets stored in the variable n.

2. file2 = open('output.txt', 'w')
  Opens (or creates if it doesn’t exist) output.txt in write mode ('w').
  Write mode will erase existing contents before writing new data.

3. result = file2.write(n + '\n')
  Writes the text from n into the file, followed by a newline character \n.
  The return value (result) is the number of characters written.
  Example: If you type "Hello", it writes "Hello\n" to the file.

4. print("Data successfully written to output.txt.")
  Confirms that the first write was successful.

5. m = input("Enter additional text to append: ")
  Asks the user for more text to add to the file.

6. file2 = open('output.txt', 'a')
  Opens the file again, this time in append mode ('a').
  Append mode adds new content at the end without erasing the old content.

7. result = file2.write(m)
  Adds the new text from m to the file (no automatic newline unless you add '\n' manually).

8. print("Data successfully appended.")
  Confirms that the second write was successful.

print("Final content of output.txt: ")

Prints a message saying it will now display the final file content.
