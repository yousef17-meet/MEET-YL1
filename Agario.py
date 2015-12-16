import meet

import random
cells=[]
cells_nums=0
colors=["yellow","blue","red","green","purple","pink","orange"]
while cells_nums<30:
	balls={'radius':random.randint(0,30),'x':random.randint(-200,100),'y':random.randint(-200,100),'dx':random.randint(-2,2),'dy':random.randint(-2,2),'color':random.choice(colors)}


	cells_nums+=1
	circle=meet.create_cell(balls)
	cells.append(circle)

user_cell = {'radius':20,'x':500, 'y':500, 'dx':0.1, 'dy':0.1, 'color':'black', 'shape':'circle'}
#cell1 = {'radius':18,'x':5, 'y':150, 'dx':1, 'dy':1, 'color':'blue', 'shape':'square'}
#cell2 = {'radius':10,'x':10, 'y':10, 'dx':-2, 'dy':-2, 'color':'green', 'shape':'square'}
#cell3 = {'radius':15,'x':7, 'y':-150, 'dx':8, 'dy':8, 'color':'red', 'shape':'square'}
#cell4 = {'radius':14,'x':100, 'y':-200, 'dx':-0.6, 'dy':-0.6, 'color':'purple', 'shape':'square'}
#cell5 = {'radius':25,'x':-100, 'y':200, 'dx':0.5, 'dy':0.5, 'color':'black', 'shape':'square'}
#cell6 = {'radius':5,'x':150, 'y':-150, 'dx':0.3, 'dy':-0.3, 'color':'black', 'shape':'square'}
#cell7 = {'radius':5,'x':125, 'y':-100, 'dx':-0.4, 'dy':0.4, 'color':'orange', 'shape':'square'}
#cell8 = {'radius':5,'x':-150, 'y':100, 'dx':0.2, 'dy':-0.2, 'color':'yellow', 'shape':'square'}
#cell9 = {'radius':5,'x':-125, 'y':50, 'dx':0.2, 'dy':0.2, 'color':'pink', 'shape':'square'}

#cells=[]
user_cell = meet.create_cell(user_cell)
cells.append(user_cell)

#cell = meet.create_cell(cell1)
#cells.append(cell)
#cell = meet.create_cell(cell2)
#cells.append(cell)
#cell = meet.create_cell(cell3)
#cells.append(cell)
#cell = meet.create_cell(cell4)
#cells.append(cell)
#cell = meet.create_cell(cell5)
#cells.append(cell)
#cell = meet.create_cell(cell6)
#cells.append(cell)
#cell = meet.create_cell(cell7)
#cells.append(cell)
#cell = meet.create_cell(cell8)
#cells.append(cell)
#cell = meet.create_cell(cell9)
#cells.append(cell)

def check_border(cells):
	for cell in cells:
		width = meet.get_screen_width()
		height=meet.get_screen_height()
		if cell.xcor() > width or cell.xcor() < -width:
			h1 = cell.get_dx()
			cell.set_dx(-h1)
		if cell.ycor() > height or cell.ycor() < -height:
			h2 = cell.get_dy()
			cell.set_dy(-h2)



i = 1
a = 10
while True:
	print("working")
	x,y = meet.get_user_direction(user_cell)
	user_cell.set_dx(x)
	user_cell.set_dy(y)
	meet.move_cells(cells)
	check_border(cells)
	for cell2 in cells:
		if(cell2 != user_cell):
			a=user_cell.xcor()
			b=user_cell.ycor()
			r=user_cell.get_radius()
			c=cell2.xcor()
			d=cell2.ycor()
			r2=cell2.get_radius()
			if((a-c)**2 + (b-d)**2)**0.5 <= (r+r2):
				if(r>r2):
					cell2.goto(meet.get_random_x(),meet.get_random_y())
					user_cell.set_radius(r+0.001*r2)
				else:
					bye
			
	
meet.mainloop()	
	
