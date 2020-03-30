import lab6_submission
import introcs
import a1lab6


obj1 = Point(2,3)			
line1 = Line(1,0,0)
A = str(findMirrorPoint(obj1, line1)) #test case 1 for findMirrorPoint

obj2 = Point(-1, -1)
line2 = Line(1, -1, 0)
B = str(findMirrorPoint(obj2, line2))  #test case 2 for findMirrorPoint(checking when mirror image lies on the line)

obj3 = Point(2,1)
obj4 = Point(5,1)
line3 = Line(1, -1, 0)
line4 = Line(1, -1, 2)
C = str(checkSides(obj3,obj4,line3,line4))   #test case1 for checkSides

obj5 = Point(-1,1)
obj6 = Point(4,1)
line5 = Line(1, -1, 0)
line6 = Line(1, -1,2)
D = str(checkSides(obj5,obj6,line5,line6))   #test case2 for checkSides(when mirror image of p1 lies on l2)

c1 = Circle(-1,0,1)
c2 = Circle(1,0,1)
E = checkIntersection(c1,c2)        #test case 1 for checkIntersection(when the circles are just touching each other at one point)

c3 = Circle(2,0,2)
c4 = Circle(3,0,2)
F = checkIntersection(c3,c4)   #test case 2 for checkIntersection(when the circles are touching each other externally)

introcs.assert_equal('(2,3)',A)
introcs.assert_equal('(-1,-1)',B)

introcs.assert_equal(False ,C)
introcs.assert_equal(True ,D)
 
introcs.assert_equal(True ,E)
introcs.assert_equal(False ,E)
introcs.assert_equal(True ,F)
introcs.assert_equal(False ,F)
