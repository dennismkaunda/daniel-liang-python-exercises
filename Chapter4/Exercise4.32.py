# 4.32 (Geometry: point on line segment
x0, y0, x1, y1, x2, y2 = eval(input("Enter the coordinates for the three points p0, p1, and p2: "))

d = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if d <= 0.0000000001 and ((x0 <= x2 and x2 <= x1) or (x0 >= x2 and x2 >= x1)):
    print("(" + str(x2) + ", " + str(y2) + ") is on the line segment from (" + str(x0) + ", " + str(y0) + ") to ", "(" + \
          str(x1) + ", " + str(y1) + ")")
else:
    print("(" + str(x2) + ", " + str(y2) + ") is not on the line segment from (" + str(x0) + ", " + str(y0) + ") to ", "(" + \
          str(x1) + ", " + str(y1) + ")")
