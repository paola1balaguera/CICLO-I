import json
with open("Ahorradores.json") as pepe:
    clientes=json.load(pepe)

uCliente={}
uCliente["clientes"]=[]
consecutivo=0

for i in clientes["cliente"]:
    if i["Saldo"]>35000000:
        consecutivo+=1
        uCliente["clientes"].append({"consecutivo": consecutivo, "numcuenta":i["NumCuenta"], "Saldo": i["Saldo"]})

with open("Dian.json","w") as i:
    json.dump(uCliente,i,indent=4)