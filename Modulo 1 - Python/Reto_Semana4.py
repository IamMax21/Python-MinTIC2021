def clasificacion_huevos(mylist):
    if mylist==[]:
        return mylist
    else:
        contadorAAA=0       # Huevos AAA cuyo peso es igual o está por encima de los 69 g.
        bandejasAAA=0       # Bandejas de 12 huevos

        contadorAA=0        # Huevos AA cuyo peso va desde los 60 g. 68 g.
        bandejasAA=0        # Bandejas de 24 huevos

        contadorA=0         # Huevos A cuyo peso va desde los 55 g. hasta 59 g.
        bandejasA=0         # Bandejas de 30 huevos

        contadorBC=0        # Huevos A cuyo peso va desde los 54 g para abajo.
        bandejasBC=0        # Bandejas de 30 huevos
        for i in range(0, len(mylist)):
            if mylist[i]>=69:                                #Huevos AAA
                contadorAAA+=1
                if contadorAAA==12:
                    bandejasAAA+=1
                    contadorAAA=0
            if mylist[i]>=60 and mylist[i]<69:               #Huevos AA
                contadorAA+=1
                if contadorAA==24:
                    bandejasAA+=1
                    contadorAA=0
            if mylist[i]>=55 and mylist[i]<60:               #Huevos A
                contadorA+=1
                if contadorA==30:
                    bandejasA+=1
                    contadorA=0
            if mylist[i]<55:                                 #Huevos BC
                contadorBC+=1
                if contadorBC==30:
                    bandejasBC+=1
                    contadorBC=0
        listHuevos=[{"tipo_huevo": "A", "numero_huevos": ((bandejasA*30)+contadorA), "numero_bandejas": bandejasA},{"tipo_huevo": "AA", "numero_huevos": ((bandejasAA*24)+contadorAA), "numero_bandejas": bandejasAA},{"tipo_huevo": "AAA", "numero_huevos": ((bandejasAAA*12)+contadorAAA), "numero_bandejas": bandejasAAA},{"tipo_huevo": "BC", "numero_huevos": ((bandejasBC*30)+contadorBC), "numero_bandejas": bandejasBC}]
        return listHuevos

print (clasificacion_huevos([]))

list1=[{'tipo_huevo': 'A', 'numero_huevos': 3, 'numero_bandejas': 0}, {'tipo_huevo': 'AA', 'numero_huevos': 2, 'numero_bandejas': 0}, {'tipo_huevo': 'AAA', 'numero_huevos': 11, 'numero_bandejas': 0}, {'tipo_huevo': 'BC', 'numero_huevos': 17, 'numero_bandejas': 0}]
list2=clasificacion_huevos([61.346298686672775, 34.233178626107, 57.34384047779798, 14.759669451854407, 2.6094012384316523, 15.86566649377813, 73.24921756463254, 92.06565326205666, 82.42624746401899, 41.40520634697313, 27.887615910281504, 15.419097772731337, 87.84008972503628, 70.27623742730331, 69.16153101283734, 0.612101269882015, 46.289802764059154, 49.26286961156773, 70.6449165045779, 69.00412474194266, 8.831852730338607, 91.42746088863736, 59.18919604417584, 2.7020114490544755, 19.957344941087108, 66.79631476206701, 93.1631865015004, 1.7468752974341029, 70.27756352117139, 43.67833420165258, 16.500802082672028, 59.05977555941144, 27.316777517619485])


if list1==list2:
    print(True)
else:
    print(False)