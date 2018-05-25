'''
Graphics Filters

By: Spencer Milbrandt

Created: 10/25/13
Last Modified: 10/27/13

This program is used to take an image that is decided by the user in 
the graphics_main.py. From there it filters the image in a graphical window depending 
on the choice the user determined and will display 2 windows. One of the Original Image 
and one of the new filtered image.
'''
from graphics import *

def save_image(img2):
	
	# This will ask the user if they would like to save the image. If they choose
	# Y it will save the image and if they choose N it will take them back to the filter
	# selection.
	
	save = input("\nWould you like to save the image? Y/N\n")
	if (save == "Y"):
		name = input("\nWhat would you like to name the file? (Include .gif)\n")
		img2.save(name)
		print("Image Saved as", name)
	elif (save == "N"):
		print("\nOk")
	else:
		print("\nIncorrect Input! - Image will not be saved!")

def display_grayscale(selection_file):
		
		# This pulls the selection_file and assigns it to img and img2 which are
		# then executed in the filter. This applies to every filter in the 
		# graphics_filters.py.
		
		# The try statement was to keep the program from crashing when running
		# only graphics_filters.py to test filters when creating the program. It
		# doesn't effect the overall program in any way. This applies to all the
		# filters in graphics_filters.py.
		
		try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			# This takes each row and column and changes the brightness to turn the pixels 
			# into a grayscale format.
		
			print("\nWorking...")
		
			row = 0
			column = 0
		
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
					img2.setPixel(row, column, color_rgb(brightness, brightness, brightness))
				
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file.
		
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Grayscale Filter", w + 2 * border, h + 2 * border)
		
			# Moves the image anchor point to the center of the window.
		
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
	
			# Draws the image to the window.
		
			img.draw(win)
			img2.draw(win2)
		
			print("\nDONE!")
			
			# Calls img2 to save_image where it uses the input to save or not to save
			# the image to a file. This applies to all the filters in graphics_filters.py.
			
			save_image(img2)
		
		except:
			print("")
			
