import sys, getopt, os
import cv2
import glob
import numpy as np

def frame_extract(input_folder, output_folder):
'''
This function expects a directory with numerically sequenced real and fake PNGs to generate
a combined video of the real alongside the fake
'''

	size = None
	#print(input_folder)
	fake_filenames = []
	real_filenames = []
	for filename in glob.glob(input_folder+'/*.png'):
		if "real" in filename:
			real_filenames.append(filename)
		else:
			fake_filenames.append(filename)
		
	real_filenames.sort()
	fake_filenames.sort()
	first_frame = cv2.imread(real_filenames[0])
	height, width, _ = first_frame.shape
	size = (width * 2, height)
	video = cv2.VideoWriter(output_folder + '/output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 29.97, size)

	for index, file in enumerate(fake_filenames):
		fake_img = cv2.imread(file)
		real_img = cv2.imread(real_filenames[index])
		combined_img = np.concatenate((real_img, fake_img), axis=1)
		video.write(combined_img)
	video.release()

def main(argv):
	# Main handles the file naming of the input/output stream
	input_file = ''
	output_folder = ''
	name = ''
	usage_string = 'make_vid.py -i <input_folder> -o <output_folder>'
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print(usage_string)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(usage_string)
			sys.exit()
		elif opt in ("-i", "--ifile"):
			input_file = arg
		elif opt in ("-o", "--ofile"):
			output_folder = arg
	if ( input_file == '' ):
		print(usage_string)
		sys.exit(2)
	if (output_folder == ''):
		output_folder = os.getcwd()
	frame_extract( input_file, output_folder )

if __name__ == '__main__':
	main(sys.argv[1:])
