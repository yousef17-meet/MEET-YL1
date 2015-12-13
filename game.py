import meet
#ball1={"radius":2,"x":5,"y":5,"dx":1,"dy":0}
user_cell = {'radius':20,'x':8, 'y':8, 'dx':0.1, 'dy':0.1, 'color':'black', 'shape':'circle'}
cell1 = {'radius':18,'x':5, 'y':150, 'dx':1, 'dy':1, 'color':'blue', 'shape':'square'}
cell2 = {'radius':10,'x':10, 'y':10, 'dx':-2, 'dy':-2, 'color':'green', 'shape':'square'}
cell3 = {'radius':15,'x':7, 'y':-150, 'dx':8, 'dy':8, 'color':'red', 'shape':'square'}
cell4 = {'radius':14,'x':100, 'y':-200, 'dx':-0.6, 'dy':-0.6, 'color':'purple', 'shape':'square'}
cell5 = {'radius':25,'x':-100, 'y':200, 'dx':0.5, 'dy':0.5, 'color':'black', 'shape':'square'}
cell6 = {'radius':5,'x':150, 'y':-150, 'dx':0.3, 'dy':-0.3, 'color':'black', 'shape':'square'}
cell7 = {'radius':5,'x':125, 'y':-100, 'dx':-0.4, 'dy':0.4, 'color':'orange', 'shape':'square'}
cell8 = {'radius':5,'x':-150, 'y':100, 'dx':0.2, 'dy':-0.2, 'color':'yellow', 'shape':'square'}
cell9 = {'radius':5,'x':-125, 'y':50, 'dx':0.2, 'dy':0.2, 'color':'pink', 'shape':'square'}

cells=[]
#circle1=create_cell(ball1)
user_cell =meet.create_cell(user_cell)
cells.append(user_cell)

cell = meet.create_cell(cell1)
cells.append(cell)
cell = meet.create_cell(cell2)
cells.append(cell)
cell = meet.create_cell(cell3)
cells.append(cell)
cell = meet.create_cell(cell4)
cells.append(cell)
cell = meet.create_cell(cell5)
cells.append(cell)
cell = meet.create_cell(cell6)
cells.append(cell)
cell = meet.create_cell(cell7)
cells.append(cell)
cell = meet.create_cell(cell8)
cells.append(cell)
cell = meet.create_cell(cell9)
cells.append(cell)

#cells.append(circle1)


#def check_boarders (cells):
	#for cell in cells: 
		#erd=get_screen_width()
		#tool=get_screen_height()
		#sadi=ycor()
		#seeni=xcor()
		#if (seeni > erd):
			#cell.set_dx(-cell.get_dx())
		#if (sadi > tool):
			#cell.set_dy(-cell.get_dx())
def check_x_boarder(cells):
	width = meet.get_screen_width()
	for cell in cells:
		if cell.xcor() > width or cell.xcor() < -width:
			h1 = cell.get_dx()
			cell.set_dx(-h1)

def check_y_boarder(cells):
	height =meet.get_screen_height()
	for cell in cells:
		if cell.ycor() > height or cell.ycor() < -height:
			h2 = cell.get_dy()
			cell.set_dy(-h2)


while(True):
	move_cells(cells)
	check_x_boarder (cells)

while(True):
	move_cells(cells)
	check_y_boarder (cells)
meet.mainloop()

