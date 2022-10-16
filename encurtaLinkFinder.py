# CODED BY:
#  github: mat1Vn
#  instagram: matheus000l
#
# DETAILS:
#
# a program made in python to look up Bit.ly link shortener urls
#
# this program generates random ids and does the concatenation with the base url
#
# I am not responsible for what you do with the urls found by this program


import requests
from random import randint
import string
import time

lc = list(string.ascii_lowercase)
uc = list(string.ascii_uppercase)
base = "https://bit.ly/"
idx = 0
mult = 1

with open("urlsds.txt", "a") as ff:
  while True:
    id = ""
    for i in range(0,7):
      cd = randint(1,3)
      if cd == 1:
        id += lc[randint(0,len(lc)-1)]
      if cd == 2:
        id += uc[randint(0,len(uc)-1)]
      if cd == 3:
        id += str(randint(0,9))
    idx += 1
    vr = 50*mult
    if idx == vr:
      print ("============"+str(idx)+"============")
      time.sleep(randint(5,10))
      mult+=1
    try:
      url = base+id
      req = requests.get(url)
      if req.status_code == 200:
        ff.write(f"URL: {url} \n")
        print (f"[{idx}] [{req.status_code}] - {url}")
    except:
      continue
