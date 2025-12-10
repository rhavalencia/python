#Break

name = "Python"
for letter in name:
    if letter == "h":
        break
    print(letter)
    
#Continue
number = "123-456-7890"
for digit in number:
    if digit == "-":
        continue
    print(digit)
    
#Pass
for counter in range(1, 21):
    if counter == 15:
        pass
    else:
        print(counter)