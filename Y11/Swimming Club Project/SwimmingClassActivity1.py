#calculate the annual fee
def fee(personMembership, personTeam):
    cost = 0
    #initial cost
    if personMembership == "Junior":
        cost = 10
    elif personMembership == "Adult":
        cost = 20
    elif personMembership == "Senior":
        cost = 15
    elif personMembership == "Golden":
        cost = 0

    if personTeam == "Active" and personMembership != "Golden":
        cost = cost*0.9

    cost = "{:.2f}".format(cost)

    return cost

class person():
    def __init__(self, name, age, membershipType, teamMember, annualFee, paid):
        self.name = name
        self.age = age
        self.membershipType = membershipType
        self.teamMember = teamMember
        self.annualFee = annualFee
        self.paid = paid

    def stat(self, newPerson):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Membership type:", self.membershipType)
        print("Team member status:", self.teamMember)
        print("Annual fees: $", self.annualFee)
        print("Paid:", self.paid)



global customer
global index
customer = []
index = 2
count = 0


for i in range(index):
    personName = input("\nWhat is your name?: ")
    personAge = int(input("What is your age?: "))

    #Membership type
    if personAge >= 2 and personAge < 18:
        personMembership = "Junior"
    elif personAge >= 18 and personAge < 50:
        personMembership = "Adult"
    elif personAge >= 50 and personAge < 80:
        personMembership = "Senior"
    elif personAge >= 80:
        personMembership = "Golden"

    #Team member or not
    personTeam = input("Are you a team member of our swimming team?: ")
    if personTeam.capitalize() == "Yes" or personTeam.capitalize() == "Y":
        personTeam = "Active"
    elif personTeam.capitalize() == "No" or personTeam.capitalize() == "N":
        personTeam = "Inactive"

    #Annual Fees
    personFee = fee(personMembership,personTeam)

    #Paid or not
    personPaid = input("Have you paid your annual fee this year?(y/n): ")
    if personPaid.capitalize() == "Yes" or personPaid.capitalize() == "Y":
        personPaid = "Yes"
    elif personPaid.capitalize() == "No" or personPaid.capitalize() == "N":
        personPaid = "No"

    #Add object to list customer
    newPerson = person(personName,personAge,personMembership,personTeam,personFee,personPaid)
    customer.append(newPerson)

#Print the 'Stats'
for i in range(len(customer)):
    count += 1
    print("\nCustomer", count)
    customer[i].stat(customer[i])
