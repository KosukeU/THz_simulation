import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
import FileOpen as fo

mpl.use('tkAgg')


fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.25, bottom=0.35)

#初期値の設定,可変部を分離して定義
j = 0.5
omega0 = 1.9
gamma0 = 0.26
alpha0 = 0.25

j01 = j*10**-19
omegaB1 = omega0*2.0*np.pi*10**12
gamma1 = 1/(gamma0*10**-12)
alpha1 = alpha0

J_tmp = [0] * 501
E_tmp = [0] * 501
gaussian_ld = [0] * 501		#zero埋めした配列の準備

def emission(j0, omegaB, gamma, alpha):
	#J_tmp = [0] * 501
	#E_tmp = [0] * 501
	#gaussian_ld = [0] * 501

	for t in range(-100, 400):
			if t == 0:
					E_tmp[t + 101] = np.cos(alpha) * 10**12 *10**2
			elif t>0:
					E_tmp[t + 101] = -gamma*np.exp(-gamma * t * 10**-12 * 10**-2) * np.cos(omegaB * t * 10**-12 * 10**-2 + alpha) - omegaB *np.exp(-gamma * t * 10**-12 * 10**-2) * np.sin(omegaB * t * 10**-12 * 10**-2 + alpha)
			else:
					pass

	a = np.log(2) * 4/(0.28*10**-12)**2

	for t in range(-100, 400):
		gaussian_ld[t + 101] = np.exp(-a * (t * 10**-12 * 10**-2)**2)

	E = np.convolve(E_tmp, gaussian_ld) * j0 
	return E


#グラフの描画
#ax1 = fig.add_subplot(3, 1, 1)
#ax2 = fig.add_subplot(3, 1, 2)
#ax3 = fig.add_subplot(1, 1, 1)

t = np.linspace(-2, 8, 1001)

#ax1.plot(gaussian_ld, color=c1, label=l1)
#ax2.plot(E_tmp, color=c2, label=l2)
Em1 = emission(j01, omegaB1, gamma1, alpha1)

#軸の設定
plt.xlim(-2.0,3.0)
plt.xlabel('Time (ps)')
plt.ylabel('Amplitude (a.u.)')

plt.grid('x=0')

l,= ax.plot(t, Em1, color=c3, label=l3, linestyle='solid', linewidth = 0.5) 
dt, = ax.plot(-3,0, "o", color="k", label='value of data', markersize=1)

#スライダーの設置
ax_j = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor='gold')
ax_omega = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='gold')
ax_gamma = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='gold')
ax_alpha = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='gold')

#スライダーの調整
sli_j = Slider(ax_j, 'Amplitude', 0.05, 0.5, valinit=j, valstep=0.01)
sli_omega = Slider(ax_omega, 'BlochFrequency', 1, 2, valinit=omega0, valstep=0.01)
sli_gamma = Slider(ax_gamma, 'RelaxationTime', 0.01, 0.5, valinit=gamma0, valstep=0.01)
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
	l.set_ydata(Em2)
	fig.canvas.draw_idle()

sli_j.on_changed(update)
sli_omega.on_changed(update)
sli_gamma.on_changed(update)
sli_alpha.on_changed(update)

#エクスポートボタンの設置
exportax = plt.axes([0.05, 0.7, 0.1, 0.04])
buttonex = Button(exportax, 'export', color='gold', hovercolor='0.975')


#インポートボタンの設置
importax = plt.axes([0.05, 0.8, 0.1, 0.04])
buttonim = Button(importax, 'import', color='gold', hovercolor='0.975')

def FileOpen(event):
	data_store = fo.openFile()
	data_axis = data_store[0]
	data_value = data_store[1]
	dt.set_data(data_axis,data_value)
buttonim.on_clicked(FileOpen)
#ファイルのimport

#リセットボタンの設置
resetax = plt.axes([0.05, 0.6,  0.1, 0.04])
button = Button(resetax, 'Reset', color='gold', hovercolor='0.975')

def reset(event):
	sli_j.reset()
	sli_omega.reset()
	sli_gamma.reset()
	sli_alpha.reset()

button.on_clicked(reset)

#plt.title("TeraHerzEmission")
plt.show()
'''
def export(event):
	plt.close()
	exname = input()
	fileoutput.output(exname)


buttonex.on_clicked(export)
'''