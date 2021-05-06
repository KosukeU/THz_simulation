def AppChange():
    timres_value = timres.get()
    global tm
    tm = float(timres_value)
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

'''
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
    	root.geometry('700x700')
    	flag1 = -1

    else:
        timres.place_forget()
        tmlabel.place_forget()
        appbtn.place_forget()
        root.geometry('700x600')
        flag1 = 0
'''
