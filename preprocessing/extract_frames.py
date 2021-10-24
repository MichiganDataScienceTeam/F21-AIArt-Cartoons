import sys, getopt, os
import cv2

def frame_extract(video_path, output_folder):
	video = cv2.VideoCapture(video_path)
	
	count = 0
	
	success = True
	
	while success:
		
		# read the current frame from the video
		success, image = video.read()
		# save that frame as a jpeg
		if( count % 20 == 0 ):
			cv2.imwrite(f"{output_folder}/frame_{count}.jpg", image)
		
		# increase count
		count += 1
def main(argv):
	# Main handles the file naming of the input/output stream
	input_file = ''
	output_folder = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('extract_frames.py -i <input_file> -o <output_folder>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('extract_frames.py -i <input_file> -o <output_folder>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			input_file = arg
		elif opt in ("-o", "--ofile"):
			output_folder = arg
	if ( input_file == '' ):
		print('extract_frames.py -i <input_file> -o <output_folder>')
		sys.exit(2)
	if (output_folder == ''):
		output_folder = os.getcwd()
	frame_extract( input_file, output_folder )

if __name__ == '__main__':
	main(sys.argv[1:])
