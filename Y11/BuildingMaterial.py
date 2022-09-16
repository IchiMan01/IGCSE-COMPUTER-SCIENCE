def cement():
    weight = float(input("Enter the weight of the sack(kg): "))
    if weight < 25.1 and weight > 24.9:
        return "Accepted", weight
    elif weight >= 25.1:
        print("Status: Rejected")
        print("Reason: Sack is overweight")
        exit()
    elif weight <= 24.9:
        print("Status: Rejected")
        print("Reason: Sack is underweight")
        exit()

def gravelOrsand():
    weight = float(input("Enter the weight of the sack(kg): "))
    weight = round(weight, 1)
    if weight < 50.1 and weight > 49.9:
        return "Accepted", 3, weight
    elif weight >= 50.1:
        print("Status: Rejected")
        print("Reason: Sack is overweight")
        exit()
    elif weight <= 49.9:
        print("Status: Rejected")
        print("Reason: Sack is underweight")
        exit()

#content printing procedure
def contentPrint():
    if content == "C":
        print("Cement")
    elif content == "G":
        print("Gravel")
    elif content == "S":
        print("Sand")

#weight printing procedure
print("CONTENT AND WEIGHT OF MATERIAL CHECKING PROGRAM")
print("Please use these when answering question:\n- C for cement\n- G for gravel\n- S for sand")
content = input("Please enter the type of content (C/G/S): ")
content = content.capitalize()
while content != "C" and content != "G" and content != "S":
    print("Status: Rejected")
    print("Reason: Incorrect content")
    content = input("Please enter the type of content (C/G/S): ")
if content == "C":
    status, weight = cement()
elif content == "S" or content == "G":
    status, weight = gravelOrsand()


print("\n==REPORT==\nContent:", end = " ")
contentPrint()
print("Status: Accepted")
print("Weight:", weight, "KG")
