#Reto Semana 3
"""
productos= [{"sku": 1, "fecha_expiracion": "", "precio": 376.443, "descuento": 0}, 
            {"sku": 2, "fecha_expiracion": "hoy", "precio": 84.945, "descuento": 31}, 
            {"sku": 3, "fecha_expiracion": "", "precio": 941.135, "descuento": 15}, 
            {"sku": 4, "fecha_expiracion": "hoy", "precio": 40.244, "descuento": 20}, 
            {"sku": 5, "fecha_expiracion": "hoy", "precio": 796.153, "descuento": 21}, 
            {"sku": 6, "fecha_expiracion": "hoy", "precio": 308.358, "descuento": 0}, 
            {"sku": 7, "fecha_expiracion": "hoy", "precio": 457.561, "descuento": 20}, 
            {"sku": 8, "fecha_expiracion": "", "precio": 322.529, "descuento": 7}, 
            {"sku": 9, "fecha_expiracion": "hoy", "precio": 837.608, "descuento": 0}]
numberObjects=len(productos)
indiceDiccionario=0
subtotal=0
precio=0
descuento=0.0
vencimiento=False
print(f"La lista tiene {numberObjects} objetos")

while indiceDiccionario<numberObjects:

    precio=productos[indiceDiccionario]["precio"]
    if productos[indiceDiccionario]["fecha_expiracion"]=="hoy":
        vencimiento=True
        sku=productos[indiceDiccionario]["sku"]
        print(f"Sku: {sku}")
        print(f"Precio Real: {precio}")
        descuento=(1-(productos[indiceDiccionario]["descuento"])/100)
        print(f"Descuento: {descuento}")
        precio= (precio*descuento)
        print(f"Nuevo Precio: {precio}")
        print(f"Subtotal: {subtotal}")
        print(f"Descuento por Vencimiento: {vencimiento}")
        subtotal+=precio*0.8
        print(f"Nuevo Subtotal: {subtotal}")
        print("")
    else:
        vencimiento=False
        sku=productos[indiceDiccionario]["sku"]
        print(f"Sku: {sku}")
        print(f"Precio Real: {precio}")
        descuento=(1-(productos[indiceDiccionario]["descuento"])/100)
        print(f"Descuento: {descuento}")
        precio= (precio*descuento)
        print(f"Nuevo Precio: {precio}")
        print(f"Subtotal: {subtotal}")
        print(f"Descuento por Vencimiento: {vencimiento}")
        subtotal+=precio
        print(f"Nuevo Subtotal: {subtotal}")
        print("")

    indiceDiccionario+=1
resultado=round(subtotal, 2)

print(resultado)
"""
frase="- 1 jamón Zenú 500 gr - 1 butifarra caribe- 1 salchicha superperro Zenú- 2 salchichón de pollo Zenú de 250 grs- 2 papa fácil de 500- 4Milo de 500 o 600( mejor precio)- 4 azúcar marca O de 1 kl.- 1 queso mozzarella coolechera de 500 - 1 queso sabana x15 - 1 queso finesse x 15 - 3 sello rojo de 250grs - 1 colcafe descafeinado mediano- 1 bocadillo lonchera marca O - 3 galleta oreo original - 3 chocolatina jet - 2 bolsas de jet lyne- 1 galleta leche Noel - 1 paquete saltin Noel x4 - 1 paquete ducales x 4 - 2 cajitas de macarrones con queso- 3 sobres base bolognesa - sobres base napolitana - 3 sobres base bechamel - 4 sobres de sopas Maggi de las de empaque blanco que son de quinoa y avena - 1 aceite canola life - 1 saragoza 1 lb - 1 cajita de cebada perlada- 1 bolsa maíz pira - 1 arroz Diana 3 kl - 2 laticas maíz San Jorge pequeña- 1 bolsa Doritos - 1 bolsa de todito picante- 1 bolsa chitos- 1 sobre chicoco el más pequeño- 1 sobre salsa BBQ pequeño- 1 papel cocina familia practidiarias - 2 mantequilla de maní Manitoba- 1 bolsa chocoramito - 1 galleta Ritz de queso - 2champú h y s verde(el mejor precio) - 2 champú savital azul biotina - garrafa alcohol - 1 bolsa pan árabe Ismael - 1 botella grande de jugo cranberry ligth - 1 garrafita alcohol - paquete Protex x 3 ( mejor precio) - 1 caja de alka Seltzer - 1 dogourmet cachorro 2 kl- 1 nutrecan adulto 1 kl - 2 mirringo de 1 kl- 1 papel higiénico O x 12 rollos - 3 sixpack coolechera entera - 4 sixpack Colanta deslactosada - 1 sixpack leche slight colanta- 1 bolsa de quinoa en grano - 8 filetes de tilapia - 2 lbs pulpa de cerdo relajada delgada - 2 lb costilla full carnuda - 1 malla mandarina - 1 piña oromiel- 1 malla plátanos verdes- 5 lbs papa clasificada - 1 malla limón - 1 brócoli pequeño - 1 coliflor pequeño - 3 mazorcas tiernas - 6 lulos - 6 maracuyas - 1 Ensure Advance grande vainilla - 1caja aromática canela - 1 caldo costilla doblegusto x12 - 1 caldo gallina doblegusto x 12 - 1 pan Bimbo vital fucsia ."
algoritmo=frase.replace("-", "\n")
print(algoritmo)

