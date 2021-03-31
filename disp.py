import csv
import tkinter.filedialog as fd

def openFile():
	fpath = fd.askopenfilename()
	if fpath:
		with open (fpath , 'r') as f:
			reader = csv.reader(f)
			for line in reader :
				print(line)
	return line
