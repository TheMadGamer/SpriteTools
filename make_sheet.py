from PIL import Image
import sys

if len(sys.argv) != 4:
    print 'make_sheet {args} {width} {height}'
    exit(0)

## Get frame range
frameRange = sys.argv[1]

[first,last] = frameRange.split('-')

[last, extension] = last.split('.')

numDigits = len(last)

rootString = first[0:len(first)-numDigits]

firstFrame = int(first[len(first)-numDigits: ])
lastFrame = int(last)

## Get the new sheet width and ht
width = int(sys.argv[2])
height = int(sys.argv[3])

# get sprite dims
testSprite = Image.open(str(rootString) + str(0).zfill(numDigits) + '.' + extension)
spriteSize = testSprite.size

print 'SpriteSize ', spriteSize

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
    
    print 'row', row, 'column', column
    
    box = (column * spriteSize, row*spriteSize, column * spriteSize + spriteSize, row*spriteSize + spriteSize)
    
    print box
    
    #write sprite
    newImage.paste(sprite, box)
    
#save newImage

newImage.save('spriteSheet.png')