import os

def createExportWindow():
    f_type = [('Text', '*.txt'),('csv', '*.csv')]
    ini_dir = r'C:\\Users\UedaKosuke\Documents\UEDA'
    filename = fd.asksaveasfilename(defaultextension='txt', filetypes=f_type, initialdir=ini_dir, title = 'Export As ...')
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
