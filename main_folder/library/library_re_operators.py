import re

# This library in ESP32 only allows to search for the first match in a string

# .
# Match any character
pattern_dot = r"a.b"
string_dot = "acb abb a!b a@b"
match_dot = re.search(pattern_dot, string_dot)
print("Match for .:", match_dot.group(0) if match_dot else "No match")

# [...]
# Match set of characters
pattern_set = r"[abc]"
string_set = "abc123def"
match_set = re.search(pattern_set, string_set)
print("Match for [abc]:", match_set.group(0) if match_set else "No match")

# ^
# Match the start of the string
pattern_start = r"^abc"
string_start = "abcdef"
match_start = re.search(pattern_start, string_start)
print("Match for ^abc:", match_start.group(0) if match_start else "No match")

# $
# Match the end of the string
pattern_end = r"def$"
string_end = "abcdef"
match_end = re.search(pattern_end, string_end)
print("Match for def$:", match_end.group(0) if match_end else "No match")

# ?
# Match zero or one of the previous sub-pattern
pattern_zero_or_one = r"ab?c"
string_zero_or_one = "ac abc abbc"
match_zero_or_one = re.search(pattern_zero_or_one, string_zero_or_one)
print(
    "Match for ab?c:", match_zero_or_one.group(0) if match_zero_or_one else "No match"
)

# *
# Match zero or more of the previous sub-pattern
pattern_zero_or_more = r"ab*c"
string_zero_or_more = "ac abc abbc"
match_zero_or_more = re.search(pattern_zero_or_more, string_zero_or_more)
print(
    "Match for ab*c:", match_zero_or_more.group(0) if match_zero_or_more else "No match"
)

# +
# Match one or more of the previous sub-pattern
pattern_one_or_more = r"ab+c"
string_one_or_more = "ac abc abbc"
match_one_or_more = re.search(pattern_one_or_more, string_one_or_more)
print(
    "Match for ab+c:", match_one_or_more.group(0) if match_one_or_more else "No match"
)

# ??
# Non-greedy version of ?, match zero or one, with the preference for zero
pattern_non_greedy_zero_or_one = r"ab??c"
string_non_greedy_zero_or_one = "ac abc abbc"
match_non_greedy_zero_or_one = re.search(
    pattern_non_greedy_zero_or_one, string_non_greedy_zero_or_one
)
print(
    "Match for ab??c:",
    (
        match_non_greedy_zero_or_one.group(0)
        if match_non_greedy_zero_or_one
        else "No match"
    ),
)

# *?
# Non-greedy version of *, match zero or more, with the preference for the shortest match
pattern_non_greedy_zero_or_more = r"ab*c?"
string_non_greedy_zero_or_more = "abbbc"
match_non_greedy_zero_or_more = re.search(
    pattern_non_greedy_zero_or_more, string_non_greedy_zero_or_more
)
print(
    "Match for ab*c?:",
    (
        match_non_greedy_zero_or_more.group(0)
        if match_non_greedy_zero_or_more
        else "No match"
    ),
)

# +?
# Non-greedy version of +, match one or more, with the preference for the shortest match
pattern_non_greedy_one_or_more = r"ab+c?"
string_non_greedy_one_or_more = "abbbc"
match_non_greedy_one_or_more = re.search(
    pattern_non_greedy_one_or_more, string_non_greedy_one_or_more
)
print(
    "Match for ab+c?:",
    (
        match_non_greedy_one_or_more.group(0)
        if match_non_greedy_one_or_more
        else "No match"
    ),
)

# |
# Match either the left-hand side or the right-hand side sub-patterns of this operator
pattern_or = r"cat|dog"
string_or = "I have a cat and a dog"
match_or = re.search(pattern_or, string_or)
print("Match for cat|dog:", match_or.group(0) if match_or else "No match")

# (...)
# Grouping
pattern_group = r"(\d+)([a-z]+)"
string_group = "123abc456def"
match_group = re.search(pattern_group, string_group)
print(
    "Match for (\d+)([a-z]+):",
    (match_group.group(0) if match_group else "No match"),
)

# \d
# Matches digit
pattern_digit = r"\d+"
string_digit = "abc123def456"
match_digit = re.search(pattern_digit, string_digit)
print("Match for \d+:", match_digit.group(0) if match_digit else "No match")

# \D
# Matches non-digit
pattern_non_digit = r"\D+"
string_non_digit = "abc123def456"
match_non_digit = re.search(pattern_non_digit, string_non_digit)
print("Match for \D+:", match_non_digit.group(0) if match_non_digit else "No match")

# \s
# Matches whitespace
pattern_whitespace = r"\s+"
string_whitespace = "This is a sentence with spaces"
match_whitespace = re.search(pattern_whitespace, string_whitespace)
print("Match for \s+:", match_whitespace.group(0) if match_whitespace else "No match")

# \S
# Matches non-whitespace
pattern_non_whitespace = r"\S+"
string_non_whitespace = "This is a sentence with spaces"
match_non_whitespace = re.search(pattern_non_whitespace, string_non_whitespace)
print(
    "Match for \S+:",
    match_non_whitespace.group(0) if match_non_whitespace else "No match",
)

# \w
# Matches “word characters” (ASCII only)
pattern_word = r"\w+"
string_word = "word123_456"
match_word = re.search(pattern_word, string_word)
print("Match for \w+:", match_word.group(0) if match_word else "No match")

# \W
# Matches non “word characters” (ASCII only)
pattern_non_word = r"\W+"
string_non_word = "word123_456"
match_non_word = re.search(pattern_non_word, string_non_word)
print("Match for \W+:", match_non_word.group(0) if match_non_word else "No match")

# \
# Escape character
pattern_escape = r"\*"
string_escape = "This * is an asterisk"
match_escape = re.search(pattern_escape, string_escape)
print("Match for \*:", match_escape.group(0) if match_escape else "No match")
