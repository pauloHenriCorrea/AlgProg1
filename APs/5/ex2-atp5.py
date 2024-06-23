# a=5 e b=18

# menor = 5
# i = [2 .. 4] -> a/i ? b/i ? São coprimos se achar algum caso desses  

def coprimos(a,b):
    count = 2
    
    while count < a and count < b:
        if a % count == 0 and b % count == 0:
            return False
        count += 1
    return True
        

a = int(input())
b = int(input())
print("São coprimos -> " + str(coprimos(a,b)))