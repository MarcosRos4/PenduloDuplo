from math import sin, cos, pi


class PenduloDuplo:

  def __init__(self, t1, t2, m1, m2, r1, r2, v1, v2, a1, a2, g):
    self.t1 = t1
    self.t2 = t2
    self.m1 = m1
    self.m2 = m2
    self.r1 = r1
    self.r2 = r2
    self.v1 = v1
    self.v2 = v2
    self.a1 = a1
    self.a2 = a2
    self.g = g

    self.x1 = self.r1 * sin(self.t1)
    self.y1 = self.r1 * cos(self.t1)

    self.x2 = self.x1 + self.r2 * sin(self.t2)
    self.y2 = self.y1 + self.r2 * cos(self.t2)  

    self.novaPosicao()

  def novaPosicao(self):
    print("Teta 1 = {0}\nTeta 2 = {1}\nVel 1 = {2}\nVel 2 = {3}\nAcc 1 = {4}\nAcc 2 = {5}\nX1 = {6}\nX2 = {7}\nY1 = {8}\nY2 = {9}".format(self.t1, self.t2, self.v1, self.v2, self.a1, self.a2, self.x1, self.x2, self.y1, self.y2))
    self.x1 = round(self.r1 * sin(self.t1), 6)
    self.y1 = round(self.r1 * cos(self.t1), 6)
                
    self.x2 = round(self.x1 + self.r2 * sin(self.t2), 6)
    self.y2 = round(self.y1 + self.r2 * cos(self.t2), 6)


    self.a1 = round(
      -1 * self.g * (2 * self.m1 + self.m2) * sin(self.t1) -
      self.m2 * self.g * sin(self.t1 - 2 * self.t2) -
      2 * sin(self.t1 - self.t2) * self.m2 *
      (self.t2 * self.t2 * self.r2 + self.t1 +
       self.t1 * self.r1 * cos(self.t1 - self.t2)) / self.r1 *
      (2 * self.m1 + self.m2 - self.m2 * cos(2 * self.t1 - 2 * self.t2)), 6)

    self.a2 = round(
      2 * sin(self.t1 - self.t2) * (self.t1 * self.t1 * self.r1 *(self.m1 + self.m2)) +
      self.g * (self.m1 + self.m2) * cos(self.t1) + self.t2 * self.t2 +
      self.r2 * cos(self.t1 - self.t2) /
      self.r2 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * self.t1 - 2 * self.t2)), 6)
    
    self.t1+=1
    self.t2+=1



    
    
p1 = PenduloDuplo(pi/2, pi/2, 10, 20, 30, 60, 1, 1, 1, 1, 9)
for i in range (50):
  p1.novaPosicao()
  
  
