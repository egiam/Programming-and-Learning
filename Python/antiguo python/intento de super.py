
productos=['banana','manzana','pera','uva','naranja','mandarina','sandia','kiwi']
precios=[0.75,1.23,1.11,1.98,2.01,1.20,2.01,0.96]

def finish():
    print('gracias por su compra')
    print('Lista de sus productos:',Lista_compra)
    print(total)

Lista_compra=[]
cosa='x'
total=0

while cosa!='0':
    cosa=input("producto a pasar(si aprieta 0 se detendra la lista): ")
    if cosa=='0':
        finish()
    else:
        fruit=productos.index(cosa)
        lista=Lista_compra.append(cosa)
        print(precios[fruit])
        total=total+precios[fruit]
        print('total actual:',total)
