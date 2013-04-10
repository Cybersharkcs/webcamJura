#!/usr/bin/python

import urllib2
import re
from urlparse import urlsplit
from os.path import basename


# on recupere les donnees de l'url
usock = urllib2.urlopen("http://www.trinum.com/ibox/lelexcrozet/pageWebcam/")
htmlSource=usock.read()
usock.close()

imgUrls = re.findall('http://www.trinum.com/ibox/ftpcam/.*jpg*', htmlSource)
print imgUrls
for imgUrl in imgUrls:
    try:
        print imgUrl
        imgData = urllib2.urlopen(imgUrl).read()
        filename = basename(urlsplit(imgUrl)[2])
        print filename
        output = open("/home/maxime-pi/workspace/Webcamjura/images/"+"//"+filename,'wb')
        output.write(imgData)
        output.close()
    except:
        pass
