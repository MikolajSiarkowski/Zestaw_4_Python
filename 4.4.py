def fibonacci(n):
    n1=0
    n2=1
    ilosc=0
    if(n <= 0):
        print("liczba musi byc wieksza od 0")
    elif(n==1):
        return(n1)
    else:
        while ilosc<n-1:
            new = n1+n2
            n1 = n2
            n2 = new
            ilosc += 1
        return(n1)


n=int(input("Podaj ktory wyraz ciagu fibonnaciego chcesz obliczyc:"))
print(fibonacci(n))
