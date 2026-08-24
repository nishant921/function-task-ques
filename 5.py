# write a function to check whether a number is perfect or not  a perfect number is a number that is a half the sum of all of its positive division including itself 
def perfect_no(num):
    sum=0
    for i in range(1,num):
        if num % i == 0:
            sum+=i
    if sum==num:
        return True
    else:
        return False
    
    
print(perfect_no(30))