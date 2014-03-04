# write.py


filename = "file.txt"
file = open(filename, "w")  # Here, "w" stands for open for writing

contents = ["Python is awesome.", "You should check it out!"]

# Here, we are joining each element with a new line
file.write("\n".join(contents))

# when we are done, we close the file
file.close()
