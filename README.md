# Implementation-practice
<br>
<br>

## OpenCV Practice

### 1, 2, and 3: Load single image, video and display them
<img src="https://user-images.githubusercontent.com/102780764/168073114-06c1e840-d3d1-44de-b8a7-ea60ced869ba.png" width="400px" alt="building"/>
1st frame of the video:
<img src="https://user-images.githubusercontent.com/102780764/168078779-4aed10b2-0b2e-4159-9f6e-dd4f008adffb.jpg" width="400px">
<br>

### 4: Load color image and swap RGB channels
swap R channel and B channel:  
<img src="https://user-images.githubusercontent.com/102780764/168079470-ee294b7a-2ae1-4707-a14f-7491e85d2a3f.png" width="400px">
<br>

### 5: Load color image and rotate it 45degrees
Rotate 45 degrees = input -45:
```
rows, cols, _ = original.shape
matrix = cv.getRotationMatrix2D((cols/2, rows/2), -45, 1)
img_45rotation = cv.warpAffine(original, matrix, (cols, rows))
```

Result:  
<img src="https://user-images.githubusercontent.com/102780764/168079750-7971da63-6171-4cc8-9156-95c091640b7c.png" width="400px">
<br>

### 6: Load color image and convert it to grayscale (cvtColor)
<img src="https://user-images.githubusercontent.com/102780764/168079274-15772f20-842f-488a-b2e7-a8cecfae986e.png" width="400px">
<br>

### 7: Detect edges in a grayscale image (Sobel, Laplacian, Canny)
>* **Sobel Result:**  
><img src="https://user-images.githubusercontent.com/102780764/168081704-013a885c-e3bc-4b40-80e1-c021a91d5087.png" width="400px">

>* **Laplacian Result:**  
><img src="https://user-images.githubusercontent.com/102780764/168085955-9dcb9488-d288-48bd-9272-501f5c7c3339.png" width="400px">

>* **Canny Result:**  
><img src="https://user-images.githubusercontent.com/102780764/168086207-39e18439-987b-4625-9858-88e343d14f60.png" width="400px">
<br>

### 8 and 9: Add random noise in a grayscale image and Remove the noise
In this practice, I choose the gaussian white noise mostly used in Image Processing.
>* Noisy Image:  
><img src="https://user-images.githubusercontent.com/102780764/168087111-3ccebaaa-d14c-4412-900e-bed84592ccc5.png" width="400px">

<br>

