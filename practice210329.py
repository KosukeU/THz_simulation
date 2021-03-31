import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import disp

root = tk.Tk()
root.geometry("400x350")

lst = []	#globalで変数を格納

btn=tk.Button(text="ファイルを開く", command = disp.openFile)
print(lst)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()

