from Superheroes import superheroes
from tree import BinaryTree
from typing import Any, Optional


class Superhero_tree(BinaryTree):

    def es_villano(self):
        def __es_villano(root):
            if root is not None:
                __es_villano(root.left)
                if root.other_values.get("is_villain") == True:
                    print(root.value)  
                __es_villano(root.right)

        if self.root is not None:
            __es_villano(self.root)
    
    def contador_heroe(self):
        def __es_heroe(root):
            if root is None:
                return 0  

            contador = __es_heroe(root.left)

            if root.other_values.get("is_villain") == False:
                contador += 1

            contador += __es_heroe(root.right)

            return contador

        if self.root is not None:
            total = __es_heroe(self.root)
            print(total)   # lo imprimimos
            return total
        return 0

    def in_order_busqueda(self, valor):
            
        def __in_order_busqueda (root, valor):

            if root is not None:
                if root.value >= valor:
                        __in_order_busqueda(root.left, valor)
                if root.value.startswith(valor):
                        print(root.value)
                    
                __in_order_busqueda(root.right, valor)
        if self.root is not None:
            __in_order_busqueda(self.root, valor)
    
    def divide_tree(self,arbol_a,arbol_b):
        def __divide_tree(root, arbol_a, arbol_b):
            if root is not None:
                if root.other_values['is_villain'] is False:
                    arbol_a.insert(root.value, root.other_values)
                else:
                    arbol_b.insert(root.value, root.other_values)
                
                __divide_tree(root.left, arbol_a, arbol_b)
                __divide_tree(root.right, arbol_a, arbol_b)

        __divide_tree(self.root, arbol_a, arbol_b)
            
    

arbol = Superhero_tree()

for super_hero in superheroes:
    arbol.insert(super_hero['name'], super_hero)
#a
arbol.in_order()
#b
arbol.es_villano()
#c
arbol.in_order_busqueda("C")

#D
arbol.contador_heroe()

#E
arbol.proximity_search("D")
nombre_borrar = input(str('introduzca el valor a eliminar '))
nombre_borrado, values = arbol.delete(nombre_borrar)
nuevo_nombre = input(str('nuevo nombre '))
values['name'] =nuevo_nombre
arbol.insert(nuevo_nombre, values)


#F
arbol.post_order()

#G
heroes = Superhero_tree()
villanos = Superhero_tree()
arbol.divide_tree(heroes, villanos)

bosque = [heroes, villanos]

heroes.in_order()
villanos.in_order()



    
