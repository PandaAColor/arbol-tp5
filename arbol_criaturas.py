from Criaturas import criaturas
from tree import BinaryTree
from collections import Counter

class Arbol_criaturas(BinaryTree):
    def in_order_criaturas(self, valor= str):
        if valor in self.root.other_values:
            def __in_order_criaturas(root, valor):
                if root is not None:
                    __in_order_criaturas(root.left, valor)
                    print(f'{root.value} , {valor}: {root.other_values[valor]}')
                    __in_order_criaturas(root.right, valor)

            if self.root is not None:
                __in_order_criaturas(self.root, valor)
        else:
            print('valor no encontrado')
    
    def cargar_nuevo_dato(self, nombre, clave, dato):
        nodo = self.search(nombre)
        if nodo is not None:
            nodo.other_values[clave] = dato

    def buscar_datos(self, nombre):
        nodo = self.search(nombre)
        if nodo is not None:
            print(nodo.other_values)
        else:
            print('criatura no encontrada')

    def contador_top3(self, busco):
        contar = Counter()

        def __contador_top3(root, busco):
            if root is not None:
                __contador_top3(root.left, busco)
                valor = root.other_values[busco]
                if valor:
                    contar[valor]+=1
                __contador_top3(root.right, busco)

        __contador_top3(self.root, busco)
        return contar.most_common(3)
    
    def criaturas_derrotadas_por(self, nombre):
        criaturas_vencidas = []

        def __criaturas_derrotadas_por(root, nombre):
            if root is not None:
                __criaturas_derrotadas_por(root.left, nombre)
                vencedor = root.other_values['vencedor']
                if vencedor == nombre:
                    criaturas_vencidas.append(root.value)
                __criaturas_derrotadas_por(root.right, nombre)
        
        __criaturas_derrotadas_por(self.root, nombre)
        if len(criaturas_vencidas)>=1:
            return criaturas_vencidas
        else:
            print(f'{nombre} no ha derrotado a ninguna criatura')
    
    def criaturas_capturadas_por(self, nombre):
        criaturas_capturadas = []

        def __criaturas_capturadas_por(root, nombre):
            if root is not None:
                __criaturas_capturadas_por(root.left, nombre)
                vencedor = root.other_values['capturada']
                if vencedor == nombre:
                    criaturas_capturadas.append(root.value)
                __criaturas_capturadas_por(root.right, nombre)
        
        __criaturas_capturadas_por(self.root, nombre)
        if len(criaturas_capturadas)>=1:
            return criaturas_capturadas
        else:
            print(f'{nombre} no ha capturado a ninguna criatura')


                

    

criaturas_arbol = Arbol_criaturas()

for criatura in criaturas:
    criaturas_arbol.insert(criatura['nombre'], criatura)

#A
criaturas_arbol.in_order_criaturas('vencedor')

#B
print()
for criatura in criaturas:
    criaturas_arbol.cargar_nuevo_dato(criatura['nombre'], 'descripcion','nueva descripcion')

criaturas_arbol.in_order_criaturas('descripcion')

#C
print()
criaturas_arbol.buscar_datos('Talos')

#D
print()
top3 =criaturas_arbol.contador_top3('vencedor')
print('top 3 héroes o dioses que más criaturas vencieron:')
for heroe in top3:
    print(heroe)

#E
print()
criaturas_derrotadas = criaturas_arbol.criaturas_derrotadas_por('Heracles')
print('criaturas derrotadas por Heracles:')
for criatura in criaturas_derrotadas:
    print(criatura)

#F
print()
criaturas_derrotadas = criaturas_arbol.criaturas_derrotadas_por(None)
print('criaturas que no han sido derrotadas:')
for criatura in criaturas_derrotadas:
    print(criatura)

#G
print()
for criatura in criaturas:
    criaturas_arbol.cargar_nuevo_dato(criatura['nombre'], 'capturada','héroe o dios')

#H
print()
lista_capturados = ['Cerbero','Toro de Creta', 'Cierva de Cerinea', 'Erimanto']

for captura in lista_capturados:
    criaturas_arbol.cargar_nuevo_dato(captura, 'capturada', 'Heracles')

#I
print()
criaturas_arbol.proximity_search('E')

#J
print()
eliminado, info = criaturas_arbol.delete('Basilisco')
print(f'se elimino a {eliminado}')

eliminado, info= criaturas_arbol.delete('Sirenas')
print(f'se elimino a {eliminado}')

#K
print()
criaturas_arbol.cargar_nuevo_dato('Aves del Estínfalo', 'descripcion', 'Heracles derrotó a varias')
criaturas_arbol.buscar_datos('Aves del Estínfalo')

#L
print()
nombre_borrado, values = criaturas_arbol.delete('Ladón')
values['nombre'] ='Dragón Ladón'
criaturas_arbol.insert('Dragón Ladón', values)

#M
print()
criaturas_arbol.by_level()

#n
print()
lista_capturados= criaturas_arbol.criaturas_capturadas_por('Heracles')
print('criaturas capturadas por Heracles:')
for criatura in lista_capturados:
    criaturas_arbol.buscar_datos(criatura)