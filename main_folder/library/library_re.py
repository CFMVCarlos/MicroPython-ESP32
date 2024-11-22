import re

# Compile regular expression
regex = re.compile(r"(\w+)\s+(\d+)")

# Match against a string
match = regex.match("John 123")

if match:
    print("Match found!")
    print("Entire match:", match.group(0))
    print("Name:", match.group(1))
    print("ID:", match.group(2))
else:
    print("No match")

print()

# Search for a pattern in a string
search_result = regex.search("Alice 456")

if search_result:
    print("Search result found!")
    print("Entire match:", search_result.group(0))
    print("Name:", search_result.group(1))
    print("ID:", search_result.group(2))
else:
    print("No search result")

print()

# Substitute matching pattern in a string
new_string = regex.sub("Jane \\2", "Name: Bob 789, ID: 321")
print("Substituted string:", new_string)

print()

# Split a string using a regex
regex = re.compile(r",\s+")
split_result = regex.split("Mike 789, David 123")
print("Split result:", split_result)
