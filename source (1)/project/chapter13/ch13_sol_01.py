class Car:		
    def __init__(self, c, l):	
        self.color = c             
        self.length = l            
    def moveForward(self):	
         print('=== moveForward() 호출 ===')

    def moveBackward(self):
        print('=== moveBackward() 호출 ===')

car1 = Car('blue', 500)
car2 = Car('black', 450)

print('Color of car1 :', car1.color)
print('Color of car2 :', car2.color)

car1.color = input('원하는 색상을 입력하세요. ') 
car2.color = input('원하는 색상을 입력하세요. ')  

print('Color of car1 :', car1.color) 
print('Color of car2 :', car2.color) 
