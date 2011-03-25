#!/usr/bin/env python

from PIL import Image
import sys, os, math

def get_dims(numFrames):

    root = math.pow(2,math.ceil(math.log(numFrames,2) ))

    root = math.pow(2,math.ceil(math.log(math.sqrt(root),2) ) ) 
    
    if( root * (root/2 ) >= numFrames):
        return (int(root), int(root/2))
    else:
        return (int(root), int(root))
    
def make_sheet(frameRange, spriteSheetName):

    [first,last] = frameRange.split('-')

    [last, extension] = last.split('.')

    numDigits = len(last)

    rootString = first[0:len(first)-numDigits]

    firstFrame = int(first[len(first)-numDigits: ])
    lastFrame = int(last)

    ## Get the new sheet width and ht
    (width, height) = get_dims(lastFrame+1)
    print 'width', width, 'height', height

    # get sprite dims
    testSprite = Image.open(str(rootString) + str(0).zfill(numDigits) + '.' + extension)
    spriteSize = testSprite.size

    #print 'SpriteSize ', spriteSize

    if spriteSize[0] != spriteSize[1]:
        print 'Invalid sprite size'
        exit(-1)

    spriteSize = spriteSize[0]    

    ## compute sheet size
    sheetSize = ( spriteSize * width, spriteSize *height)

    ## create new sheet
    newImage = Image.new( 'RGBA', sheetSize)

    for i in range(firstFrame, lastFrame+1):
    
        #load sprite
        spriteFile = str(rootString) + str(i).zfill(numDigits) + '.' + extension
        sprite = Image.open(spriteFile)
    
        #compute where to write
        row = int(round( i / width))
        column = i % width
    
        #print 'row', row, 'column', column
    
        box = (column * spriteSize, row*spriteSize, column * spriteSize + spriteSize, row*spriteSize + spriteSize)
    
        #print box
    
        #write sprite
        newImage.paste(sprite, box)
    
    #save newImage

    newImage.save(spriteSheetName)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'make_sheet {args}  [sprite_sheet_name]'
        exit(0)

    if len(sys.argv) == 3:
        spriteSheetName = sys.argv[2]
    else:
        dirName = os.getcwd()
        
        spriteSheetName = dirName.split('/')[-1] + '.png'

    ## Get frame range
    frameRange = sys.argv[1]
    
    make_sheet(frameRange, spriteSheetName)