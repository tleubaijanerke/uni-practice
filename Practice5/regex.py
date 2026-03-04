# 1. Match 'a' followed by zero or more 'b'
# Pattern: ^ab*$
# *  → zero or more occurrences
# ^  → start of string
# $  → end of string

import re

s = input()
x = re.findall("^ab*$", s)

if x:
    print("Match")
else:
    print("No Match")


# 2. Match 'a' followed by two to three 'b'
# Pattern: ^ab{2,3}$
# {2,3} → between 2 and 3 repetitions

import re

s = input()
x = re.findall("^ab{2,3}$", s)

if x:
    print("Match")
else:
    print("No Match")



# 3. Find lowercase letters joined with underscore
# Pattern: ^[a-z]+_[a-z]+$
# [a-z]+ → one or more lowercase letters
# _      → literal underscore

import re

s = input()
x = re.findall("^[a-z]+_[a-z]+$", s)

if x:
    print("Match")
else:
    print("No Match")



# 4. One uppercase letter followed by lowercase letters
# Pattern: ^[A-Z][a-z]+$
# [A-Z]   → one capital letter
# [a-z]+  → one or more lowercase letters

import re

s = input()
x = re.findall("^[A-Z][a-z]+$", s)

if x:
    print("Match")
else:
    print("No Match")


# 5. Match 'a' followed by anything, ending in 'b'
# Pattern: ^a.*b$
# .* → any character, zero or more

import re

s = input()
x = re.findall("^a.*b$", s)

if x:
    print("Match")
else:
    print("No Match")


# 6. Replace space, comma, or dot with colon
# Pattern: [ ,.]
# [] → character set

import re

s = input()
result = re.sub("[ ,.]", ":", s)
print(result)


# 7. Convert snake_case to camelCase
# Pattern: _([a-z])
# () → capture group
# group(1) → letter after underscore

import re

s = input()
result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)
print(result)


# 8. Split a string at uppercase letters
# Pattern: (?=[A-Z])
# (?= ) → positive lookahead

import re

s = input()
result = re.split(r"(?=[A-Z])", s)
print(result)



# 9. Insert spaces before capital letters
# Pattern: (?<!^)([A-Z])
# (?<!^) → not at beginning of string

import re

s = input()
result = re.sub(r"(?<!^)([A-Z])", r" \1", s)
print(result)


# 10. Convert camelCase to snake_case
# Pattern: (?<!^)([A-Z])
# Add underscore before capital letters
# Then convert to lowercase

import re

s = input()
result = re.sub(r"(?<!^)([A-Z])", r"_\1", s).lower()
print(result)