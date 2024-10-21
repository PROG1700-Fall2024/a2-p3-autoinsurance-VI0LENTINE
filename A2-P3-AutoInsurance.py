#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #: W0516070     
#Student Name: Valentine Byrnes  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    import sys

    #INPUT - Sex and age input
    sex = input("Are you 'Male' or 'Female': ").lower()
    if sex == "male" or sex == "female":
        age = int(input("Enter your age: "))
    else:
        print("Invalid sex entered.")
        sys.exit()

    #INPUT - Age, find insurance rate based on input (Male/female)
    if sex == "male":
        if age >= 15 and age <= 24:
            rate = 0.25

        elif age >= 25 and age <= 39:
            rate = 0.17

        elif age >= 40 and age <= 69:
            rate = 0.1
            
        else:
            print("Age not eligible for insurance.")
            sys.exit()

    elif sex == "female":
        if age >= 15 and age <= 24:
            rate = 0.2

        elif age >= 25 and age <= 39:
            rate = 0.15

        elif age >= 40 and age <= 69:
            rate = 0.1     
        else:
            print("Age not eligible for insurance.")
            sys.exit()
    
    #INPUT - Purchase
    purchase = int(input("Enter the purchase price of the vehicle: "))
    
    #CALCULATIONS - Calculate client's monthly insurance
    monthly = float((purchase * rate) / 12)

    #OUTPUT - Client's monthly insurance
    print("Your monthly insurance will be: ${0:.2f}".format(monthly))

    # YOUR CODE ENDS HERE

main()
