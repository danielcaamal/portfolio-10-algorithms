class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

    
    def set(self, key, value):
        index = self.__hash(key)
        
        if not self.data_map[index]:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])
        return True
    
    def get(self, key):
        index = self.__hash(key)
        
        if self.data_map[index] == None:
          return None

        for item in self.data_map[index]:
            if item[0] == key:
                return item[1]
        
        return None
    
    def keys(self):
        all_keys = []
        
        for index in self.data_map:
            for key_value in index:
                all_keys.append(key_value[0])
        return all_keys