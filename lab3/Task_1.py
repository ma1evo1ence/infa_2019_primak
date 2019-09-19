from graph import *

h=700
w=700
r=35 #eyes


canvasSize(w,h)

penColor("light grey")
penSize(0)
brushColor("grey")
rectangle(0,0,w,h)

penColor("black")
penSize(5)
brushColor("yellow")
circle(h/2,w/2,200)


penColor("black")
penSize(5)
brushColor("red")
circle(w/2 - 70,h/2 - 50,r+5)
circle(w/2 + 70,h/2 - 50,r)

brushColor("black")
circle(w/2 - 70,h/2 - 50,r/3)
circle(w/2 + 70,h/2 - 50,r/3)
rectangle(w/2 - 95, h/2 +65,w/2 +95, h/2 +85)
penSize(20)
line(w/2 - 180, h/2 - 180,w/2 - 5,h/2-50)
penSize(10)
line(w/2 + 120, h/2 - 120,w/2 + 5,h/2 - 50)



run()