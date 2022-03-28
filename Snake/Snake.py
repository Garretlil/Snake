

arr=[]
for i in range(10):
    for k in range(10):
        arr.append('')



class Point:
     def __init__(self,x,y,color,direction):
         self.x=x
         self.y=y
         self.color=color
         self.direction=direction
         
class Setka:

    def __init__(self,dimesion_):
        self.Cells=[]
        self.dimesion=dimesion_
    def SetPoint(self,point):    
        self.Cells[point.x][point.y]=point
        

point=Point(5,6,'Blue','Right')
setka=Setka(arr)
setka.SetPoint(point)
print(setka)
