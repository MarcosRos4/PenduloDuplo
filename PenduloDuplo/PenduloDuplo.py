from math import sin, cos

class PenduloDuplo:

  def __init__(self, t1, t2, m1, m2, r1, r2, g):
    self.t1 = t1
    self.t2 = t2
    self.m1 = m1
    self.m2 = m2
    self.r1 = r1
    self.r2 = r2
    self.v1 = 0
    self.v2 = 0
    self.g = g


    self.novaPosicao()

  def novaPosicao(self):
    
    num1 = -self.g * (2 * self.m1 + self.m2) * sin(self.t1)
    num2 = -self.m2 * self.g * sin(self.t1 - (2 * self.t2))
    num3 = -2 * sin(self.t1 - self.t2) * self.m2
    num4 = self.v2 * self.v2 * self.r2 + self.v1 * self.v1 * self.r1 * cos(self.t1 - self.t2)
    den =  self.r1 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * self.t1 - 2 * self.t2))

    self.a1 = (num1+num2+num3*num4)/den
    
    num1 =  2 * sin(self.t1 - self.t2)
    num2 = (self.v1 * self.v1 * self.r1 *(self.m1 + self.m2)) 
    num3 = self.g * (self.m1 + self.m2) * cos(self.t1)
    num4 = self.v2 * self.v2 * self.r2 * self.m2 * cos(self.t1 - self.t2)
    den  = self.r2 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * self.t1 - 2 * self.t2))

    self.a2 = (num1*(num2+num3+num4))/den

    self.x1 = 300 + self.r1 * sin(self.t1)
    self.y1 = 200 + self.r1 * cos(self.t1)
                
    self.x2 = self.x1 + self.r2 * sin(self.t2)
    self.y2 = self.y1 + self.r2 * cos(self.t2)    

    self.v1 += self.a1
    self.v2 += self.a2

    self.t1 += self.v1
    self.t2 += self.v2

    #self.v1 *= 0.999
    #self.v2 *= 0.999

    print("Teta 1 = {0}\nTeta 2 = {1}\nVel 1 = {2}\nVel 2 = {3}\nAcc 1 = {4}\nAcc 2 = {5}\nX1 = {6}\nX2 = {7}\nY1 = {8}\nY2 = {9}".format(self.t1, self.t2, self.v1, self.v2, self.a1, self.a2, self.x1, self.x2, self.y1, self.y2))
