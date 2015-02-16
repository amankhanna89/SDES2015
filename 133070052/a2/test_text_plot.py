from text_plot import *

def test_plot():
  import math
  
  x=[]
  sin_x=[]
  
  steps= 40
  len_x= 2*(math.pi)
  
  interval = len_x/steps
  
  for j in range(steps):
    x.append(j*interval)
    sin_x.append(math.sin(x[j]))
  plot(sin_x,x)



if __name__=='__main__':
	test_plot()

