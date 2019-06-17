from Tkinter import *
import PIL
from PIL import Image, ImageDraw

#TODO: save a better resolution picture
def paint(event):
	global lastx, lasty
	global canvas_width, canvas_height
	x, y = event.x, event.y
	
	opp_lastx = canvas_width - lastx
	opp_x = canvas_height - x
	opp_lasty = canvas_width - lasty
	opp_y = canvas_height - y
	cv.create_line(lastx, lasty, x, y, fill="black")
	cv.create_line(opp_lastx, lasty, opp_x, y, fill="black")
	cv.create_line(opp_lastx, opp_lasty, opp_x, opp_y, fill="black")
	cv.create_line(lastx, opp_lasty, x, opp_y, fill="black")

	cv.create_line(lasty, lastx, y, x, fill="black")
	cv.create_line(lasty, opp_lastx, y, opp_x, fill="black")
	cv.create_line(opp_lasty, opp_lastx, opp_y, opp_x, fill="black")
	cv.create_line(opp_lasty, lastx, opp_y, x, fill="black")

	#drawing the identical lines on the PIL image
	draw.line((lastx, lasty, x, y), fill="black", width=1)
	draw.line((opp_lastx, lasty, opp_x, y), fill="black", width=1)
	draw.line((opp_lastx, opp_lasty, opp_x, opp_y), fill="black", width=1)
	draw.line((lastx, opp_lasty, x, opp_y), fill="black", width=1)

	draw.line((lasty, lastx, y, x), fill="black", width=1)
	draw.line((lasty, opp_lastx, y, opp_x), fill="black", width=1)
	draw.line((opp_lasty, opp_lastx, opp_y, opp_x), fill="black", width=1)
	draw.line((opp_lasty, lastx, opp_y, x), fill="black", width=1)

	lastx, lasty = x, y

def start_paint(event):
	global lastx, lasty
	lastx, lasty = event.x, event.y
	cv.bind("<B1-Motion>", paint)

def save():
	global image_number
	image_number += 1
	filename = "Eclipsis" + str(image_number) + ".jpg"
	image.save(filename)

def clear():
	global image, draw
	global canvas_width, canvas_height
	cv.delete("all")
	del draw
	image = PIL.Image.new("RGB", (canvas_width, canvas_height), "white")
	draw = ImageDraw.Draw(image)

master = Tk()
master.title("Eclipsis")

canvas_width = 700
canvas_height = 700

image_number = 1

# constructs new image to save later
image = PIL.Image.new("RGB", (canvas_width, canvas_height), "white")
# allows user to draw on this image (above the widget in layers)
draw = ImageDraw.Draw(image)

cv = Canvas(master, width = canvas_width, height = canvas_height)
cv.bind("<Button-1>", start_paint)
cv.pack(expand = YES, fill = BOTH)


save_button = Button(text = "Save", command = save, padx=4, pady=2)
save_button.pack(side=LEFT)
clear_button = Button(text = "Clear", command = clear)
clear_button.pack(side=RIGHT)

mainloop()

