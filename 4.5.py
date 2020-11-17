
def odwracanieRekurencja(L,left,right):
    if(left < right):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        odwracanieRekurencja(L,left+1,right-1)  
    return L;

def odwracanieIteracja(L,left,right):
    while(left<right):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left+=1
        right-=1
    return L
    

L=[1,2,3,4,5]
print("L: ",L)
print("Odwracam iteracyjnie L, wynik: ",odwracanieIteracja(L,0,4))
L2 = [5,4,3,2,1]
print("L2: ",L2)
print("odwracam rekurencyjnie L2, wynik: ",odwracanieRekurencja(L2,0,4))
