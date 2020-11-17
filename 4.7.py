L=[]
def flatten(sequence):
    global L
    for i in range(0,len(sequence)):
        flag = isinstance(sequence[i],(list,tuple))
        if(flag == True):
           flatten(sequence[i])
        else:
            L += str(sequence[i])
    return(L)


seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print("seq = ",seq)
print("flatten(seq) = ",flatten(seq))
