"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('C:\\lambda\\cs\\week1\\project1\\src\\foo.txt') as f:
    read_data = f.read()
    print(read_data)

'''
It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks.
'''

print(f.closed)  # verifies that the file has been automatically closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

try:
    with open('C:\\lambda\\cs\\week1\\project1\\src\\bar.txt', 'x') as f:
        f.write("Hello world\n")
        f.write("Isn't this amazing that I am now gonna smash Python\n")
        f.write("Nwanne ndi a amaro k'anyi si kwado o")
except FileExistsError:
    print("Hey buddy, the file has been created, consider deleting it before creating it again")

with open('C:\\lambda\\cs\\week1\\project1\\src\\bar.txt') as f:
    read_data = f.read()
    print(read_data)
