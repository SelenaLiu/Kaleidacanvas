from Tkinter import *

def paint(event):
	global lastx, lasty
	x, y = event.x, event.y
	
	opp_lastx = 800 - lastx
	opp_x = 800 - x
	opp_lasty = 800 - lasty
	opp_y = 800 - y
	cv.create_line(lastx, lasty, x, y, fill="black")
	cv.create_line(opp_lastx, lasty, opp_x, y, fill="black")
	cv.create_line(opp_lastx, opp_lasty, opp_x, opp_y, fill="black")
	cv.create_line(lastx, opp_lasty, x, opp_y, fill="black")

	cv.create_line(lasty, lastx, y, x, fill="black")
	cv.create_line(lasty, opp_lastx, y, opp_x, fill="black")
	cv.create_line(opp_lasty, opp_lastx, opp_y, opp_x, fill="black")
	cv.create_line(opp_lasty, lastx, opp_y, x, fill="black")

	lastx, lasty = x, y

def start_paint(event):
	global lastx, lasty
	lastx, lasty = event.x, event.y
	cv.bind("<B1-Motion>", paint)


master = Tk()
master.title("Eclipsis")

canvas_width = 800
canvas_height = 800

cv = Canvas(master, width = canvas_width, height = canvas_height)
cv.pack(expand = YES, fill = BOTH)
cv.bind("<Button-1>", start_paint)

mainloop()

