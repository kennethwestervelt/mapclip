from PIL import Image

#Argument for input file goes here later.

print "This script will take the image ... and break it up into many smaller images of equal size."

newImage = 0
x=0
y=0
xOffset = input('Please input the length of each image. \n')
yOffset = input('Please input the height of each image. \n')
length = 100 #Sample number here. Add length.img later.
height = 100 #Sample number here. Add width.img later.

if xOffset >= 1 and yOffset >= 1:
#  xModulus = length % xOffset
#  yModulus = height % yOffset
#  if xModulus != 0 or yModulus !=0
#    print "This program cannot divide the image into unequal pieces."
#    sys.exit() 
  while y < height:
    while x < length:
      newImage +=1
      #more stuff here later
      x = x + xOffset
      
    x = 0
    y = y + yOffset
  print "There will be a total of " + str(newImage) +" images."
else:
  print "nope"
