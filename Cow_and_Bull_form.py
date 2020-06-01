# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 04:43:22 2020

@author: lilliloo
"""
#---------------------------------------------------------#
#
#実装完了
#・入力と入力値の表示
#・ボタンを押すと入力値の反映
#・入力値の表への挿入
#
#未完了
#・cow bull の計算

#-----------------------------------------------------------#
#Library123
import tkinter as tk
import tkinter.ttk as ttk
import Func_cows_bulls as CB

#---------------------------------------#
#Variable
count = 1
correct = CB.make_digit(4)

#----------------------------------------#
# Function
def Cals_cow_bull():
    global count
    global correct
    
    user_input = text.get()
    text.delete(0,tk.END)
    #---------------------#
    #Calc cow and bull
     
    answer = [int(s) for s in user_input]
    cow , bull = CB.get_cows_bulls(correct, answer)
    #---------------------#
    # 結果をラベルに表示
    tree.insert("","end",values=(count,user_input,cow,bull))
    count += 1    
    
    if cow == 4 :
        labelResult['text'] = "You Win :)"
        
#---------------------------------------#
# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("Cows and Bulls Game") # タイトル
win.geometry("500x400") # サイズ


#-------------部品------------------#

#--------input-----------#
#input
label = tk.Label(win, text='Please enter a \n 4-digit integer')
label.pack()
label.place(x = 80,y = 30)

# テキストボックスを作成
text = tk.Entry(win)
text.pack()
text.insert(tk.END, '') # 初期値を指定
text.place(x = 200, y = 40)


# Button
Button = tk.Button(win,text = u'OK')
Button.place(x = 350,y = 35)
Button["command"] = Cals_cow_bull

#Table
tree = ttk.Treeview(win)
tree.place(x = 120, y = 100)
# 列インデックスの作成
tree["columns"] = (1,2,3,4)
# 表スタイルの設定(headingsはツリー形式ではない、通常の表形式)
tree["show"] = "headings"
# 各列の設定(インデックス,オプション(今回は幅を指定))
tree.column(1,width=75)
tree.column(2,width=75)
tree.column(3,width=100)
tree.column(4,width=100)
# 各列のヘッダー設定(インデックス,テキスト)
tree.heading(1,text="Trial")
tree.heading(2,text="Guess")
tree.heading(3,text="Cows")
tree.heading(4,text="Bulls")

#Win
#label = tk.Label(win, text=correct)
#label.pack()
#label.place(x = 100,y = 350)

#Result
labelResult = tk.Label(win, text=u'Correct answer :   ? ? ? ?')
labelResult.place(x = 150,y = 350)
print(correct)
#------------------------#




# ウィンドウを動かす --- (*3) 大事！！
win.mainloop()