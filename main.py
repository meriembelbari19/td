print('hello')


from collections import namedtuple
point1D = namedtuple('point1D', ['x'])

print(point1D)

p_04= point1D(0.4)
p_05= point1D(0.5)

print(p_04+p_05)


point2D = namedtuple('point2D', ['x','y'])

p2d = point2D(x=0, y=1)
print(p2d)

#Ce qu'on voudrait
#P04+P05 == point1D(0.9)

def ajout_point(point1,point2):
  x= point1[0]+point2[0]
  print(x)
  return point1D(x)

print(f'Addition ok: {ajout_point(p_04,p_05)}')
