class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size 
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 13) % len(self.data_map)
        return my_hash

    def set_item(self,key,value):
        index= self.__hash(key) # genera posición basado en el key
        if self.data_map[index]==None: # inicializa arreglo vacio
            self.data_map[index]=[] # arreglo vacio
        self.data_map[index].append([key,value]) #inserto el item
    
    def get_item(self,key):
        index= self.__hash(key) # genera posición basado en el key
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1] # regresa el valor
        return None

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
        
my_hash_table = HashTable()


my_hash_table.set_item("maria",80)
my_hash_table.set_item("JC",70)
my_hash_table.set_item("Bryan",69)
my_hash_table.print_table()
print(my_hash_table.get_item("maria"))
print(my_hash_table.get_item("JC"))
print(my_hash_table.get_item("Bryan"))



"""
    salida esperada
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""