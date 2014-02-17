from PIL import Image
import sys
#Error check for input file goes here later.
     
im = Image.open(sys.argv[1])
im.copy()
im.size
width = im.size[0]
height = im.size[1]
print "***********************************\n"
print "MapClip will take the image \"" + str(sys.argv[1]) + "\" and break it up into many smaller images of equal size."
print "Your image is " + str(width) + "px wide and " + str(height) +"px tall."
     
newImage = 0
x=0
y=0
     
# Alpha offset procedure. A database of popular/useful image sizes is on the wishlist.
     
xOffset = input('Please input the width of each image. \n')
yOffset = input('Please input the height of each image. \n')

# A useful error check to prevent 0px images.
if xOffset >= 1 and yOffset >= 1:

# Verifies all images will be of equal size.

  if width % xOffset != 0:
    print "This would create images of unequal size. Try a different width."
    exit()
  
  if height % yOffset != 0:
    print "This would create images of unequal size. Try a different height."
    exit()


     
  while y < height:
    while x < width:
      newImage +=1
      img_crop = im.crop((x,y,x+xOffset,y+yOffset))
      img_crop.save (str(newImage), "PNG")
      x = x + xOffset
           
    x = 0
    y = y + yOffset
  print "There will be a total of " + str(newImage) +" images."
  print "Thanks for using MapClip!"
  exit()
     
     
else:
  print "Cannot create 0x0px files, sorry. That would destroy your hard drive, I think."
  exit()
