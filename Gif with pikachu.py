
from PIL import Image
images=["pikachu2.gif","pikachu3.gif","pikachu4.gif"]
all_images=[]
for arg in images:
    image=Image.open(arg)
    all_images.append(image)
all_images[0].save("Pikachu.gif", save_all=True, append_all_images=[images[1:]],duration=200,loop=0)
