from meet import *
ball1={"radius":2,"x":5,"y":5,"dx":1,"dy":0}

cells=[]
circle1=create_cell(ball1)

cells.append(circle1)


def check_boarders (cells):
	for cell in cells: 
		erd=get_screen_width()
		tool=get_screen_height()
		sadi=ycor()
		seeni=xcor()
		if (seeni > erd):
			cell.set_dx(-cell.get_dx())
		if (sadi > tool):
			cell.set_dy(-cell.get_dx())


while(True):
	move_cells(cells)
	check_boarders (cells)()

