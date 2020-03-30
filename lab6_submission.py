import a1lab6 



#Task1 : takes object p of Point class and l of Line class and overwrites the x and y coordinate of the point with the coordinates of its mirror image

def findMirrorPoint(p,l):
	p.x = p.x - 2* l.a * (l.a*p.x + l.b*p.y + l.c)/(l.a **2 + l.b**2)  #x-coordinate of mirror image
	p.y = p.y - 2* l.b * (l.a*p.x + l.b*p.y + l.c)/(l.a **2 + l.b**2)  #y-coordinate of mirror image
	return p.x , p.y                     


#Task2: checking if the mirror image of Point p1 wrt Line l1 and Point p2 lie on the same side of Line l2 


def checkSides(p1,p2,l1,l2):
	g = ((p1.x * (l1.b**2 - l1.a**2)) - 2*l1.a*((l1.b * p1.y) + l1.c)) / (l1.a**2 + l1.b**2)  #x-coordinate of mirror image
	h = ((p1.y * (l1.a**2 - l1.b**2)) - 2*l1.b*((l1.a * p1.y) + l1.c)) / (l1.a**2 + l1.b**2)  #y-coordinate of mirror image
	if (((l2.a * g) + (l2.b * h) + l2.c) * ((l2.a * p2.x) + (l2.b * p2.y) + l2.c) > 0):                   #Logic: if both points lie on the same side of the line, their product on inserting the value of the points into the line will be positive
		return True    # gives true for only those cases when they lie on the same side
	else:
		return False   


#Task3: checking if Circle c1 and c2 are intersecting or not


def checkIntersection(c1, c2):
	r = c1.centre_x 
	t = c1.centre_y
	q = c2.centre_x
	w = c2.centre_y
	r1 = c1.radius
	r2 = c2.radius
	d = ((r-q)**2 + (t-w)**2)** 0.5    #checks distance between the centres by distance formula
	if(d < (r1+r2)):
		return True
	else:
		return False
