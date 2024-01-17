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
    
    
    def insertion_sort(self, my_list):
        for i in range(1, len(my_list)):
            temp = my_list[i]
            j = i - 1
            while j >= 0 and temp < my_list[j]:
                my_list[j+1] = my_list[j]
                my_list[j] = temp
                j -= 1
        return my_list
    
    def _merge(self, my_list1, my_list2):
        merged = []
        i = 0
        j = 0
        while i < len(my_list1) and j < len(my_list2):
            if my_list1[i] < my_list2[j]:
                merged.append(my_list1[i])
                i += 1
            else:
                merged.append(my_list2[j])
                j += 1
        
        while i < len(my_list1):
            merged.append(my_list1[i])
            i += 1
        
        while j < len(my_list2):
            merged.append(my_list2[j])
            j += 1
        
        return merged
    
    def merge_sort(self, my_list):
        if len(my_list) == 1:
            return my_list
        
        mid_index = int(len(my_list) / 2)
        
        left = self.merge_sort(my_list[:mid_index])
        right = self.merge_sort(my_list[mid_index:])
        
        return self._merge(left, right)

    def _pivot(self, my_list, pivot_index, end_index):
        swap_index = pivot_index
        
        for i in range(pivot_index + 1, end_index + 1):
            if my_list[i] < my_list[pivot_index]:
                swap_index += 1
                self._swap(my_list, swap_index, i)
        
        self._swap(my_list, pivot_index, swap_index)
        return swap_index
      
    def _r_quick_sort(self, my_list, left, right):
        if left < right:
            pivot_index = self._pivot(my_list, left, right)
            self._r_quick_sort(my_list, left, pivot_index-1)
            self._r_quick_sort(my_list, pivot_index + 1, right)
        return my_list
      

    def quick_sort(self, my_list):
        return self._r_quick_sort(my_list, 0, len(my_list) - 1)
