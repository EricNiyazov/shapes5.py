from graphics import *
window = GraphWin("shapes5.py", 300, 300)
window.setCoords(0, 0, 1000, 1000)
bTri = Polygon(Point(100, 100), Point(150, 200), Point (200, 100))
bTri.setFill(color_rgb(30, 30,230))
gSqur = Polygon(Point(500, 500), Point(500, 600), Point (600, 600), Point(600, 500))
gSqur.setFill(color_rgb(30, 230, 30))

orRomb = Polygon(Point(800, 100), Point(850, 200), Point (900, 100), Point(850, 0))
orRomb.setFill(color_rgb(255,165,0))

orRomb.draw(window)
gSqur.draw(window)
bTri.draw(window)



window.getMouse()
window.close()
