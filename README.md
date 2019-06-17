# Kaleidacanvas

This script was a small experimentation with tkinter's canvas, and in general, a GUI for python.

Using the Kaleidacanvas, users may create their own ecliptical (or otherwise) kaleidascope patterns! Some examples are shown below:

![Example1](https://github.com/SelenaLiu/Kaleidacanvas/blob/master/Images/Eclipsis1.jpg)
![Example2](https://github.com/SelenaLiu/Kaleidacanvas/blob/master/Images/Eclipsis2.jpg)
![Example3](https://github.com/SelenaLiu/Kaleidacanvas/blob/master/Images/Eclipsis3.jpg)


For more examples you can look in the Images folder.

### Libraries used
Tkinter, Pillow: Image and ImageDraw. The latter was used to help save the Kaleidapiece you made, but a problem that
I have yet to solve is the quality of the image PIL saves. I am using the mode `RGB`, but I also tried other modes compatible 
with the file format `.jpg` prescribed on [this page](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes), but none of them turned out any more satisfactory. One reason that does not include the fault of Pillow would be the fact that Kaleidacanvas's canvas is only 700x700 pixels, restricting the saved image's quality.

Overall, I am much more interested by Tkinter's abilities as a GUI, and if I were to improve on the current version of Kaleidacanvas, I would look at different image-saving libraries that would allow for higher quality images.

### Potential Features
Some features that I would want to explore with this project is adding a slider of some sort to adjust brush size and a colour palette to allow for more user customability.

Also, while I was debugging, I accidentally made a feature that made some wicked-looking kaleidapieces (the name's really catching on) by extending lines from the initial button click. An example is shown below.

![kaleidapiece](https://github.com/SelenaLiu/Kaleidacanvas/blob/master/Images/Screen%20Shot%202019-06-16%20at%201.10.26%20PM.png)

### Useful resources
Some resources that I definitely relied on while learning to use Tkinter and Pillow are listed below:

1. The [very basic](https://www.python-course.eu/tkinter_canvas.php) canvas overview
1. Another basic canvas [overview](http://effbot.org/tkinterbook/canvas.htm).
1. An extremely helpful person on [StackOverflow](https://stackoverflow.com/questions/52146562/python-tkinter-paint-how-to-paint-smoothly-and-save-images-with-a-different) that helped make the lines continuous on the canvas. 
    Please note: there was no copy and pasting happening here.
1. A [page](https://www.tutorialspoint.com/python/tk_pack.htm) to understand the basic functions of tkinter's canvas.
1. A [complete outline](https://pillow.readthedocs.io/en/stable/reference/Image.html#attributes) of all of Pillow's Image functions that proved to be interesting and insightful.
