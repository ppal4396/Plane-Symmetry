

import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from tkinter.filedialog import askopenfilename
import math
import numpy as np


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Window")

        self.label = tk.Label(master, text="Canvas", fg = "light green")
        self.label.pack()

        self.symmetry = None
        self.imageChosen = False

        self.getImage_button = tk.Button(master, text="Choose an image",fg = "black",bg="white", command=self.getImage)
        self.getImage_button.pack()

        self.symmetry442_button = tk.Button(master, text="442 Symmetry",fg = "black",bg="white", command=self.choose442)
        self.symmetry442_button.pack()

        self.symmetryStar442_button = tk.Button(master, text="*442 Symmetry",fg = "black",bg="white", command=self.chooseStar442)
        self.symmetryStar442_button.pack()

        self.symmetry4Star2_button = tk.Button(master, text="4*2 Symmetry",fg = "black",bg="white", command= self.choose4Star2)
        self.symmetry4Star2_button.pack()

        self.symmetry2Star22_button = tk.Button(master, text="2*22 Symmetry",fg = "black",bg="white", command= self.choose2Star22)
        self.symmetry2Star22_button.pack()

        self.symmetry2222_button = tk.Button(master, text="2222 Symmetry",fg = "black",bg="white", command= self.choose2222)
        self.symmetry2222_button.pack()

        self.symmetry22Star_button = tk.Button(master, text="22* Symmetry",fg = "black",bg="white", command= self.choose22Star)
        self.symmetry22Star_button.pack()

        self.symmetryStar2222_button = tk.Button(master, text="*2222 Symmetry",fg = "black",bg="white", command= self.chooseStar2222)
        self.symmetryStar2222_button.pack()

        self.symmetry22x_button = tk.Button(master, text="22x Symmetry",fg = "black",bg="white", command= self.choose22x)
        self.symmetry22x_button.pack()

        self.symmetryStarx_button = tk.Button(master, text="*x Symmetry",fg = "black",bg="white", command= self.chooseStarx)
        self.symmetryStarx_button.pack()

        self.symmetryStarStar_button = tk.Button(master, text="** Symmetry",fg = "black",bg="white", command= self.chooseStarStar)
        self.symmetryStarStar_button.pack()

        self.symmetryxx_button = tk.Button(master, text="xx Symmetry",fg = "black",bg="white", command= self.choosexx)
        self.symmetryxx_button.pack()

        self.symmetryo_button = tk.Button(master, text="o Symmetry",fg = "black",bg="white", command= self.chooseo)
        self.symmetryo_button.pack()

        self.symmetry333_button = tk.Button(master, text="333 Symmetry",fg = "black",bg="white", command= self.choose333)
        self.symmetry333_button.pack()

        self.imagesLoaded = False


    def choose442(self):
        self.symmetry = "442"
    def chooseStar442(self):
        self.symmetry = "star442"
    def choose4Star2(self):
        self.symmetry="4star2"
    def choose2Star22(self):
        self.symmetry="2star22"
    def choose2222(self):
        self.symmetry="2222"
    def choose22Star(self):
        self.symmetry="22star"
    def chooseStar2222(self):
        self.symmetry="star2222"
    def choose22x(self):
        self.symmetry="22x"
    def chooseStarx(self):
        self.symmetry="starx"
    def chooseStarStar(self):
        self.symmetry = "starstar"
    def choosexx(self):
        self.symmetry = "xx"
    def chooseo(self):
        self.symmetry = "o"
    def choose333(self):
        self.symmetry = "333"

    def checkSymmetryAndImage(self):
        if self.symmetry!=None and self.imageChosen:
            if self.symmetry == "442":
                self.symmetry442(self.load)
            elif self.symmetry == "star442":
                self.symmetryStar442(self.load)
            elif self.symmetry == "4star2":
                self.symmetry4Star2(self.load)
            elif self.symmetry == "2star22":
                self.symmetry2Star22(self.load)
            elif self.symmetry == "2222":
                self.symmetry2222(self.load)
            elif self.symmetry == "22star":
                self.symmetry22Star(self.load)
            elif self.symmetry == "star2222":
                self.symmetryStar2222(self.load)
            elif self.symmetry=="22x":
                self.symmetry22x(self.load)
            elif self.symmetry=="starx":
                self.symmetryStarx(self.load)
            elif self.symmetry =="starstar":
                self.symmetryStarStar(self.load)
            elif self.symmetry == "xx":
                self.symmetryxx(self.load)
            elif self.symmetry == "o":
                self.symmetryo(self.load)
            elif self.symmetry == "333":
                self.symmetry333(self.load)

            self.imagesLoaded = True

    def getImage(self):
        filename = askopenfilename()
        load = Image.open(filename)
        size = (200, 200)
        load = load.resize(size)
        self.load = load
        self.imageChosen = True

    def symmetry333(self, image):
        # cut 1/3 of a hexagon with radius 100 out of square (200,200) image to
        # get a diamond shaped fundamental domain (fd)

        polygon = [(0,0), (87, 50), (87, 150), (0, 100)]
        fd = self.cutPolygon(image, polygon)
        # cut fd to size (87,150)
        box = [0,0,87,150]
        fd = fd.crop(box)
        # build hexagon cell by rotating fd thrice
        # See hexagonal cell on wikipedia for orientation.
        hexWidth = 87*2
        diamondWidth = math.ceil(math.sqrt(87**2 +50**2))
        hexHeight = 150+diamondWidth
        dst = Image.new("RGBA", (hexWidth, hexHeight))
        dst.paste(fd, (87,0))
        R = dst.rotate(120, center=(87*2,50))
        L = dst.rotate(120, center=(87, 100))
        LL = dst.rotate(240, center=(87,100))
        dst = self.imageStack(dst, R)
        dst = self.imageStack(dst, L)
        dst = self.imageStack(dst, LL)
        cell = dst
        self.tileHexagonalCell(cell, hexWidth, hexHeight, diamondWidth)

    def symmetryo(self, image):
        self.tile16SquareCells(image)

    def symmetryxx(self, image):
        # uses horizontal glides
        size = (100, 200)
        fd = image.resize(size)
        fdRotated = self.rotate(180, fd)
        cell = self.imageHorizontalStack(fd, fdRotated)
        self.tile16SquareCells(cell)

    def symmetryStarStar(self, image):
        # uses horizontal mirrors.
        size = (200, 100)
        fd = image.resize(size)
        fdFlipped = fd.transpose(Image.FLIP_TOP_BOTTOM)
        cell = self.imageVerticalStack(fdFlipped, fd)
        self.tile16SquareCells(cell)

    def symmetryStarx(self, image):
        triangle = [(0,200),(100,100),(200,200)] #bottom triangular quarter.
        fd = self.cutPolygon(image, triangle)
        fdFlipped = fd.transpose(Image.FLIP_TOP_BOTTOM)
        cell = self.imageVerticalStack(fdFlipped, fd) #cell.size = (200, 400)
        box = [0, 100, 200, 300]
        cell = cell.crop(box) #cell.size = (200, 200); boxed out around diamond.
        self.tileDiamondCell(cell)

    def symmetry22x(self, image):
        triangle = [(0,200),(100,100),(200,200)] #bottom triangular quarter.
        fd = self.cutPolygon(image,triangle)
        fdRotated = fd.rotate(180, fd)
        cell = self.imageVerticalStack(fdRotated, fd) #cell.size = (200, 400)
        box = [0, 100, 200, 300]
        cell = cell.crop(box) #cell.size = (200, 200); boxed out around diamond.

        # get top half of diamond
        box = [0, 0, 200, 100]
        top = cell.crop(box)
        # flip and slide left and right (into 200 x 200 square)
        topFlipped = top.transpose(Image.FLIP_TOP_BOTTOM)
        box = [100, 0, 200, 100]
        slideTopLeft = topFlipped.crop(box)
        cell.paste(slideTopLeft, (0,0), slideTopLeft)
        box = [0, 0, 100, 100]
        slideTopRight = topFlipped.crop(box)
        cell.paste(slideTopRight, (100, 0), slideTopRight)

        # get bottom half of diamond
        box = [0, 100, 200, 200]
        bottom = cell.crop(box)
        # flip and slide left and right (into 200 x 200 square)
        botFlipped = bottom.transpose(Image.FLIP_TOP_BOTTOM)
        box = [100, 0, 200, 100]
        slideBottomLeft = botFlipped.crop(box)
        cell.paste(slideBottomLeft, (0, 100), slideBottomLeft)

        box = [0, 0, 100, 100]
        slideBottomRight = botFlipped.crop(box)
        cell.paste(slideBottomRight, (100,100), slideBottomRight)

        self.tile16SquareCells(cell)


    def symmetryStar2222(self, image):
        fd = image
        fdHFlipped = fd.transpose(Image.FLIP_LEFT_RIGHT)
        bottom = self.imageHorizontalStack(fd, fdHFlipped)
        top = bottom.transpose(Image.FLIP_TOP_BOTTOM)
        cell = self.imageVerticalStack(bottom, top)
        size = (200, 200)
        cell = cell.resize(size)
        self.tile16SquareCells(cell)

    def symmetry22Star(self, image):
        # uses horizontal mirrors
        size = (200, 100)
        fd = image.resize(size)
        fdRotated = self.rotate(180, fd)
        bottom = self.imageHorizontalStack(fd, fdRotated)
        top = bottom.transpose(Image.FLIP_TOP_BOTTOM)
        cell = self.imageVerticalStack(bottom, top)
        size = (200, 200)
        cell = cell.resize(size)
        self.tile16SquareCells(cell)

    def symmetry2222(self, image):
        size = (200, 100)
        fd = image.resize(size)
        fdRotated = self.rotate(180, fd)
        cell = self.imageVerticalStack(fd, fdRotated)
        self.tile16SquareCells(cell)

    def symmetry2Star22(self, image):
        # bug: black line appears after second diagonal flip. Some problem with a mask/image paste in imageStack?
        triangle = [(0,200),(100,100),(200,200)]
        fd = self.cutPolygon(image,triangle)
        self.placeImage(fd, (0,0))
        fdDiagFlippedTopLeft = self.flipAcrossDiagonal(fd)
        triangleBottomRight = self.imageStack(fd, fdDiagFlippedTopLeft)
        triangleTopleft = self.flipAcrossDiagonal(triangleBottomRight, topLeft=False)
        cell = self.imageStack(triangleBottomRight, triangleTopleft)
        self.tile16SquareCells(cell)

    def symmetry4Star2(self, image):
        triangle = [(0,0),(200,0),(200,200)]
        fd = self.rotate(90, self.cutPolygon(image,triangle))
        fdDiagFlippedTopRight = self.flipAcrossDiagonal(fd, topLeft=False)
        cell = self.imageStack(fd, fdDiagFlippedTopRight)
        self.symmetry442(cell)

    def symmetryStar442(self, image):
        triangle = [(0,0),(200,0),(200,200)]
        fd = self.cutPolygon(image, triangle)
        fdDiagFlipped = self.flipAcrossDiagonal(fd)
        cell = self.imageStack(fd, fdDiagFlipped)
        self.symmetry442(cell)


    def flipAcrossDiagonal(self, image, topLeft=True):

        height = image.height
        width = image.width
        imArray = np.asarray(image)

        dstArray = np.empty(imArray.shape,dtype='uint8')

        if topLeft:
            # flips across mirror line top left to bottom right.
            for x in range(0, width, 1):
                for y in range(0, height, 1):
                    sourcePixel = imArray[x,y,:]
                    dstArray[y,x,:] = sourcePixel
        else:
            # flips across mirror line top right to bottom left.
            for x in range(0, width, 1):
                for y in range(0, height, 1):
                    sourcePixel = imArray[x,y,:]
                    dstArray[(width-1)-y,(height-1)-x,:] = sourcePixel
        imArray = 0
        dst = Image.fromarray(dstArray, "RGBA")
        return dst


    def imageHorizontalStack(self, im1, im2):
        dst = Image.new('RGBA', (im1.width + im2.width, im1.height))
        dst.paste(im1, (0,0))
        dst.paste(im2, (im1.width, 0))
        return dst

    def imageVerticalStack(self, im1, im2):
        dst = Image.new('RGBA', (im1.width, im1.height + im2.height))
        dst.paste(im2, (0,0))
        dst.paste(im1, (0, im2.height))
        return dst

    def imageStack(self, im1, im2):
        dst = Image.new('RGBA', (im1.width, im1.height))
        dst.paste(im1, (0, 0), im1)
        dst.paste(im2, (0,0), im2)
        return dst

    def cutPolygon(self, image, polygon):
        image = image.convert("RGBA")
        imArray = np.asarray(image)
        mask = Image.new('L',(imArray.shape[1], imArray.shape[0]), 0)
        ImageDraw.Draw(mask).polygon(polygon, outline=1,fill=1)
        mask = np.array(mask)
        newImArray = np.empty(imArray.shape,dtype='uint8')
        newImArray[:,:,:3] = imArray[:,:,:3]
        newImArray[:,:,3] = mask*255
        image = Image.fromarray(newImArray, "RGBA")
        return image

    def correctMask(self, image, coords):
        imArray = np.asarray(image)
        mask = Image.new('L', (imArray.shape[1], imArray.shape[0]),0)
        ImageDraw.Draw(mask).line(coords, width=1,fill=1)
        mask = np.array(mask)
        dstArray = np.empty(imArray.shape,dtype='uint8')
        dstArray[:,:,:] = imArray[:,:,:]
        dstArray[:,:,3] = mask*255
        dst = Image.fromarray(dstArray, "RGBA")
        return image


    def rotatePoint(self, point, angle, fixedPoint):
        angle = angle * (math.pi/180)

        x = int(((math.cos(angle) * (point[0] - fixedPoint[0])) - (math.sin(angle) *
        (point[1] - fixedPoint[1])) + fixedPoint[0]))

        y = int(((math.sin(angle) * (point[0] - fixedPoint[0])) - (math.cos(angle) *
        (point[1] - fixedPoint[1])) + fixedPoint[1]))

        return (x, y)

    def symmetry442(self, image):
        for k in range(2):
            for j in range(2):
                startX = j*400
                startY = k*400
                square = self.squareLatticePositions(startX,startY)
                for i in range(4):
                    self.placeImage(image, square[i])
                    image = self.rotate(270, image)


    def placeImage(self, image, pos):
        render = ImageTk.PhotoImage(image)
        img = tk.Label(self.master, image=render, borderwidth=0,highlightthickness=0)
        img['bg'] = img.master['bg']
        img.image = render
        img.place(x=pos[0],y=pos[1])

    def tile16SquareCells(self, cell):
        for k in range(2):
            for j in range(2):
                startX = j*400
                startY = k*400
                square = self.squareLatticePositions(startX,startY)
                for i in range(4):
                    self.placeImage(cell, square[i])

    def tileDiamondCell(self, cell):
        dst = Image.new('RGBA', (cell.width, cell.height))

        triangleTL = [(0, 100), (100, 0), (100,100)] #top left triangle cut
        quarterTLCopy = self.cutPolygon(cell, triangleTL)
        dst.paste(quarterTLCopy, (100,100), quarterTLCopy)

        triangleTR = [(100, 100), (100,0), (200,100)] #top left triangle cut
        quarterTRCopy = self.cutPolygon(cell, triangleTR)
        box=[100, 0, 200, 100]
        quarterTRCopy = quarterTRCopy.crop(box)
        dst.paste(quarterTRCopy, (0,100), quarterTRCopy)

        quarterBLandBRCopy = dst.transpose(Image.FLIP_TOP_BOTTOM)
        dst = self.imageStack(dst, quarterBLandBRCopy)
        dst = self.imageStack(dst, cell)
        self.tile16SquareCells(dst)

    def rotate(self, angle, image):
        load = image.rotate(angle)
        return load

    def tileHexagonalCell(self, cell, hexWidth, hexHeight, diamondWidth):
        dst = Image.new("RGBA", (800,800))
        stepX = hexWidth
        stepY = hexHeight-diamondWidth
        startY = 0 - stepY
        startX = 0
        layerCount = -1

        for y in range(startY,800,stepY):
            for x in range(startX,800,stepX):
                j = x
                k = y
                if layerCount%2!=0:
                    j -= math.ceil(hexWidth/2)
                    if j >= 800:
                        continue
                coords = (j,k)
                dst.paste(cell, coords, cell)
            layerCount+=1
        self.placeImage(dst, (0,0))

    def squareLatticePositions(self, startX, startY):
        squarePositions = np.asarray([[startX+0,startY+0],
                            [startX+200,startY+0],
                            [startX+200,startY+200],
                            [startX+0,startY+200]])
        return squarePositions

    def clearWhitePixels(self, image):
        data = image.getdata()
        newData = []
        for pixel in data:
            if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                newData.append((255,255,255,0))
            else:
                newData.append(pixel)
        image.putdata(newData)
        return image

def tick(my_gui):
    if my_gui.imagesLoaded == False:
        my_gui.checkSymmetryAndImage()


root = tk.Tk()
root.configure(background='black')
root.wm_attributes('-alpha',1)
my_gui = GUI(root)
root.geometry("800x800")
while True:
    root.update_idletasks()
    root.update()
    tick(my_gui)
