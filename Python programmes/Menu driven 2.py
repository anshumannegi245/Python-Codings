print("MENU")
print("1. Enter a tuple")
print("2. Find the maximun element")
print("3. Find the minimum element")
print("4. Find the sum of elements")
print("5. Count total number of elements")
print("6. Search an element from list")
print("7. Find index of an element")
print("8. Sort element of tuple")
print("9. Concatenation of two tuples")
print("10. Find length of tuple")
print("11. Performing slicing operation")
print("12. Compairing two tuples")
print("13. Excessing item from the tuple")
print("14. Performing traversing in tuples")
print("15. Replicate a tuple")
print("16. Performing membership testing")
print("17. Exit")
choice="yes"
while choice=="yes":
    a=int(input("Enter your choice from the menu"))
    if a==1:
        b=eval(input("Enter a tuple"))
    elif a==2:
        c=max(b)
        print("The maximum element in tuple is",c)
    elif a==3:
        c=min(b)
        print('The minimum element of tuple is',c)
    elif a==4:
        c=sum(b)
        print('The sum of elements is tuple is',c)
    elif a==5:
        i=int(input("Enter the element you want to count"))
        c=b.count(i)
        print("The total number that element occur in element",c)
    elif a==6:
        i=int(input("Enter the index you want to find element of"))
        c=list(b)
        d=c[i]
        print("The element of the above index in list is",d)
    elif a==7:
        i=eval(input("Enter the element you find index of"))
        c=b.index(i)
        print("The index of the element is",c)
    elif a==8:
        c=sorted(b)
        print("After sorting the tuple will be",c)
    elif a==9:
        c=eval(input("Enter the second tuple for concatenation"))
        d=b+c
        print("After concatenation tuple is",d)
    elif a==10:
        c=len(b)
        print("The length of tuple is",c)
    elif a==11:
        i=int(input("Enter the starting value"))
        j=int(input("Enter the ending value"))
        k=int(input("Enter the step value"))
        c=b[i:j:k]
        print("After slicing tuple is",c)
    elif a==12:
        c=eval(input("Enter the second tuple"))
        if b<c:
            print("First tuple is smaller than the second one")
        elif c<b:
            print("Second element is smaller than the second one")
        else:
            print("Both tuples are equal")
    elif a==13:
        i=int(input("Enter the index you want to find element of"))
        c=b[i]
        print("The element of the above index in list is",c)
    elif a==14:
        for i in range(0,len(a)):
            print(a[i])
    elif a==15:
        i=int(input("Enter the number of times you want to replicate"))
        c=b*i
        print(c)
    elif a==16:
        c=eval(input("Enter any element"))
        if c in b:
            print("The typed element is present in the tuple")
        else:
            print("The typed letter is not present in the tuple")
    elif a==17:
        break
    choice=input("Do you want to continue (yes/no)")
    continue
print("THE END")
