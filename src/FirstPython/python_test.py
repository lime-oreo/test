class Sorter:
    def sort_data (self, data, sort_type):
        if sort_type == 'asc':
            return sorted(data)
        elif sort_type == 'desc':
            return sorted(data, reverse=True)
        
class DataProcessor:
    def __init__(self,sorter):
        self.sorter = sorter
        
    def process (self,data,sort_type):
        return self.sorter.sort_type (data.sort_type)
    

sorter= Sorter()
processor = DataProcessor (sorter)
sorted_data = processor.process ([5,2,9,1],'asc')
print(f'Sorted data:{sorted_data}')