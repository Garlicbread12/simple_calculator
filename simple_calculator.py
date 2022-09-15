#get raw input

# --- INPUTS --- #
raw_equation = input("please enter you equation in the format similar to the following examples:7+7,49x2,54/5,40-35. etc.")
#turn string input into list by placing each character in the string into list with for loop
equation = list(raw_equation)

for character in equation:
    #loop through list until you find a mathematical operator
    #each if/elif statement checks for an operator, then processes the equation in the same ways
    if character == "x" or character == "*":
        # find index of the operator
        operater_indx = equation.index(character)
        #create two empty strings to store each side of the equation
        fnum = ""
        snum = ""
        # append each character before the operator to the first number's string
        for i in range(operater_indx):
            fnum += equation[i]
        #similarly append each character after the operator to the snum string
        for j in range(operater_indx+1, len(equation)):
            snum += equation[j]
        #convert both strings into integers to do operations
        fnum = int(fnum)
        snum = int(snum)
        #print the result, in this case multiplication
        print(fnum*snum)
    elif character == "+":
        #same process as last block, this time for addition
        operater_indx = equation.index(character)
        fnum = ""
        snum = ""
        for i in range(operater_indx):
            fnum += equation[i]
        for j in range(operater_indx+1, len(equation)):
            snum += equation[j]
        fnum = int(fnum)
        snum = int(snum)
        print(fnum+snum)
    elif character == "-":
        operater_indx = equation.index(character)
        fnum = ""
        snum = ""
        for i in range(operater_indx):
            fnum += equation[i]
        for j in range(operater_indx+1, len(equation)):
            snum += equation[j]
        fnum = int(fnum)
        snum = int(snum)
        print(fnum-snum)
    elif character  == "/":
        operater_indx = equation.index(character)
        fnum = ""
        snum = ""
        for i in range(operater_indx):
            fnum += equation[i]
        for j in range(operater_indx+1, len(equation)):
            snum += equation[j]
        fnum = int(fnum)
        snum = int(snum)
        print(fnum/snum)
    
