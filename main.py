print("I can solve ax^2 + bx + c = 0 for you!")
# define a function to judge whether quaratic is greater than 0
def quaratic():
    y=b**2-4*a*c
    return y
# define the function to calculate the roots
def root1():
    y=(-b+((b**2)-(4*a*c))**(0.5))/(2*a)
    return y
def root2():
    y=(-b-((b**2)-(4*a*c))**(0.5))/(2*a)
    return y
while True:# make a cycle
    try:
# ask for a,b c
        a = int(input("Please give me the 'a' coefficient:"))
        b = int(input("Please give me the 'b' coefficient:"))
        c = int(input("Please give me the 'c' coefficient:"))
# discuss the a, b and c
        if a==0:
            print("a cannot be zero")
        elif quaratic()<0:
            print("Sorry, but thst quadratic does not have real roots.")
        elif quaratic()==0:
            print("Thank you, that is a valid input:),I WILL SOLVE NOW.")
            print("Root is:",root1())
            break# stop the code
        else:
            print("Thank you, that is a valid input:),I WILL SOLVE NOW.")
            print("Root 1:",root1())
            print("Root 2:",root2())
            break# stop the code
    except:
        print("That is not a real number!")





