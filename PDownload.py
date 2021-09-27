import wget
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

#url = ''

path_file_list = []
urls_list = []

#file_path_name = ''

#wget.download(url, file_path_name)

def refresh_urls():
    urls.configure(state='normal')
    b = 0
    downl_index = 0
    urls.event_generate("<<SelectAll>>")
    urls.event_generate("<<Clear>>")
   # for url in urls_list:
    #    print(url + " [" + str(downl_index) + "]")
     #
    for url in urls_list:
        urls.insert(0.0, url + " " + path_file_list[b] + " " + str(downl_index)+ "\n")
        downl_index += 1
        b += 1
    urls.configure(state='disabled')
def add_url():
    url = entry.get()
    file_name = entry2.get()
    path = entry3.get()
    file_path_name = path + "/" + file_name
    urls_list.append(url)
    path_file_list.append(file_path_name)
    print(urls_list)
    print(path_file_list)
    refresh_urls()
def download_queue():
    a=0
    for url in urls_list:
        print("a")
        wget.download(url, path_file_list[a])
        a += 1
    messagebox.showinfo("showinfo", "Downloaded " + str(a) + "files " + "to " + path_file_list[0])
def delete_url():
    downl_index2 = 0
    downl_index2 = entry4.get()
    urls_list.pop(int(downl_index2))
    path_file_list.pop(int(downl_index2))
    refresh_urls()
    if downl_index2 < 0 or downl_index2 > len(urls_list) - 1:
        return

def clear_queue():
    path_file_list.clear()
    urls_list.clear()
    refresh_urls()

root = tkinter.Tk()
root['background']='grey'
root.title("NDIDownl ver0")
root.geometry('670x400')
root.resizable(False, False)

l = tkinter.Label(root, text='Python downloader', bg='grey')
l.pack()
entry = tkinter.Entry(width=60)
entry.place(x=0,y=30)
m = tkinter.Button(root, text = 'Add to queue', command=add_url, bg='grey')
m.place(x=390,y=63)
l = tkinter.Label(root, text='File URL', bg='grey')
l.place(x=0, y=10)
entry = tkinter.Entry(width=60)
entry.place(x=0,y=30)
l = tkinter.Label(root, text='File name', bg='grey')
l.place(x=390, y=10)
m = tkinter.Button(root, text = 'Delete', command=delete_url, bg='grey')
m.place(x=590,y=30)
l = tkinter.Label(root, text='Number to delete', bg='grey')
l.place(x=550, y=10)
entry4 = tkinter.Entry(width=5)
entry4.place(x=550,y=30)
entry2 = tkinter.Entry(width=23)
entry2.place(x=390,y=30)
l = tkinter.Label(root, text='Path', bg='grey')
l.place(x=0,y=50)
entry3 = tkinter.Entry(width=60)
entry3.place(x=0,y=69)

urls = ScrolledText(root, width=81, height=19, bg='black', fg='white')
urls.place(x=0, y=90)

m = tkinter.Button(root, text = 'Download queue', command=download_queue, bg='grey')
m.place(x=480,y=63)

m = tkinter.Button(root, text = 'Clear queue', command=clear_queue, bg='grey')
m.place(x=590,y=63)

refresh_urls()
root.mainloop()