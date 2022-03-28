from tkinter import*

class Point:
     def __init__(self,Column_,Row_):
         self.Column=Column_
         self.Row=Row_  

class Paint:
    def __init__(self):        
        pass

    def PaintForm(self):
        window_width = 1000
        window_length = 800
        ob= Tk()
        self.canvas = Canvas(ob,width = window_width,height = window_length)
        ob.title('Snake')
        self.canvas.pack()
        ob.update()
        return  ob

    def PaintRectange(self,X0,Y0,X1,Y1,Color):
        self.canvas.create_rectangle(X0,Y0,X1,Y1,fill=Color)

class Setka:

    def __init__(self,dimesionSetka_,size_,paintobj_):
        self.CellsSetka=[]
        self.Color="Grey"
        self.dimesionSetka=dimesionSetka_
        self.size=size_
        self.sizeCell=self.size//self.dimesionSetka
        self.paintobj=paintobj_
        for i in range(self.dimesionSetka):
          for k in range(self.dimesionSetka):
             self.CellsSetka.append(Point(i,k))
     

    def FindPointOfColumnRow(self,Column_,Row_):
       return self.CellsSetka[Column_,Row_]

    def GetRect(p):

    def PaintSetka(self):
        for arrRow in self.CellsSetka:       
             self.paintobj.PaintRectange(GetRect(arrRow[]),(arrRow.Row+2)*self.sizeCell,(arrRow.Column+1)*self.sizeCell,(arrRow.Row+1)*self.sizeCell,'Blue')
    

class Snake:   
      def __init__(self,dimesionSnake_,owner_):
        self.Owner=owner_
        self.CellsSnake=[]

        self.Color="Blue"
        self.dimesionSnake=dimesionSnake_

      def SetPoinsForSnake(self,Col0,Row0):
          self.CellsSnake.clear
          self.CellsSnake.append(Point(Col0,Row0))
          self.CellsSnake.append(Point(Col0+1,Row0))
          self.CellsSnake.append(Point(Col0+2,Row0))
          self.CellsSnake.append(Point(Col0+3,Row0))
       

paint_=Paint()
ob=paint_.PaintForm()
setka=Setka(10,500,paint_)
setka.PaintSetka()
ob.mainloop()


