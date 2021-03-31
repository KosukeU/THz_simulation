import tkinter.filedialog as fd
import numpy as np


def openFile():
	fpath = fd.askopenfilename()
	if fpath:
			with open (fpath, 'r') as f:
				#lst = list(csv.reader(f))
				data01,data02 = np.loadtxt(f,unpack = True)
	return(data01, data02)
