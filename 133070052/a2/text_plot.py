def plot(x,y,x_row=29,y_column=79):  
  if type(x) is tuple or list:
    x_min=min(x)
    x_max=max(x)
  else:
    raise TypeError,"Error:x is not list or tuple "
  
  if type(y) is tuple or list:
    y_min=min(y)
    y_max=max(y)
  else:
    raise TypeError,"Error:y is not list or tuple "
  
  x_shift=[]
  y_shift=[]
  if x_min<0:
    for i in range(len(x)):
      x_shift.append(x[i]-x_min)
  else:
    x_shift=x
    
  if y_min<0:
    for i in range(len(y)):
      y_shift.append(y[i]-y_min)
  else:
    y_shift=y
  
  print x_shift
  print y_shift
  x_max=max(x_shift)
  y_max=max(y_shift)
  
  min_length=min(len(x_shift),len(y_shift))
  
  x_plot=[]
  y_plot=[]
  p=[]
  
  for i in range(min_length):
    x_abs= abs(int(round((x_shift[i]*x_row)/x_max)))
    y_abs= abs(int(round(((y_shift[i])*y_column)/y_max)))
    x_plot.append(x_abs)
    y_plot.append(y_abs)
  
  
  print x_plot
  print y_plot
  for i in range(x_row+1):
    for j in range(y_column+1):
      p.append(' ')
    p.append('\n')
  print len(p)
  print min_length
  print y_column
  for i in range(min_length):    
    print y_plot[i]+(y_column+1)*x_plot[i]
    p[y_plot[i]+(y_column+2)*x_plot[i]]='*'
  
  q=[]
  k=[]
  for j in reversed(range(x_row+1)):
    for i in range(y_column+2):
      q.append(p[i+(y_column+2)*j])
    k.append(''.join(q))
    q=[]
  
  print ''.join(k)
  
