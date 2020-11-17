suma = 0
def sum_seq(sequence):
    global suma
    for i in range(0,len(sequence)):
        flag = isinstance(sequence[i],(list,tuple))
        if(flag == True):
           sum_seq(sequence[i])
        else:
            suma+=sequence[i]
    return(suma)


seq = (1,(2,3),[3,4,(5,8)])
print("seq = ",seq)
print("suma = ",sum_seq(seq))
