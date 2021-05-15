import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog as fd
import FileOpen as fo
import tkinter as tk
from tkinter import ttk
import os
import datetime

mpl.use('tkAgg')

c1,c2,c3 = "blue","green","red"	#色の用意
l1,l2,l3 = "gaussian","E_tmp","E"	#ラベルの用意
#fig = plt.figure()

fig, ax = plt.subplots(figsize=(6,5))
#plt.subplots_adjust(left=0.25, bottom=0.35)

#初期値の設定,可変部を分離して定義
j = 0.5
omega0 = 1.9
gamma0 = 0.26
alpha0 = 0.25
tm = 0.28

j01 = j*10**-19
omegaB1 = omega0*2.0*np.pi*10**12
gamma1 = 1/(gamma0*10**-12)
alpha1 = alpha0

J_tmp = [0] * 501
E_tmp = [0] * 501
gaussian_ld = [0] * 501		#zero埋めした配列の準備

def emission(j0, omegaB, gamma, alpha):
	for t in range(-100, 400):
			if t == 0:
					E_tmp[t + 101] = np.cos(alpha) * 10**12 *10**2
			elif t>0:
					E_tmp[t + 101] = -gamma*np.exp(-gamma * t * 10**-12 * 10**-2) * np.cos(omegaB * t * 10**-12 * 10**-2 + alpha) - omegaB *np.exp(-gamma * t * 10**-12 * 10**-2) * np.sin(omegaB * t * 10**-12 * 10**-2 + alpha)
			else:
					pass

	a = np.log(2) * 4/(tm*10**-12)**2

	for t in range(-100, 400):
		gaussian_ld[t + 101] = np.exp(-a * (t * 10**-12 * 10**-2)**2)

	E = np.convolve(E_tmp, gaussian_ld) * j0
	return E


#グラフの描画
#ax1 = fig.add_subplot(3, 1, 1)
#ax2 = fig.add_subplot(3, 1, 2)
#ax3 = fig.add_subplot(1, 1, 1)

t = np.round(np.linspace(-2, 8, 1001),2)

#ax1.plot(gaussian_ld, color=c1, label=l1)
#ax2.plot(E_tmp, color=c2, label=l2)
Em1 = emission(j01, omegaB1, gamma1, alpha1)
Em3 = Em1
#軸の設定
plt.xlim(-2.0,3.0)
plt.ylim(-3.0*10**-6,3.0*10**-6)
plt.xlabel('Time (ps)')
plt.ylabel('Amplitude (a.u.)')

plt.grid('x=0')

l,= ax.plot(t, Em1, color=c3, label=l3, linestyle='solid', linewidth = 0.5)
dt, = ax.plot(-3,0,"o", color="k", label='value of data', markersize=1)

'''
#スライダーの設置
ax_j = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor='gold')
ax_omega = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='gold')
ax_gamma = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='gold')
ax_alpha = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='gold')

#スライダーの調整
sli_j = Slider(ax_j, 'Amplitude', 0.05, 0.7, valinit=j, valstep=0.005)
sli_omega = Slider(ax_omega, 'BlochFrequency', 1, 2, valinit=omega0, valstep=0.01)
sli_gamma = Slider(ax_gamma, 'RelaxationTime', 0.01, 0.7, valinit=gamma0, valstep=0.005)
sli_alpha = Slider(ax_alpha, 'InitialPhase', -2, 2, valinit=alpha0, valstep=0.01)

#スライダーの有効化
def update(val):
	sj = sli_j.val
	somega = sli_omega.val
	sgamma = sli_gamma.val
	salpha = sli_alpha.val
	j02 = sj*10**-19
	omegaB2 = somega * 2.0 * np.pi* 10 **12
	gamma2 = 1/(sgamma * 10**-12)
	alpha2 = salpha
	Em2 = emission(j02, omegaB2, gamma2, alpha2)
	global Em3
	Em3 = Em2
	l.set_ydata(Em2)
	fig.canvas.draw_idle()

sli_j.on_changed(update)
sli_omega.on_changed(update)
sli_gamma.on_changed(update)
sli_alpha.on_changed(update)
'''


root = tk.Tk()
root.geometry('700x700')
root.title(u'Terahertz Fitting')


dt_now = datetime.datetime.now()
basename = str(dt_now) + '_test' #ファイルをインポートしていない場合にはtestとして出力
dirname = r'C:\\Users\UedaKosuke\Documents\UEDA'

