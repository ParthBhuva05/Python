# Leap Year Code 


print("-------------------- 1 Start --------------------")

def is_leap(year):
    leap = False

    if year / 4 == 0:
        return True
    elif  year / 100 == 0:
        return True
    elif year / 400 == 0:
        return True
    else: 
        return False

    return leap

year = int(input("Enter The Year :"))
print(is_leap(year))

print("-------------------- 1 Complete --------------------")



# # Next

if __name__ == '__main__':
    n = int(input("Enter The Number: "))
    for i in range(1,n+1):
        print(i, end=" ")





