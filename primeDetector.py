def main():
    num = int(input("Enter a number: "))
    if num == 1:
        print("Not prime")
    elif num == 2:     
        print("prime")
    elif num == 5:
        print("prime")
    elif num % 2 == 0:     
        print("Not prime")
    else:
        max = num // 2 
        for i in range(3,max+1,2):
            if num % i == 0:
                print("Not prime")
                print("Two factors are",i,"and",int(num/i))
                return
        print("Prime")    
   
main()     
