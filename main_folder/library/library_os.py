import os

# General functions
print("System information:", os.uname())
print("Random bytes:", os.urandom(5))

# Filesystem access
print("Current directory:", os.getcwd())
print("List of directory entries:")
for entry in os.ilistdir():
    print(entry)
print("List of files in current directory:", os.listdir())
print("Create a directory")
os.mkdir("test_dir")
print("Rename directory")
os.rename("test_dir", "new_dir")
print("Remove directory")
os.rmdir("new_dir")

# Terminal redirection and duplication
print("Redirecting terminal output to a file")

with open("output.txt", "w") as f:
    os.dupterm(f)
    print("This message will be redirected to output.txt")
    print("This message will also be redirected to output.txt")
    os.dupterm(None)

print("Restoring terminal output")
