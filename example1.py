# problem on error handling
def palindrome(x):
    sum=0
    while x>0:
        sum=sum*10+x%10
        x=x//10
    return sum
while True:
    try:
        x=int(input("enter a number: "))
        print(x==palindrome(x))
        break
    except ValueError:
        print("you have entered a character")jbsfjgfjbcsdjh
