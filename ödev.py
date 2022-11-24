#soru1
m = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = []


#soru2
t=[[1, 2], [3, 4], [5, 6, 7]]
output= []


def cevir(x):
    for i in x:
        if isinstance(i,list):
            cevir(i)

        else:
            output_list.append(i)


def ters_dondur(x):

    x=x[::-1]

    for i in x:
        if isinstance(i,list):
            e=i[::-1]
            output.append(e)

        else:
            output.append(i)

    return output


#cevap1
cevir(m)
print("Cevap 1:",output_list)
#cevap2
ters_dondur(t)
print("Cevap 2:",output)