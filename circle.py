import math

radius = float(input('请输入半径:'))
perimeter=2*math.pi*radius
area=math.pi*radius*radius
V=4*math.pi*radius**3/3
print('周长：%.2f'%perimeter)
print('面积：%.2f'%area)
print('体积：%.2f'%V)