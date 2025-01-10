def binary_calculator(bin1, bin2, operator):
    acceptablenum = ["0", "1"] # Checks if any characters in bins are not in the acceptable characters.
    for chars in bin1: 
        if chars not in acceptablenum:
            return("Error")
    for chars in bin2:
        if chars not in acceptablenum:
            return("Error")
    if len(bin1) != 8: # Checks if the bin is equal to 8 characters.
        return("Error")
    else:
        for binary in bin1: # Converts all 1's in the bin into their decimal value.
            pos = "1"
            instances = " ".join(str(i) for i in range(len(bin1)) if bin1.startswith(pos, i))
            decical = {48: "128", 49: "64", 50: "32", 51: "16", 52: "8", 53: "4", 54: "2", 55: "1"}
            decisult = instances.translate(decical)
    bin1res = (decisult.split())
    bin1fin = ([int(num) for num in bin1res])
    sum1 = (sum(bin1fin))



    if len(bin2) != 8: # Repeats the same processes from before but instead checking through bin2.
        return("Error")
    else:
        for binary in bin2:
            pos = "1"
            instances = " ".join(str(i) for i in range(len(bin2)) if bin2.startswith(pos, i))
            decical2 = {48: "128", 49: "64", 50: "32", 51: "16", 52: "8", 53: "4", 54: "2", 55: "1"}
            decisult2 = instances.translate(decical2)
    bin2res = (decisult2.split())
    bin2fin = ([int(num) for num in bin2res])
    sum2 = (sum(bin2fin))



    if operator == "+": # Determines what the operator being used is and how to process the answer.
        answer = (sum1 + sum2)
    if operator == "-":
        answer = (sum1 - sum2)
    if operator == "*":
        answer = (sum1 * sum2)
    if operator == "/":
        if sum2 == 0: # Checks if 0 is being divided by.
            return("NaN")
        answer = (sum1 / sum2)
        
    

    basefin = list("00000000") # Converts the final answer from decimal to binary value.
    if answer > 255 or answer < 0: # Checks if the calculation causes an overflow.
        return("Overflow")
    if answer >= 128:
        answer = answer - 128
        basefin[0] = "1"
    if answer >= 64:
        answer = answer - 64
        basefin[1] = "1"
    if answer >= 32:
        answer = answer - 32
        basefin[2] = "1"
    if answer >= 16:
        answer = answer - 16
        basefin[3] = "1"
    if answer >= 8:
        answer = answer - 8
        basefin[4] = "1"
    if answer >= 4:
        answer = answer - 4
        basefin[5] = "1"
    if answer >= 2:
        answer = answer - 2
        basefin[6] = "1"
    if answer >= 1:
        answer = answer - 1
        basefin[7] = "1"
    return("".join(basefin))