def black_and_white(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			# This takes each row and column and changes the brightness to turn the pixels 
			# into a black and white format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					average = (r + g + b) / 3
					if average < 128:
						img2.setPixel(row, column, color_rgb(0, 0, 0))
					else:
						img2.setPixel(row, column, color_rgb(255, 255, 255))
						
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file.
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Black and White Filter", w + 2 * border, h + 2 * border)
		
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
		
			# Draws the image to the window.
			
			img.draw(win)
			img2.draw(win2)
			
			print("\nDONE!")
			
			save_image(img2)
		
	except:
		print("")
	
def red_tones(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			# This takes each row and column and changes the hue to turn the pixels 
			# into a red tone format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					r = r
					g = g * 0
					b = b * 0
					img2.setPixel(row, column, color_rgb(r, g, b))
					
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file.
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Red Tones Filter", w + 2 * border, h + 2 * border)
		
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
		
			# Draws the image to the window.
			
			img.draw(win)
			img2.draw(win2)
		
			print("\nDONE!")
			
			save_image(img2)
		
	except:
		print("")	
		
def green_tones(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			# This takes each row and column and changes the brightness to turn the pixels 
			# into a green tone format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					r = r * 0
					g = g 
					b = b * 0
					img2.setPixel(row, column, color_rgb(r, g, b))
					
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file.
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Green Tones Filter", w + 2 * border, h + 2 * border)
		
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
		
			# Draws the image to the window.
			
			img.draw(win)
			img2.draw(win2)
					
			print("\nDONE!")
 
			save_image(img2)
		
	except:
		print("")	
		
def blue_tones(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			# This takes each row and column and changes the brightness to turn the pixels 
			# into a blue tone format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					r = r * 0
					g = g * 0
					b = b 
					img2.setPixel(row, column, color_rgb(r, g, b))
			
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Blue Tones Filter", w + 2 * border, h + 2 * border)
			
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
			
			# Draws the image to the window.
			
			img.draw(win)
			img2.draw(win2)
		
			print("\nDONE!")
 
			save_image(img2)
		
	except:
		print("")

def posterize(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			# This takes each row and column and changes the brightness to turn the pixels 
			# into a posterize format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			# You can program a separate function to eliminate having to repeat
			# the if/elif statement for g and b but was having complications with
			# it. For the sake of time I did it this way to ensure no errors.
			
			for row in range(w):
				for column in range(h):
					r, g, b  = img.getPixel(row, column)
					if r <= 64:
						r = 32
					elif r <= 128:
						r = 96
					elif r <= 192:
						r = 160
					elif r <= 255:
						r = 223
					if g <= 64:
						g = 32
					elif g <= 128:
						g = 96
					elif g <= 192:
						g = 160
					elif g <= 255:
						g = 223
					if b <= 64:
						b = 32
					elif b <= 128:
						b = 96
					elif b <= 192:
						b = 160
					elif b <= 255:
						b = 223
					img2.setPixel(row, column, color_rgb(r, g, b))
					
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file.
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Posterizing Filter", w + 2 * border, h + 2 * border)
			
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
		
			# Draws the image to the window.
			
			img.draw(win)
			img2.draw(win2)
				
			print("\nDONE!")
					
			save_image(img2)
		
	except:
		print("")

def inverted(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			# This takes each row and column and changes the brightness to turn the pixels 
			# into an inverted format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					r = 255 - r
					g = 255 - g
					b = 255 - b
					img2.setPixel(row, column, color_rgb(r, g, b))
					
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Inverted Filter", w + 2 * border, h + 2 * border)
			
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
			
			# Draws the image to the window.
			
			img.draw(win)
			img2.draw(win2)
					
			print("\nDONE!")
 
			save_image(img2)
		
	except:
		print("")
		
def white_and_black(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			# This takes each row and column and changes the brightness to turn the pixels 
			# into a white and black format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					average = (r + g + b) / 3
					if average < 128:
						img2.setPixel(row, column, color_rgb(255, 255, 255))
					else:
						img2.setPixel(row, column, color_rgb(0, 0, 0))
						
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file.
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Black and White Filter", w + 2 * border, h + 2 * border)
		
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
		
			# Draws the image to the window.
			
			img.draw(win)
			img2.draw(win2)
							
			print("\nDONE!")
 
			save_image(img2)
		
	except:
		print("")

def hot_pink_awesomeness(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			# This takes each row and column and changes the hue to turn the pixels 
			# into a hot pink and cyan format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					average = (r + g + b) / 3
					if average < 128:
						img2.setPixel(row, column, color_rgb(255, 105, 180))
					else:
						img2.setPixel(row, column, color_rgb(0, 255, 255))
						
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file.
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("Hot Pink Awesomeness Filter", w + 2 * border, h + 2 * border)
		
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
		
			# Draws the image to the window.
			
			img.draw(win)
			img2.draw(win2)
			
			print("\nDONE!")
 
			save_image(img2)
		
	except:
		print("")

def cu_pride(selection_file):
	
	try:
			border = 30
		
			img = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
			
			img2 = Image(Point(0, 0), selection_file)
			w = img.getWidth()
			h = img.getHeight()
		
			# This takes each row and column and changes the brightness to turn the pixels 
			# into a CU Pride format.
			
			print("\nWorking...")
			
			row = 0
			column = 0
			
			for row in range(w):
				for column in range(h):
					r, g, b = img.getPixel(row, column)
					average = (r + g + b) / 3
					if average < 128:
						img2.setPixel(row, column, color_rgb(255, 215, 0))
					else:
						img2.setPixel(row, column, color_rgb(0, 0, 0))
						
			# Using the Image width and height, a window of correct size is created for
			# displaying the image file.
			
			win = GraphWin("Original Image", w + 2 * border, h + 2 * border)
			win2 = GraphWin("CU Pride Filter", w + 2 * border, h + 2 * border)
			
			# Moves the image anchor point to the center of the window.
			
			img.move(w // 2 + border, h // 2 + border)
			img2.move(w // 2 + border, h // 2 + border)
			
			# Draws the image to the window.
			
			img.draw(win)
						
			img2.draw(win2)
						
			print("\nDONE!")
 
			save_image(img2)
		
	except:
		print("")
