import random
from tkinter import ttk
from tkinter import *

root = Tk()     # 初始旷的声明
columns = ("a", "b", "c")
treeview = ttk.Treeview(
    root, height=18, show="headings", columns=columns)  # 表格

treeview.column('a', width=50, anchor='center')
treeview.column('b', width=100, anchor='center')
treeview.column('c', width=80, anchor='center')
treeview.heading('a', text='列1')
treeview.heading('b', text='列2')
treeview.heading('c', text='列3')
treeview.pack(side=LEFT, fill=BOTH)
for i in range(10):
    treeview.insert('', i, values=(str(random.randint(0, 9)), str(
        random.randint(0, 9)), str(random.randint(0, 9))))


def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    print(tv.get_children(''))
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
        print(k)
    tv.heading(col, command=lambda: treeview_sort_column(
        tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题


'''
#莫名其妙？？？？写循环的话只有最后一列管用,看论坛说的好像是python2.7管用
for col in columns:
    treeview.heading(col, text=col, command=lambda: treeview_sort_column(treeview, col, False))
'''

'''
#基本用法（上边注释的只有最后一列管用、索性手工试验一下可用性，证实可行）
treeview.heading('a', text='123', command=lambda: treeview_sort_column(tree, 'a', False))#重建标题，添加控件排序方法
treeview.heading('b', text='111', command=lambda: treeview_sort_column(tree, 'b', False))#重建标题，添加控件排序方法
treeview.heading('c', text='223', command=lambda: treeview_sort_column(tree, 'c', False))#重建标题，添加控件排序方法
'''

# 这个代码对于python3就管用了
for col in columns:  # 给所有标题加（循环上边的“手工”）
    treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(
        treeview, _col, False))

root.mainloop()  # 进入消息循环


# from tkinter import *
# from tkinter import ttk
# bookList = [('aaa', 123), ('bbb', 123), ('xxx', 123),
#             ('sss', 123), ('ddd', 123)]
# root = Tk()
# frame = ttk.Frame(root)
# frame.pack(fill='both', expand='false')
# tree = ttk.Treeview(frame, columns=['name', 'price'], show='headings')
# tree.heading('name', text='name')
# tree.heading('price', text='price')
# for item in bookList:
#     tree.insert('', 'end', values=item)
# tree.pack()

# root.mainloop()
