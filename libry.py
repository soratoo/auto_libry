import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)


from selenium import webdriver
import chromedriver_binary
import time 
import random
import os
import datetime
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
#----------------------------------------------------------------------------------
import tkinter as tk

# メインウィンドウを作成
baseGround = tk.Tk()
# ウィンドウのサイズを設定
baseGround.geometry('600x360')
# 画面タイトル
baseGround.title('ログイン情報を入力してください')

# ラベル
label1 = tk.Label(text='Libryユーザー名（josog----------）')
label1.place(x=30, y=40)

label2 = tk.Label(text='パスワード')
label2.place(x=30, y=90)

# テキストボックス
textBox1 = tk.Entry(width=40)
textBox1.place(x=30, y=60)

textBox2 = tk.Entry()
textBox2.place(x=30, y=120)

def val():
    # テキストボックスの値を取得
    print(textBox1.get())
    print(textBox2.get())
    global USER
    global PATH
    USER = textBox1.get()
    PATH = textBox2.get()
    baseGround.destroy()
# ボタンの作成と配置
button = tk.Button(baseGround,
                text = '完了!!',
                # クリック時にval()関数を呼ぶ
                command = val
                ).place(x=30, y=180)

baseGround.mainloop()
#----------------------------------------------------------------------------------
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(3)
browser.set_window_size(800,600)
browser.set_window_position(5,5)

URL = "https://app.libry.jp/auth/login/"
browser.get(URL)
for i in range(5):
    while True:
        try:
            net = browser.find_element("xpath", '/html/body/div[2]/div[3]/div/button')
            net.click()
        except:
            time.sleep(0.5)
        else:
            print("finish")
            break

while True:
    try:
        user_id = browser.find_element("xpath", '/html/body/div[2]/div[2]/form/div[4]/label[1]/input')
        user_id.clear()
        user_id.send_keys(str(USER))
    except:
        time.sleep(0.5)
    else:
        print("finish")
        break

while True:
    try:
        word = browser.find_element("xpath", '/html/body/div[2]/div[2]/form/div[4]/label[2]/input')
        word.clear()
        word.send_keys(str(PATH))
    except:
        time.sleep(0.5)
    else:
        print("finish")
        break

while True:
    try:
        login = browser.find_element("xpath", '/html/body/div[2]/div[2]/form/button[1]')
        login.click()
    except:
        time.sleep(0.5)
    else:
        print("finish")
        break

while True:#課題を開く
    try:
        button = browser.find_element("xpath", '/html/body/div[2]/div/div[6]/ul/li[5]/a')
        button.click()
    except:
        time.sleep(0.5)
    else:
        print("finish")
        break

"""
while True:
    try:
        button = browser.find_element("xpath", '/html/body/div[2]/div/div[3]/div[2]/ul/li[2]/label')
        button.click()
    except:
        time.sleep(0.5)
    else:
        print("finish")
        break
"""
#please choose your file
"""
from tkinter import messagebox
messagebox.showinfo('最後のステップです', '自動入力したい課題を選択して下さい')
"""

from tkinter import messagebox
import tkinter as tk
#rootウィンドウを表示されないようにする
ossan = tk.Tk()
ossan.withdraw()
messagebox.showinfo('最後のステップです', '自動入力したい課題を選択して下さい')
#-----------------------------------------------------------------------------------------
while True:
    """
    try:
        button = browser.find_element("xpath", '/html/body/div[2]/div/div[4]/ul[1]/li[2]/a/div[4]')
        button.click()
    except:
        pass
    """
    try:
        button = browser.find_element("xpath", '/html/body/div[2]/div/div[3]/div/ul/li[2]/a/div[4]')
        button.click()
    except:
        pass
#問題を解く
    try:
        button = browser.find_element("xpath", '/html/body/div[2]/div[5]/div[3]/div[2]/a')
        button.click()
    except:
        pass
#結果の入力
    try:
        button = browser.find_element("xpath", '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/a')
        button.click()
    except:
        #全問正解
        try:
            button = browser.find_element("xpath", '/html/body/div[4]/button[1]')
            button.click()
        except:
            pass
        #決定
        try:
            button = browser.find_element("xpath", '/html/body/div[4]/div/button[2]')
            button.click()
        except:
            pass

    try:
        button = browser.find_element("xpath", '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/a[2]')
        button.click()
    except:
        pass

    try:#スタンプ
        button = browser.find_element("xpath", '/html/body/div[4]/div/div/div[1]/div')
        button.click()
    except:
        pass
    else:#スタンプ＿close
        try:
            button = browser.find_element("xpath", '/html/body/div[4]/div/div/div[2]/button')
            button.click()    
        except:
            pass   
#次の課題を解く
    try:
        button = browser.find_element("xpath", '/html/body/div[2]/div[1]/div[3]/div[3]/a[8]')
        button.click()
    except:
        pass

    #time.sleep(0.5)
    #未調整

