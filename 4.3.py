def factorial(n):
    silnia = 1;
    for i in range(1,n+1):
      silnia = silnia*i  
    return(silnia)

n=int(input("Podaj liczbe ktorej silnie chcesz obliczyc:"))
print(factorial(n))
