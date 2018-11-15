import sys
import os
from .trainer import trainer

options = "1. take photo\n2. train system\n3. arm system\n4. exit"
cascade = "shop/camigo/haarcascade_frontalface_default.xml"
imageRoot= "shop/camigo/images"

# def run():    
#     while True:
#         print ("\n----------camera with face regcognition----------------")

#         prompt = ("select an option:\n{0}\ncamigo:\\>")
#         option = input(prompt.format(options))
#         if option == "4":
#             print ("see you later mater")
#             break2
#         elif option == "3":
#             armSystem()
#         elif option == "2":
#             trainSystem()
#         elif option == "1":
#             setUpFace()

def trainSystem():    
    t = trainer(imageRoot, cascade)
    t.train()
    pass

def armSystem():
    print ("arming system")
    from .watcher import watcher
    watcher = watcher(imageRoot, cascade)
    watcher.watch()
    pass


def setUpFace(data):
    name = data
    # name = input("enter your name (letters only, no space):\ncamigo:\\>")    
    imageLocation =  os.path.join(imageRoot, name)
    if not os.path.exists(imageLocation):
        os.makedirs(imageLocation)
    
    print ("please stand in front of the camera for a moment, be natural and try different facial expressions")
    from .photographer import photographer
    photographer = photographer(imageLocation, cascade)
    photographer.shoot(10)

# run()