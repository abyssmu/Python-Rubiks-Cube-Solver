import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

red = [1,0,0]
green = [0,1,0]
blue = [0,0,1]
yellow = [1,1,0]
white = [1,1,1]
orange = [1,.5,0]
black = [0,0,0]

def cube(x, y, z,
		topFaceColor,
		bottomFaceColor,
		leftFaceColor,
		rightFaceColor,
		backFaceColor,
		frontFaceColor):
    glBegin(GL_TRIANGLES)
    glColor3f(frontFaceColor[0], frontFaceColor[1], frontFaceColor[2])  # N
    glVertex3f(x + .5, y + 1, z + .5)
    glVertex3f(x - .5, y + 1, z + .5)
    glVertex3f(x - .5, y,     z + .5)
    glVertex3f(x - .5, y,     z + .5)
    glVertex3f(x + .5, y,     z + .5)
    glVertex3f(x + .5, y + 1, z + .5)
    glColor3f(backFaceColor[0], backFaceColor[1], backFaceColor[2])  # S
    glVertex3f(x - .5, y + 1, z - .5)
    glVertex3f(x + .5, y + 1, z - .5)
    glVertex3f(x + .5, y,     z - .5)
    glVertex3f(x + .5, y,     z - .5)
    glVertex3f(x - .5, y,     z - .5)
    glVertex3f(x - .5, y + 1, z - .5)
    glColor3f(leftFaceColor[0], leftFaceColor[1], leftFaceColor[2])  # W
    glVertex3f(x + .5, y + 1, z - .5)
    glVertex3f(x + .5, y + 1, z + .5)
    glVertex3f(x + .5, y,     z + .5)
    glVertex3f(x + .5, y,     z + .5)
    glVertex3f(x + .5, y,     z - .5)
    glVertex3f(x + .5, y + 1, z - .5)
    glColor3f(rightFaceColor[0], rightFaceColor[1], rightFaceColor[2])  # E
    glVertex3f(x - .5, y + 1, z + .5)
    glVertex3f(x - .5, y + 1, z - .5)
    glVertex3f(x - .5, y,     z - .5)
    glVertex3f(x - .5, y,     z - .5)
    glVertex3f(x - .5, y,     z + .5)
    glVertex3f(x - .5, y + 1, z + .5)
    glColor3f(topFaceColor[0], topFaceColor[1], topFaceColor[2])  # U
    glVertex3f(x + .5, y + 1, z - .5)
    glVertex3f(x - .5, y + 1, z - .5)
    glVertex3f(x - .5, y + 1, z + .5)
    glVertex3f(x - .5, y + 1, z + .5)
    glVertex3f(x + .5, y + 1, z + .5)
    glVertex3f(x + .5, y + 1, z - .5)
    glColor3f(bottomFaceColor[0], bottomFaceColor[1], bottomFaceColor[2])  # D
    glVertex3f(x + .5, y, z - .5)
    glVertex3f(x + .5, y, z + .5)
    glVertex3f(x - .5, y, z + .5)
    glVertex3f(x - .5, y, z + .5)
    glVertex3f(x - .5, y, z - .5)
    glVertex3f(x + .5, y, z - .5)
    glEnd()

def createRubiks(x, y, z):
	#bottom layer
	#middle
	cube(x + 1, y + -1, z +0,
			black,
			white,
			red,
			black,
			black,
			black)
	cube(x + 0, y + -1, z + 0,
			black,
			white,
			black,
			black,
			black,
			black)
	cube(x + -1, y + -1, z + 0,
			black,
			white,
			black,
			orange,
			black,
			black)

	#front
	cube(x + 1, y + -1, z + 1,
			black,
			white,
			red,
			black,
			black,
			blue)
	cube(x + 0, y + -1, z + 1,
			black,
			white,
			black,
			black,
			black,
			blue)
	cube(x + -1, y + -1, z + 1,
			black,
			white,
			black,
			orange,
			black,
			blue)

	#back
	cube(x + 1, y + -1, z + -1,
			black,
			white,
			red,
			black,
			green,
			black)
	cube(x + 0, y + -1, z + -1,
			black,
			white,
			black,
			black,
			green,
			black)
	cube(x + -1, y + -1, z + -1,
			black,
			white,
			black,
			orange,
			green,
			black)

	#middle layer
	#middle
	cube(x + 1, y + 0, z + 0,
			black,
			black,
			red,
			black,
			black,
			black)
	cube(x + -1, y + 0, z + 0,
			black,
			black,
			black,
			orange,
			black,
			black)

	#front
	cube(x + 1, y + 0, z + 1,
			black,
			black,
			red,
			black,
			black,
			blue)
	cube(x + 0, y + 0, z + 1,
			black,
			black,
			black,
			black,
			black,
			blue)
	cube(x + -1, y + 0, z + 1,
			black,
			black,
			black,
			orange,
			black,
			blue)

	#back
	cube(x + 1, y + 0, z + -1,
			black,
			black,
			red,
			black,
			green,
			black)
	cube(x + 0, y + 0, z + -1,
			black,
			black,
			black,
			black,
			green,
			black)
	cube(x + -1, y + 0, z + -1,
			black,
			black,
			black,
			orange,
			green,
			black)

	#top layer
	#middle
	cube(x + 1, y + 1, z + 0,
			yellow,
			black,
			red,
			black,
			black,
			black)
	cube(x + 0, y + 1, z + 0,
			yellow,
			black,
			black,
			black,
			black,
			black)
	cube(x + -1, y + 1, z + 0,
			yellow,
			black,
			black,
			orange,
			black,
			black)

	#front
	cube(x + 1, y + 1, z + 1,
			yellow,
			black,
			red,
			black,
			black,
			blue)
	cube(x + 0, y + 1, z + 1,
			yellow,
			black,
			black,
			black,
			black,
			blue)
	cube(x + -1, y + 1, z + 1,
			yellow,
			black,
			black,
			orange,
			black,
			blue)

	#back
	cube(x + 1, y + 1, z + -1,
			yellow,
			black,
			red,
			black,
			green,
			black)
	cube(x + 0, y + 1, z + -1,
			yellow,
			black,
			black,
			black,
			green,
			black)
	cube(x + -1, y + 1, z + -1,
			yellow,
			black,
			black,
			orange,
			green,
			black)

def main():
	pygame.init()
	pygame.display.set_caption('3d Cube Example')
	display = (1200, 800)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

	glDepthMask(GL_TRUE)
	glDepthFunc(GL_LESS)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_CULL_FACE)
	glCullFace(GL_BACK)
	glFrontFace(GL_CCW)
	glShadeModel(GL_SMOOTH)
	glDepthRange(0.0,1.0)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		glClearColor(0.5, 0.5, 0.5, 1)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
		createRubiks(0, -1, -10)

		pygame.display.flip()
		pygame.time.wait(10)

main()