def createExportWindow():
    f_type = [('Text', '*.txt'),('csv', '*.csv')]
    filename = fd.asksaveasfilename(defaultextension='txt', filetypes=f_type, initialdir=dirname, initialfile = basename, title = 'Export As ...')
    if filename:
        with open(filename, mode='w',encoding='utf-8') as f:
            root, ext = os.path.splitext(filename)
            print(ext)
            for pair in zip(t,Em3):
                print(*pair, file=f)

        if ext == '.txt':
            with open(filename, encoding='utf-8') as f:
                data_lines = f.read()
                datalines=data_lines.replace(' ','\t')

        else:
            with open(filename, encoding='utf-8') as f:
                data_lines = f.read()
                datalines=data_lines.replace(' ',',')
        with open(filename, mode='w', encoding='utf-8') as f:
            print(datalines, file=f)


def WriteFile(event):
    createExportWindow()

#エクスポートボタンの設置
'''
exportax = plt.axes([0.05, 0.7, 0.1, 0.04])
buttonex = Button(exportax, 'export', color='gold', hovercolor='0.975')

buttonex.on_clicked(WriteFile)
'''
btnex = tk.Button(root, text='export', command = createExportWindow, width = 12)
btnex.place(x = 602, y = 150)

def updatewaveform():
	sj = valamp.get()
	somega = valblo.get()
	sgamma = valrel.get()
	salpha = valini.get()
	j02 = sj*10**-19
	omegaB2 = somega * 2.0 * np.pi* 10 **12
	gamma2 = 1/(sgamma * 10**-12)
	alpha2 = salpha
	Em2 = emission(j02, omegaB2, gamma2, alpha2)
	global Em3
	Em3 = Em2
	l.set_ydata(Em2)
	fig.canvas.draw_idle()

#tk_sliderの設置
def updatetest(event):
	updatewaveform()
	'''
	sj = valamp.get()
	somega = valblo.get()
	sgamma = valrel.get()
	salpha = valini.get()
	j02 = sj*10**-19
	omegaB2 = somega * 2.0 * np.pi* 10 **12
	gamma2 = 1/(sgamma * 10**-12)
	alpha2 = salpha
	Em2 = emission(j02, omegaB2, gamma2, alpha2)
	global Em3
	Em3 = Em2
	l.set_ydata(Em2)
	fig.canvas.draw_idle()
	'''
	labelvalamp["text"] = valamp.get()
	labelvalblo["text"] = valblo.get()
	labelvalrel["text"] = valrel.get()
	labelvalini["text"] = valini.get()

valamp = tk.DoubleVar(root,value=0.5)
scamp = tk.Scale(root,
    variable=valamp,
    orient=tk.HORIZONTAL,
    length=400,
    from_= 0.05,
	resolution = 0.005,
    to=0.7,
	showvalue = 0,
	command = updatetest
)
scamp.place(x= 150, y=600)
labelscamp = ttk.Label(
	root,
	text = "Amplitude"
)
labelscamp.place(x=30,y=600)
labelvalamp = ttk.Label(
	root,
	text = valamp.get()
)
labelvalamp.place(x=550,y=600)

valblo = tk.DoubleVar(root,value=1.9)
scblo = tk.Scale(root,
    variable=valblo,
    orient=tk.HORIZONTAL,
    length=400,
    from_= 1.0,
	resolution = 0.01,
    to=2.0,
	showvalue = 0,
	command = updatetest
)
scblo.place(x= 150, y=620)
labelscblo = ttk.Label(
	root,
	text = "BlochFrequency"
)
labelscblo.place(x=30,y=620)
labelvalblo = ttk.Label(
	root,
	text = valblo.get()
)
labelvalblo.place(x=550,y=620)

valrel = tk.DoubleVar(root,value=0.24)
screl = tk.Scale(root,
    variable=valrel,
    orient=tk.HORIZONTAL,
    length=400,
    from_= 0.01,
	resolution = 0.005,
    to=0.7,
	showvalue = 0,
	command = updatetest
)
screl.place(x= 150, y=640)
labelscrel = ttk.Label(
	root,
	text = "RelaxationTime"
)
labelscrel.place(x=30,y=640)
labelvalrel = ttk.Label(
	root,
	text = valrel.get()
)
labelvalrel.place(x=550,y=640)

valini = tk.DoubleVar(root,value=0.25)
scini = tk.Scale(root,
    variable=valini,
    orient=tk.HORIZONTAL,
    length=400,
    from_= -2.0,
	resolution = 0.01,
    to=2.0,
	showvalue = 0,
	command=updatetest
)
scini.place(x= 150, y=660)
labelscini = ttk.Label(
	root,
	text = "InitialPhase"
)
labelscini.place(x=30,y=660)
labelvalini = ttk.Label(
	root,
	text = valini.get()
)
labelvalini.place(x=550,y=660)


