def is_prime(num):
    if num > 1:
        for i in range(2, num//2):  
          if num % i == 0:
            print("Not a prime")
            break
        else:
            print("Prime")
    else:
       print("enter a valid number")

     


is_prime(17)  
is_prime(9)   
is_prime(1)   

