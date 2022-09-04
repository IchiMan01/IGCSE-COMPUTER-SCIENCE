#calculate the annual fee
def fee(index):
    cost = 0
    #initial cost
    if membershipType[index] == "Junior":
        cost = 10
    elif membershipType[index] == "Adult":
        cost = 20
    elif membershipType[index] == "Senior":
        cost = 15
    elif membershipType[index] == "Golden":
        cost = 0

    if teamMember[index] == "Active" and membershipType != "Golden":
        cost = cost*0.9
        cost = round(cost, 2)

    return cost


#creating arrays
global name
global age
global gender
global membershipType
global teamMember
global annualFee
global customer

name = []
age = []
gender = []
membershipType = []
teamMember = []
annualFee = []
customer = 4


#create for loops for the members
for i in range(customer):
    #Ask for name and age
    personName = input("\nWhat is your name?: ")
    name.append(personName)
    personAge = int(input("What is your age?: "))
    age.append(personAge)


    #Calculate the membership type
    if age[i] >= 2 and age[i] < 18:
        personMembership = "Junior"
        membershipType.append(personMembership)
    elif age[i] >= 18 and age[i] < 50:
        personMembership = "Adult"
        membershipType.append(personMembership)
    elif age[i] >= 50 and age[i] < 80:
        personMembership = "Senior"
        membershipType.append(personMembership)
    elif age[i] >= 80:
        personMembership = "Golden"
        membershipType.append(personMembership)


    #Team member or not
    personTeam = input("Are you a team member of our swimming team?: ")
    if personTeam.capitalize() == "Yes" or personTeam.capitalize() == "Y":
        personTeam = "Active"
        teamMember.append(personTeam)
    elif personTeam.capitalize() == "No" or personTeam.capitalize() == "N":
        personTeam = "Inactive"
        teamMember.append(personTeam)




#display the information
for i in range(customer):
    print("\nCustomer", i+1)
    print("Name:", name[i])
    print("Age:", age[i])
    print("Membership type:", membershipType[i])
    print("Team member status:", teamMember[i])
    print("Annual fees: $", annualFee[i])
