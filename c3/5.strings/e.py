#escape characters

#txt = "We are the so-called "Vikings" from the north."
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#single quote
txt = 'It\'s alright.'
print(txt) 

#backslash
txt = "This will insert one \\ (backslash)."
print(txt) 

#new line
txt = "Hello\nWorld!"
print(txt) 
print('\n')

#Carriage return 
txt = "Hello\rWorld!"
print(txt) 
print('\n')

#tab
txt = "Hello\tWorld!"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 