import subprocess   
import numpy as np
from PIL import Image
import cv2
import pywt

def cut_video(input_file_path, output_file_path, docker = None):

    command = ["ffmpeg", "-i", input_file_path, "-t", "00:01:00", "-c", "copy", output_file_path]

    if docker:# If docker is provided, use the docker command
        command = docker + command

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Video cut and saved as {output_file_path}")
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Failed to cut video: {e}")

def MP4_video(input_file_path, output_file_path, docker=None):
    command = [
        "ffmpeg", "-y",
        "-i", input_file_path,
        "-c:v", "libx264",  # H.264 (AVC) codec for video
        "-c:a", "aac",  # AAC codec for audio
        "-preset", "fast",  # Faster encoding
        "-movflags", "+faststart",  # Optimize for streaming
        output_file_path
    ]

    if docker:  # If Docker is used, prepend Docker execution command
        command = docker + command

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Video converted and saved as {output_file_path}")
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert video: {e}")
 
       
def MKV_video(input_file_path, output_file_path, docker=None):
    command = [
        "ffmpeg", "-y",
        "-i", input_file_path,
        "-c:v", "libvpx-vp9",  # VP9 codec for video
        "-c:a", "aac",  # AAC codec for audio
        "-f", "matroska",  # Use MKV container format
        output_file_path
    ]

    if docker:  # If Docker is used, prepend Docker execution command
        command = docker + command

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Video converted and saved as {output_file_path}")
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert video: {e}") 








# class Video:
#     def __init__(self, x, y, z):  
#         self.x = x
#         self.y = y
#         self.z = z

    
    
#     # to change pixels from RGB to YUV
#     def rgb_to_yuv(self, R, G, B):
#         self.x = ((66 * R + 129 * G + 25 * B + 128) / 256) + 16
#         self.y = ((-38 * R - 74 * G + 112 * B + 128) / 256) + 128
#         self.z = ((112 * R - 94 * G - 18 * B + 128) / 256) + 128
#         return Color(self.x, self.y, self.z)
    
#     # to change pixels from RGB to YUV
#     def yuv_to_rgb(self, Y, U, V):
#         self.x = 1.164 * (Y-16) + 1.596 * (V-128)
#         self.y = 1.164 * (Y-16) - 0.391 * (U-128) - 0.813 * (V-128)
#         self.z = 1.164 * (Y-16) + 2.018 * (U-128)
#         return Color(self.x, self.y, self.z)

#     # we have created this method to be used later on when reading images
#     @staticmethod
#     def load_image_as_matrix(img_path):
#         image = Image.open(img_path).convert('L')
#         return np.array(image)

#     # Resizing the image using ffmpeg command
#     @staticmethod
#     def resize_image(input_path, output_path, width=320, height=240, docker=None):
#         # If docker is provided, use the docker command
#         if docker:
#             command = docker + ['ffmpeg', '-i', input_path, '-vf', f'scale={width}:{height}', output_path]
#             try:
#                 result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 print(f"Image resized and saved as {output_path}")
#                 return result.stdout, result.stderr
#             except subprocess.CalledProcessError as e:
#                 print(f"Failed to resize image: {e}")
#         else:
#             # If no docker is provided, run ffmpeg directly
#             command = ['ffmpeg', '-i', input_path, '-vf', f'scale={width}:{height}', output_path]
#             subprocess.run(command)
        


#     # Turning the image to black & white using ffmpeg command
#     @staticmethod
#     def bw_image(input_path, output_path, docker=None):
#         # If docker is provided, use the docker command
#         if docker:
#             command = docker + ['ffmpeg', '-i', input_path, '-vf', 'format=gray', output_path]
#             try:
#                 result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 print(f"Image turned to black & white and saved as {output_path}")
#                 return result.stdout, result.stderr
#             except subprocess.CalledProcessError as e:
#                 print(f"Failed to turn image to black & white: {e}")
#         else:
#             # If no docker is provided, run ffmpeg directly
#             command = ['ffmpeg', '-i', input_path, '-vf', 'format=gray', output_path]
#             subprocess.run(command)
        


#     # method to do rl encoding
#     @staticmethod
#     def rl_encoding(values_seq):
#         encoded_values = []
#         current_byte = values_seq[0]
#         count = 0
#         for byte in values_seq:
#             if byte == current_byte:
#                 count += 1
#             else:
#                 encoded_values.append((current_byte, count))
#                 current_byte = byte
#                 count = 1
#         encoded_values.append((current_byte, count))
#         return encoded_values

#     # we have created another method to decode the rl_encoding
#     @staticmethod
#     def rl_decoding(encoded_seq):
#         decoded_seq = []
#         for value, count in encoded_seq:
#             decoded_seq.extend([value] * count)
#         return np.array(decoded_seq)

#     @staticmethod
#     def serpentine(input):
#         # TEST WITH ARRAY:
#         # input = np.array([[1, 2, 3, 4], 
#         #      [5, 6, 7, 8],
#         #      [9, 10, 11, 12],
#         #      [13, 14, 15, 16]])
#         # 
#         # EXPECTED OUTPUT: 1 2 5 9 6 3 4 7 10 13 14 11 8 12 15 16

#         width, height = input.shape
#         pixels = input.flatten().tolist()

