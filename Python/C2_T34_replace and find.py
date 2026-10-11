string="my name is mir and I am learning Python because Python is a great programming language."
print(string.find("Python"))
# Output: 33

python=string.find("Python")
print(string.find("Python", python + 1))
# Output: 48

replace_string=string.replace("Python", "programming")
print(replace_string)
# Output: my name is mir and I am learning programming because programming is a great programming language.