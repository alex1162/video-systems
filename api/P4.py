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
        "ffmpeg", "-i", input_file_path,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-f", "hls",
        "-hls_time", "10",  # Segment length
        output_file_path + ".m3u8"
    ]

    if docker:
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
        "-c:v", "libvpx-vp9",
        "-c:a", "aac",  # AAC Codec
        "-f", "dash",
        output_file_path + ".mpd"
    ]

    if docker:  # If Docker is used, prepend the Docker execution command
        command = docker + command

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Video converted and saved as {output_file_path}")
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert video: {e}")