>* Remove the noise by **GaussianBlur filter** (Each pixel's new value is set to a weighted average of that pixel's neighborhood. The original pixel's value receives the heaviest weight (having the highest Gaussian value) and neighboring pixels receive smaller weights as their distance to the original pixel increases.):   
><img src="https://user-images.githubusercontent.com/102780764/168087679-6c3c1907-6494-40af-8e14-ec011f28237a.png" width="400px">
<br>

### 10: Binarize a grayscale image. Add track bar GUI to change the threshold

[![IMAGE ALT TEXT](https://user-images.githubusercontent.com/102780764/168092318-57ad4dd5-dbbd-4010-be62-c8a32fe9ab8d.jpg)](https://www.youtube.com/shorts/r85rYPpTfts "Unity Snake Game")
<br>

### 11: Apply labeling operation to a binarized image
* Binary image:
<img src="https://user-images.githubusercontent.com/102780764/168094047-7a68358b-bb84-4334-aa27-0f8cbe094efd.png" width="400px">
Apply labeling operation:  

```
num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(binary_im, connectivity=8)
```  

And we can obtain the label information:  

```
num_labels =  1728
stats =  [[     0      0    550    657 172668]
 [     0      0    550    629 146541]
 [   148      0      2      1      2]
 ...
 [   388    650     14      7     51]
 [   223    652      3      5     14]
 [   263    656      1      1      1]]
centroids =  [[271.93807191 394.54135103]
 [277.36778785 222.57719   ]
 [148.5          0.        ]
 ...
 [394.17647059 653.68627451]
 [223.92857143 654.14285714]
 [263.         656.        ]]
labels =  [[1 1 1 ... 1 1 1]
 [1 1 1 ... 1 1 1]
 [1 1 1 ... 1 1 1]
 ...
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]]
```  
* Labeled image:
<img src="https://user-images.githubusercontent.com/102780764/168094154-7ea922ef-0949-43c6-bae3-a9a433098afd.png" width="400px">
<br>

### 12, 13 and 14:
* __Do single-camera calibration and get intrinsic & extrinsic parameters__
* __Display the reprojected points on the captured image based on the estimated parameters in single-camera calibration__
* __Obtain the pose of camera and draw object-coordinate system on the observed target__

In this part, I first simply choose a chessboard (7×7) downloaded from the Internet.

```
    # 标定
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    print("Camera Matrix : \n") # 内参矩阵
    print(mtx)
    print("Distortion Parameters : \n")
    print(dist)
    print("Rotation Vectors : \n")
    print(rvecs)
    print("Translate Vectors: \n")
    print(tvecs)
```  
Result:  
<img src="https://user-images.githubusercontent.com/102780764/168097408-d628509f-9449-44ba-b07c-7913b428e112.png" width="400px">

<br>
<br>

## OpenGl  Practice

<br>
<br>

### Tutorial 1 : Opening a window

Open a window with size (800×600):

```
window = glfw.create_window(800, 600, "Test_window", None, None)
``` 

<img src="https://user-images.githubusercontent.com/102780764/168099686-f1362921-a14f-4cb7-93e7-98dde616c747.png" width="400px">
<br>

### Tutorial 2 : The first triangle
The graphics pipeline can be divided into two large parts: the first transforms your 3D coordinates into 2D coordinates and the second part transforms the 2D coordinates into actual colored pixels.  
<img src="https://user-images.githubusercontent.com/102780764/168101871-36551226-715e-495a-9bc7-e3bcf5792268.png" width="600px">

Three axis：x, y-axis are normal, z-axis is perpendicular to the screen, pointing in the direction behind us.

```
	vertex_data = [-1.0, -1.0, 0.0,
			1.0, -1.0, 0.0,
			0.0,  1.0, 0.0]
``` 
<img src="https://user-images.githubusercontent.com/102780764/168100125-0b0ca01d-e486-45b0-a042-4174e7fb5ed3.png" width="400px">
<br>

### Tutorial 3 : Matrices

```
	# Projection matrix : 45 Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
	projection = mat4.perspective(45.0, 4.0 / 3.0, 0.1, 100.0)
	
	# Camera matrix
	view = mat4.lookat(vec3(4,3,3), # Camera is at (4,3,3), in World Space
					vec3(0,0,0), # and looks at the origin
					vec3(0,1,0)) 
	
	# Model matrix : an identity matrix (model will be at the origin)
	model = mat4.identity()

	# The ModelViewProjection : multiplication of above 3 matrices
	mvp = projection * view * model
``` 
<img src="https://user-images.githubusercontent.com/102780764/168103690-800d06ad-875d-41dd-8fc7-5da8473a5967.png" width="400px">
<br>

### Tutorial 4 : A Colored Cube
* Drawing a cube requires data from 8 vertices. To draw it, we divide 1 square face into 2 triangles, which is the smallest fragment in OpenGL.
* The cube has 6 faces. Each face has 2 triangles, i.e., 12 triangles. Each triangle has 3 vertices, so 36 vertices need to be defined.

```	
	vertex_data = [ 
		-1.0,-1.0,-1.0,
		-1.0,-1.0, 1.0,
		-1.0, 1.0, 1.0,
		 1.0, 1.0,-1.0,
		-1.0,-1.0,-1.0,
		-1.0, 1.0,-1.0,
		 1.0,-1.0, 1.0,
		-1.0,-1.0,-1.0,
		 1.0,-1.0,-1.0,
		 1.0, 1.0,-1.0,
		 1.0,-1.0,-1.0,
		-1.0,-1.0,-1.0,
		-1.0,-1.0,-1.0,
		-1.0, 1.0, 1.0,
		-1.0, 1.0,-1.0,
		 1.0,-1.0, 1.0,
		-1.0,-1.0, 1.0,
		-1.0,-1.0,-1.0,
		-1.0, 1.0, 1.0,
		-1.0,-1.0, 1.0,
		 1.0,-1.0, 1.0,
		 1.0, 1.0, 1.0,
		 1.0,-1.0,-1.0,
		 1.0, 1.0,-1.0,
		 1.0,-1.0,-1.0,
		 1.0, 1.0, 1.0,
		 1.0,-1.0, 1.0,
		 1.0, 1.0, 1.0,
		 1.0, 1.0,-1.0,
		-1.0, 1.0,-1.0,
		 1.0, 1.0, 1.0,
		-1.0, 1.0,-1.0,
		-1.0, 1.0, 1.0,
		 1.0, 1.0, 1.0,
		-1.0, 1.0, 1.0,
		 1.0,-1.0, 1.0]
```
<img src="https://user-images.githubusercontent.com/102780764/168105380-8e0b5977-b83e-4dc3-91b4-842e4308c1e5.png" width="400px">
<br>

### Tutorial 5 : A Textured Cube
__Load image:__
```
def load_image(file_name):
    im = pil_open(file_name)
    try:
        width,height,image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)

    except SystemError:
        width,height,image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)

    texture_id =  glGenTextures(1)

    # "Bind" the newly created texture : all future texture functions will modify this texture
    bind_texture(texture_id,'MIN_FILTER')
    glTexImage2D(
           GL_TEXTURE_2D, 0, 3, width, height, 0,
           GL_RGBA, GL_UNSIGNED_BYTE, image
       )
    return texture_id
``` 
***A note here:***  
*In Python 2.0, **im.tobytes** (In Python 3.0) turns to **im.tostring**, another question to be solved is that I cannot load "RGBA" form (Why?)*
<br>

<img src="https://user-images.githubusercontent.com/102780764/168106319-2f1ae267-0a58-49ff-a3c7-3f6ad248c561.png" width="400px">
<br>

### Tutorial 6 : Keyboard and Mouse

### Tutorial 7 : Model loading

### Tutorial 8 : Basic shading

<br>
<br>
<br>

## Combination_AR

<br>
<br>
