
import math
x = 0.2
y = 9.59
z= 0.1
x1=0.85
y1=9.59
z1=-1.5
xreal=x-x1
yreal=y-y1
zreal=z-z1

result = (zreal*zreal)+(yreal*yreal)
result1=math.sqrt(result)
Ax=xreal/result1
degree= math.degrees(math.atan(Ax))
if degree < 0:
    degree = 180+degree

print degree