#         # creating matrix with pixel values
#         mat = [pixels[i * width:(i + 1) * width] for i in range(height)]

#         # initializing variables
#         r = 0 # rows
#         c = 0 # columns
#         m = width
#         n = height
#         serpentine_pixels = []
#         direction = True

#         # loop for all pixels
#         for _ in range(m * n):
#             serpentine_pixels.append(mat[r][c]) # add pixel to the list

#             # up-right direction
#             if direction:
#                 # top row but not last col-> change direction and move right
#                 if r == 0 and c != n-1:
#                     direction = False
#                     c += 1 
#                 # last col-> change direction and move down
#                 elif c == n-1:
#                     direction = False
#                     r += 1 
#                 # continue moving up-right
#                 else:
#                     r -= 1 
#                     c += 1 

#             # down-left direction
#             else:
#                 # first col but not las row-> change direction and move down
#                 if c == 0 and r != m-1:
#                     direction = True
#                     r += 1 
#                 # last row-> change direction and move right
#                 elif r == m-1:
#                     direction = True
#                     c += 1 
#                 # continue moving down-left
#                 else:
#                     c -= 1
#                     r += 1 

#         return serpentine_pixels


# class DCT:
#     def __init__(self, img_path, q_matrix_level):
#         self.img_path = img_path
#         self.q_matrix_level = q_matrix_level
#         self.image_mat = Color.load_image_as_matrix(img_path)

#     def select_q_matrix(self, level="Q50"):
#         matrices = {
#             "Q10": np.array([[80,60,50,80,120,200,255,255],
#                     [55,60,70,95,130,255,255,255],
#                     [70,65,80,120,200,255,255,255],
#                     [70,85,110,145,255,255,255,255],
#                     [90,110,185,255,255,255,255,255],
#                     [120,175,255,255,255,255,255,255],
#                     [245,255,255,255,255,255,255,255],
#                     [255,255,255,255,255,255,255,255]]),  

#             "Q50": np.array([[16,11,10,16,24,40,51,61],
#                     [12,12,14,19,26,58,60,55],
#                     [14,13,16,24,40,57,69,56],
#                     [14,17,22,29,51,87,80,62],
#                     [18,22,37,56,68,109,103,77],
#                     [24,35,55,64,81,104,113,92],
#                     [49,64,78,87,103,121,120,101],
#                     [72,92,95,98,112,100,130,99]]),    

#             "Q90": np.array([[3,2,2,3,5,8,10,12],
#                         [2,2,3,4,5,12,12,11],
#                         [3,3,3,5,8,11,14,11],
#                         [3,3,4,6,10,17,16,12],
#                         [4,4,7,11,14,22,21,15],
#                         [5,7,11,13,16,12,23,18],
#                         [10,13,16,17,21,24,24,21],
#                         [14,18,19,20,22,20,20,20]])
#         }
        
#         return matrices.get(level, np.ones((8, 8)))

#     def dct_compression(self):
#         height, width = self.image_mat.shape
#         dct_transformed = np.zeros_like(self.image_mat, dtype=np.float32) 
#         q_matrix = self.select_q_matrix(self.q_matrix_level)
#         N = 8 # because we want 8x8 blocks

#         for i in range(0, height, N):
#             for j in range(0, width, N):
#                 block = self.image_mat[i:i+N, j:j+N]   # centering pixel values around zero
#                 dct_block = cv2.dct(np.float32(block))
#                 quantized_block = np.round(dct_block / q_matrix).astype(int)
#                 dct_transformed[i:i+N, j:j+N] = quantized_block

#         encoded_data = Color.rl_encoding(dct_transformed.flatten())
#         return encoded_data

#     def dct_decompression(self, encoded_data):
#         decoded_data = Color.rl_decoding(encoded_data)
#         height, width = self.image_mat.shape
#         decompressed_image = np.zeros((height, width), dtype=np.uint8)
#         q_matrix = self.select_q_matrix(self.q_matrix_level)
#         N = 8

#         reshaped_data = np.reshape(decoded_data, (height, width))
#         for i in range(0, height, N):
#             for j in range(0, width, N):
#                 quantized_block = reshaped_data[i:i+N, j:j+N]
#                 dequantized_block = quantized_block * q_matrix
#                 idct_block = cv2.idct(dequantized_block) 
#                 decompressed_image[i:i+N, j:j+N] = np.clip(idct_block, 0, 255)

#         return Image.fromarray(decompressed_image)


# class DWT:
#     def __init__(self, img_path):
#         self.img_path = img_path
    
#     def dwt_compression(self, img_path):
#         image = np.array(Image.open(img_path).convert('L')) # obtaining the array of values of the image in bw
#         dwt = pywt.dwt2(image, 'sym4') #coefficients
#         cA, (cH, cV, cD) = dwt
        
#         # combining the coefficients to form a single image for visualization
#         transformed_array = np.vstack((
#             np.hstack((cA, cH)),
#             np.hstack((cV, cD))
#         ))
        
#         return Image.fromarray(np.uint8(np.clip(transformed_array, 0, 255))), dwt
    
#     def dwt_decompression(self, compressed_data):
#         data = pywt.idwt2(compressed_data, 'sym4')
        
#         return Image.fromarray(np.uint8(np.clip(data, 0, 255)))
