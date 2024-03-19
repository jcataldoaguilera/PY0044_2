min_sn = [120, 50, 600, 30, 90, 10, 200, 0, 500]
cad_sn = []

for i in range(len(min_sn)) :
    if min_sn[i] < 90 :
        cad_sn.append("bien")
    else :
        cad_sn.append("mal")
print(cad_sn)


## COMPREHENSION ##
min_sn = [120, 50, 600, 30, 90, 10, 200, 0, 500]
cad_sn = ['bien' if min_sn[i] <90 else 'mal' for i in range(len(min_sn))]
print (cad_sn)