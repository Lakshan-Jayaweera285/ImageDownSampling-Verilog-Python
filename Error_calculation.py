# Image downsampling 

kh = np.array([1/4,1/2,1/4], np.float32) #chcanged this to int when compare integer arithmatic
kv = np.array([1/4,1/2,1/4], np.float32)

original_img = cv.imread("elon_musk.png",cv.IMREAD_GRAYSCALE)
imgpaded = cv.copyMakeBorder(original_img, 1, 1, 1, 1, cv.BORDER_CONSTANT,None, value = 0)

# Vertical Convolution
W1 = 250
H1 = 250

imgres = np.zeros((250,250),np.uint8)

for x in range(W1):
    for y in range(H1):
        tot1 = (imgpaded[y][x]*kv[0] + imgpaded[y+1][x]*kv[1] + imgpaded[y+2][x]*kv[2])
        imgres[y+1][x] = tot1

imglpf = np.zeros((250,250),np.uint8)

#Horizontal Convolution

W2 = 250
H2 = 250

for x in range(W2):
    for y in range(H2):
        tot = (imgres[x+1][y]*kh[0] + imgres[x+1][y+1]*kh[1] + imgres[x+1][y+2]*kh[2])
        imglpf[x][y] = tot

imgds = np.zeros((125,125),np.uint8)

#Downsampling
W3 = 125
H3 = 125
i = 0

for x in range(W3):
    j = 0
    for y in range(H3):
        imgds[x][y] = imglpf[i][j]
        j+= 2
    i+= 2

# Downsampled Image using processor

downsampled_img = open(output.txt","r")

rows = downsampled_img.read().splitlines()

img_array = np.zeros((125,125),np.uint8)

i = 0
for r in rows:
    pixels = r.split()
    j = 0
    for pixel in pixels[1:]:
        img_array[i][j] = pixel
        j += 1
    i += 1

# Calculating Error
width = 125
height = 125
Error = 0

for x in range(height):
    for y in range(width):
        Error += np.abs(imgds[x][y] - img_array[x][y])

print("Error per Pixel in integer domain: ", Error/(125*125))
