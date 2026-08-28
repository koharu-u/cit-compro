s = "I'm a string"
print(s)

s = 'I siad "This is a string".'
print(s)

s = """I said "I'm a string"."""
print(s)

s = "abc" + "def"
print(s)

s = 2*("ab" * 3 + "x")
print(s)

s = "Hello World"
print(len(s))
print(s.lower())
print(s.upper())
print(s.find("o"))
print(s.find("o",7))
print(s[2])
print(s[-2])
print(s[2:7])
print(s[8:])
print(s[:7])
print("lo" in s)
print("la" in s)
c = 'e'
if (c in "aeiou"):
    print(c, "is a vowel")

s = "ABCDEFGHI"
i = 3
j = 5
print(s[i])
print(s[5//3])
print(s[i:j+1])
print(s[6/3])
