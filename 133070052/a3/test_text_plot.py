from text_plot import plot
import unittest

class TestPlotFunction(unittest.TestCase):
  def setUp(self):
    print 'In setUp'
    
  def tearDown(self):
    print 'In tearDown'
    
  def test_plot(self):
    import math
    self.x=[]
    self.sin_x=[]
  
    self.steps= 30
    self.len_x= 2*(math.pi)
  
    self.interval = self.len_x/self.steps
    self.size=(20,80)
    for i in range (0,self.steps):
      self.x.append(i*self.interval)
      self.sin_x.append(math.sin(self.x[i]))
    plot(tuple (self.x), tuple (self.sin_x),self.size)
       
    
    
if __name__ == '__main__':
    unittest.main()