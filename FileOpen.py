import tkinter as tk
import tkinter.filedialog as fd
import numpy as np
import os


def openFile():
	fpath = fd.askopenfilename()
	basename = os.path.splitext(os.path.basename(fpath))[0]
	if fpath:
			with open (fpath, 'r') as f:
				#lst = list(csv.reader(f))
				data01,data02 = np.loadtxt(f,unpack = True)
	return(data01, data02, fpath, basename)
