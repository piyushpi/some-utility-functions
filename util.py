import cv2

def add_image_details_latest(image_array, custom="hello"):
	"""
	Overlays details
	Returns image data
	"""

	font = cv2.FONT_HERSHEY_SIMPLEX

	H, W, n = image_array.shape
	print(image_array.shape)

	# org = (W-100, H-16)
	org = (16,32)

	# print(H,W,n)


	fontScale = 1
	
	# Blue color in BGR
	color = (255, 255, 255)
	cblack = (0, 0, 0)

	thickness = 2
	watermark_text = 'custom'

	image_array = cv2.putText(image_array, watermark_text, org, font, 
				   fontScale, color, thickness, cv2.LINE_AA)

	top_right_text = "custom %s custom" % (custom)

	pt1 = W - 500
	print(pt1)

	H, W, c = image_array.shape

	print(image_array.shape)

	image_array = cv2.rectangle(image_array, (640, 0), (W, 32), (255, 255, 255), -1)

	cv2.imshow('watermarked', image_array)
	cv2.waitKey(0)

	return image_array

image = cv2.imread('pic.jpg')

image = add_image_details_latest(image)

