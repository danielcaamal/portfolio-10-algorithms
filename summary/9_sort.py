class Sort:
    def __init__(self):
        pass

    def _swap(self, my_list, index1, index2):
        temp = my_list[index1]
        my_list[index1] = my_list[index2]
        my_list[index2] = temp
    
    def bubble_sort(self, my_list):
        for i in range(len(my_list) - 1, 0, -1):
            for j in range(i):
                if my_list[j] > my_list[j+1]:
                    self._swap(my_list, j, j+1)
                    
    def selection_sort(self, my_list):
        for i in range(len(my_list) - 1):
            min_index = i
            for j in range(i + 1, len(my_list)):
                if my_list[j] < my_list[min_index]:
                    min_index = j
            
            if i != min_index:
                self._swap(my_list, i, min_index)
        return my_list