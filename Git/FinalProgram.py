#Firstly I Have Imported Open CV using Following Statement.
import cv2

#Exact Location of My Image, Where It Presented.

path = r'C:\Users\Kathirvel BE\Documents\AI-Internship\Day-3\OpenCV-Basics\Images\PantechAI.png'

#I Created a variable to Specify above Specified Image.

OldImage = cv2.imread(path)

#Similarlty Variables for image properties also printed.

OldImageSize = OldImage.size
OldImageShape = OldImage.shape
OldImageType = OldImage.dtype


window_Description_Old = "Interface Of Master Class."

#Path Specified image is Displayed With the help of imshow() method.

cv2.imshow(window_Description_Old, OldImage)

#Properties of Images Get's Printed.

print("Size Of Old Image is {0}, Shape is {1} and Type is {2} ".format(OldImageSize, OldImageShape, OldImageType))

#New Variable is Created By Changing Color Of Original image into HIghly Huge Saturation Value using 'cvrColor()' method.


NewImage = cv2.cvtColor(OldImage, cv2.COLOR_BGR2HSV)


NewImageSize = NewImage.size
NewImageShape = NewImage.shape
NewImageType = NewImage.dtype


window_Description_New = "Interface Of Master Class image is Convertted into Huge and Saturation Valued."

cv2.imshow(window_Description_New, NewImage)


print("Size Of New Image is {0}, Shape is {1} and Type is {2} ".format(NewImageSize, NewImageShape, NewImageType))

#The Color converted image is Stored using 'imwrite()' method.



cv2.imwrite("HSVInterfaceOfMasterClass.png", NewImage)

#Finally WaitKey is Said to be 0 'because its going to be infinite amount of time'.


cv2.waitKey(0)

#Then destroyAllWindows() method is used to exit from output screen.

cv2.destroyAllWindows()


