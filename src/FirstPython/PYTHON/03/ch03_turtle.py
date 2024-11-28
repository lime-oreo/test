#import turtle
#t=turtle.Turtle()
#t.shape('turtle')
#angle=120
#t.right(angle)
#t.forward(100)
#t.left(angle)
#t.forward(100)
#t.left(angle)
#t.forward(100)
#turtle.done()

import turtle
t=turtle.Turtle()
t.shape('turtle')
angle=int(input('회전 각도를 입력하세요.'))
length=int(input('전진 길이를 입력하세요.'))
t.fd(length)
t.left(angle)
t.fd(length)
t.lt(angle)
t.fd(length)
t.lt(angle)
t.fd(length)
t.lf(angle)
t.fd(length)
turtle.done()


