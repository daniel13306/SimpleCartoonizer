import cv2
import random
import os

# By DeadEagle
#
# www.Coding-Community.com
#
# https://discord.gg/FTmrYbEN8w

# Declaring Input and Output Folder Location's.
InputFileFolder = "Input\\"
OutputFileFolder = "Output\\"

try:
    os.mkdir("Input")
    print("Input Folder Made!")
except:
    pass

try:
    os.mkdir("Output")
    print("Output Folder Made!")
except:
    pass





# Declare filelist (Filelist = files in InputFileFolder)
filelist=os.listdir(InputFileFolder)
for fichier in filelist[:]: # For Each file in the Input Folder
    if not(fichier.endswith(".png")): # Check if FileFormat .png, otherwise Remove File from List.
        filelist.remove(fichier) # Remove non .png Files from the List
print(f"All PNG's Found: {filelist}") # Print the Final FileList

# For [i] = Each File in the Filelist, we will run the Functions Below.
for i in filelist:
    FileName = i
    img = cv2.imread(F"{InputFileFolder}{FileName}")

    # Set Edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 300, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Cartoonization
    color = cv2.bilateralFilter(img, 15, 500, 500)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    RandomNumber =  random.randrange(0,25)
    filenameImage = f"{OutputFileFolder}Image{RandomNumber}.png"
    filenameEdges = f"{OutputFileFolder}Edges{RandomNumber}.png"
    filenameCartoon = f"{OutputFileFolder}Cartoon{RandomNumber}.png"

    print("\nTo close Images quick, Press ESC")
    cv2.imshow("Image", img)
    cv2.imwrite(filenameImage, img)
    cv2.imshow("edges", edges)
    cv2.imwrite(filenameEdges, edges)
    cv2.imshow("Cartoon", cartoon)
    cv2.imwrite(filenameCartoon, cartoon)
    cv2.waitKey(0)
    print(f"Pictures saved in the Output Map. Files:\n{filenameImage}\n\n{filenameEdges}\n\n{filenameCartoon}\n")
    cv2.destroyAllWindows()


    # By DeadEagle
    #
    # www.Coding-Community.com
    #
    # https://discord.gg/FTmrYbEN8w
