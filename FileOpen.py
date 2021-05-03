import tkinter.filedialog as fd
import numpy as np


def openFile():
	fpath = fd.askopenfilename()
	if fpath:
			with open (fpath, 'r') as f:
				#lst = list(csv.reader(f))
				data01,data02 = np.loadtxt(f,unpack = True)
	return(data01, data02)


def FileOpen(event):
	data_store = openFile()
	data_axis = data_store[0]
	data_value = data_store[1]
	dt.set_data(data_axis,data_value)