#時間分解能の編集
'''
flag1 = 0

def AppChange():
    timres_value = timres.get()
    global tm
    tm = float(timres_value)
    updatewaveform()

def timeres():
    global flag1, timres, tmlabel, appbtn
    if flag1 == 0:
    	timres = tk.Entry(root, width=5)
    	timres.insert(0, tm)
    	timres.place(x=620,y=450)
    	tmlabel = tk.Label(root, text='(ps)')
    	tmlabel.place(x=650, y=450)
    	appbtn = tk.Button(root, text='Apply', command=AppChange)
    	appbtn.place(x=620, y=500)
    	#root.geometry('700x700')
    	flag1 = -1

    else:
        timres.place_forget()
        tmlabel.place_forget()
        appbtn.place_forget()
        #root.geometry('700x700')
        flag1 = 0

btn = tk.Button(self.reswin, text='EditTime'+'\n'+'Resolution', command=timeres, width = 12)
btn.place(x=100, y=100)
'''

class restest():
	def reswindestroy(self):
		timres_value = timres.get()
		global tm
		tm = float(timres_value)
		updatewaveform()
		self.reswin.destroy()

	def reswindow(self):
		global timres
		self.reswin = tk.Tk()
		self.reswin.geometry('150x100')
		self.reswin.title(u'EditTimeResolution')
		self.reswin.grab_set()
		#root.configure(bg='gray')
		timres = tk.Entry(self.reswin, width=5)
		timres.insert(0, tm)
		timres.place(x=30,y=30)
		tmlabel = tk.Label(self.reswin, text='(ps)')
		tmlabel.place(x=80, y=30)
		btnresapp = tk.Button(self.reswin, text='Apply', command = self.reswindestroy, width=10)
		btnresapp.place(x=30, y=60)
		self.reswin.mainloop()

resfunc = restest()
btnres = tk.Button(root, text='EditTime'+'\n'+'Resolution', command=resfunc.reswindow, width = 12)
btnres.place(x=602, y=430)


#軸範囲編集ウィンドウ
class axtest():
	def axprodestroy(self):
		self.axwin.destroy()

	def axisproper(self):
		self.axwin = tk.Tk()
		self.axwin.geometry('250x120')
		self.axwin.title(u'axis property')
		xfromL = tk.Label(self.axwin, text='x axis  from :')
		xfromL.place(x=20, y=20)
		xfromE = tk.Entry(self.axwin, width=5)
		xfromE.place(x=100, y=20)
		xtoL = tk.Label(self.axwin, text='to :')
		xtoL.place(x=158, y=20)
		xtoE = tk.Entry(self.axwin, width=5)
		xtoE.place(x=180, y=20)
		xtoL = tk.Label(self.axwin, text='y axis  from :')
		xtoL.place(x=20, y=60)
		yfromE = tk.Entry(self.axwin, width=5)
		yfromE.place(x=100, y=60)
		ytoL = tk.Label(self.axwin, text='to :')
		ytoL.place(x=158, y=60)
		ytoE = tk.Entry(self.axwin, width=5)
		ytoE.place(x=180, y=60)
		btnclose = tk.Button(self.axwin, text='Apply', command = self.axprodestroy, width = 10)
		btnclose.place(x=70, y=90)
		self.axwin.mainloop()

axfunc = axtest()
btnax = tk.Button(root, text='axis property', command = axfunc.axisproper, width = 12)
btnax.place(x= 602, y = 400)

#インポートボタンの設置

filenamelabel = tk.Label(root, text='No file imported')
filenamelabel.place(x=50, y=550)
def FileOpen():
	data_store = fo.openFile()
	data_axis = data_store[0]
	data_value = data_store[1]
	global filenamelabel
	filenamelabel["text"] = 'plotted data place : ' + data_store[2]
	global dirname
	dirname = os.path.dirname(data_store[2])
	global basename
	basename = data_store[3] + '_fitting'
	dt.set_data(data_axis,data_value)
	fig.canvas.draw_idle()

'''
#matplotlibによるimportボタン(有効にするにはFileOpenの引数をeventに変更)
importax = plt.axes([0.05, 0.8, 0.1, 0.04])
buttonim = Button(importax, 'import', color='gold', hovercolor='0.975')
buttonim.on_clicked(FileOpen)
'''

#Tkによるimportボタン
btnim = tk.Button(root, text='import', command = FileOpen, width = 12)
btnim.place(x = 602, y = 100)

'''
#リセットボタンの設置
resetax = plt.axes([0.05, 0.6,  0.1, 0.04])
button = Button(resetax, 'Reset', color='gold', hovercolor='0.975')

def reset(event):
	sli_j.reset()
	sli_omega.reset()
	sli_gamma.reset()
	sli_alpha.reset()
'''

def _destroyWindow():
    root.quit()
    root.destroy()

root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0)
canvas.draw()
#canvas.get_tk_widget().pack()

root.update()
root.deiconify()
root.mainloop()
