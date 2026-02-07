name = 'fabulous'
print(name[::2])

#length of string
print(len(name))

print(name.upper())

b = '''dear |name|
Good mouning!
|Date|'''

print(b.replace("|name|","Chodhri").replace('|Date|','March')) # chain of replace function

c="12"
print(name.isalpha())
print(c.isdigit())

print(f"my name is {name} Kumar")

# find double space
text = "this is a raw  text with  some extra space"
print("index",text.find("  "))
print("index",text.replace("  ",' '))

# Strings are immutable - they Dont change after they are defined - no function or operation will change it.