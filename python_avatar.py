from PIL import Image


image=Image.open("example2.jpg")
RGB_image=image.convert("RGB")
red,blue,yolow = RGB_image.split()
red1=red.crop((100,0,red.width,red.height))
red2=red.crop((50,0,red.width-50,red.height))
red3=Image.blend(red1,red2,0.5)
blue1=blue.crop((100,0,red.width,red.height))
blue2=blue.crop((50,0,red.width-50,red.height))
blue3=Image.blend(blue1,blue2,0.5)
yolow1=yolow.crop((100,0,red.width,red.height))
new_image2=Image.merge("RGB",(red3,blue3,yolow1))
new_image2.thumbnail((80,80))
new_image2.save("new_image2.jpg")










