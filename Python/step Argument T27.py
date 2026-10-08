#step Argument syntax- [start:stop:step]
#starts from index 2 and goes up to index 6 but takes gape in every second character
print("language"[2:6:2]) # prints 'pto'
#OR
language="language"
print(language[2:6:2]) # prints 'pto'

#for backwords slicing, we can use negative step argument
print("language"[::-1]) # prints 'egaugnal'


#starts from index 6 and goes up to index 2 but takes gap in every second character
print("language"[6:2:-1]) # prints 'egau'

