import sys

class PlotException(Exception):
    pass

class make_canvas_class(object):
  def __init__(self,size):
      self.cols, self.rows = size
      self.canvas = []
      for i in range(0, self.cols):
	  self.canvas.append(list(' '*self.rows))
  def return_canvas(self):
      return self.canvas

class plot_canvas_class(object):
  def __init__(self,canvas,output_file):
    self.canvas=canvas
    self.output_file=output_file
    pass
  def plot_canvas(self):
      for line in self.canvas[::-1]:
	  self.output_file.write(''.join(line))
	  self.output_file.write('\n')
        
class map_point_class(object):
  def __init__(self,x, y, xmin, ymin, xmax, ymax, size):
      """Return a pair of indices corresponding to
      the point x, y in the domain (xmin,...)
      """
      self.len_x = float(xmax - xmin)
      self.len_y = float(ymax - ymin)
      self.xi = int(round((x - xmin)/self.len_x*(size[1]-1)))
      self.yi = int(round((y - ymin)/self.len_y*(size[0]-1)))
  def return_map_point(self):
    return self.xi, self.yi

class plot(PlotException):
  def __init__(self,x_a, y_a, size=(80, 30), output_file=sys.stdout):
      if len(x_a) != len(y_a):
	  self.msg = "Input arrays have different lengths %d and %d"%(len(x_a), len(y_a))
	  raise PlotException(msg)
      self.xmin, self.xmax = min(x_a), max(x_a)
      self.ymin, self.ymax = min(y_a), max(y_a)

      self.obj_canvas = make_canvas_class(size)
      self.canvas = self.obj_canvas.return_canvas()

      self.n = len(x_a)
      for i in range(self.n):
	  self.x, self.y = x_a[i], y_a[i]
	  self.obj_xiyi= map_point_class(self.x, self.y, self.xmin, self.ymin, self.xmax, self.ymax, size)
	  self.xi,self.yi=self.obj_xiyi.return_map_point()
	  self.canvas[self.yi][self.xi] = '*'

      p=plot_canvas_class(self.canvas,output_file)
      p.plot_canvas()
      