import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

inCode = open("img_output.txt","r")
lines = inCode.readlines()

i = 0
for line in lines:
  lines[i] = int(line[:-1])
  i=i+1

print(lines)
print(len(lines))
inCode.close()

k =np.array(lines).reshape(125,125)
img = Image.fromarray(k)
img.save('Output_resized.png')
img.show()
