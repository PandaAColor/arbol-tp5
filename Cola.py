from typing import Any, Optional

class Queue:
    def __init__(self):
        self.__elements=[]
    
    def arrive(self, value: Any) ->None: #agregar elemento
        self.__elements.append(value)

    def attention(self) -> Optional[Any]: #eliminar elemento al principio de la cola
        return(
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) ->int: #tamaño de la cola
        return len(self.__elements)

    def on_front(self) ->Optional[Any]: #ver elemento delante de la cola
        return(
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self): #mover el elemento delante al final de la cola
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return(value)
    
    def show (self): #mostrar cola
        for i in range (len(self.__elements)):
            print(self.move_to_end())