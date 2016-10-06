import pyscreenshot as ImageGrab
import numpy
from PIL import Image
import sched, time

strName = "WebinarName"
numDelaySec = 5
numBorder = 0.8

numScreenShot = 0
s = sched.scheduler(time.time, time.sleep)

imScreenShot=ImageGrab.grab()
imScreenShot.save(strName+str(numScreenShot)+'.png')

def scrGrabber(sc,imScreenShot,numScreenShot): 
	print("Grabbing screenshot")
	imScreenShotNew=ImageGrab.grab()

	if (numpy.mean(numpy.array(imScreenShotNew)==numpy.array(imScreenShot))<numBorder):
		print("Saving screenshot")
		numScreenShot = numScreenShot + 1
		imScreenShotNew.save(strName+str(numScreenShot)+'.png')
		imScreenShot = imScreenShotNew

	s.enter(numDelaySec, 1, scrGrabber, (sc,imScreenShot,numScreenShot))

s.enter(numDelaySec, 1, scrGrabber, (s,imScreenShot,numScreenShot))
s.run()