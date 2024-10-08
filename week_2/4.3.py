askUser = True

inputs = []
sum = 0

while askUser == True:
    userInput = int(input("Enter a number: "))

    if userInput > 0:
        inputs.append(userInput)
    else:
        askUser = False
    
for i in inputs:
    sum += i

print(sum)