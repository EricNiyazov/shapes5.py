from graphics import *
window = GraphWin("shapes5.py", 300, 300)
window.setCoords(0, 0, 1000, 1000)

bTri = Polygon(Point(100, 100), Point(150, 200), Point (200, 100))
bTri.setFill(color_rgb(30, 30,230))

gSqur = Polygon(Point(800, 800), Point(900, 800), Point (900, 900), Point(800, 900))
gSqur.setFill(color_rgb(30, 230, 30))

orRomb = Polygon(Point(450, 500), Point(500, 600), Point (550, 500), Point(500, 400))
orRomb.setFill(color_rgb(255,165,0))

rCrcl = Circle(Point (100, 900), 50)
rCrcl.setFill(color_rgb(230,30,30))

yRect = Polygon(Point(700, 200), Point(900, 200), Point(900, 100), Point (700, 100))
yRect.setFill(color_rgb(255,255,0))

yRect.draw(window)
orRomb.draw(window)
gSqur.draw(window)
bTri.draw(window)
rCrcl.draw(window)


window.getMouse()
window.close()
