from PIL import Image


image=Image.open("example2.jpg")
RGB_image=image.convert("RGB")
red,blue,green = RGB_image.split()
red1=red.crop((100,0,red.width,red.height))
red2=red.crop((50,0,red.width-50,red.height))
red3=Image.blend(red1,red2,0.5)
blue1=blue.crop((0,0,red.width-100,red.height-0))
blue2=blue.crop((50,0,red.width-50,red.height))
blue3=Image.blend(blue1,blue2,0.5)
green1=green.crop((50,0,red.width-50,red.height))
new_image2=Image.merge("RGB",(red3,green1,blue3))
new_image2.thumbnail((80,80))
new_image2.save("new_image2.jpg")










