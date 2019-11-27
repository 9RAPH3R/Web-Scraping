from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import requests
import bs4
master = Tk()
master.title("Web Scrapper")

def source():
    res = requests.get(e1.get())
    a = res.text
    print(res.text)
    #T.insert(END,a)

def link():
    res = requests.get(e1.get())

    soup = bs4.BeautifulSoup(res.text,'lxml')

    for link in soup.find_all('a',href=True):
        print(link['href'])
        #b = link['href']
        #T.insert(END,b)

def plaintext():
    res = requests.get(e1.get())

    soup = bs4.BeautifulSoup(res.text,'lxml')

    for i in soup.select('p'):
        print(i.text)


Label(master, text="Enter URL").grid(row= 0,column=0)

e1 = Entry(master)

e1.insert(1,"https://")

e1.grid(row=0, column=1)

	
Button(master, text='Enter',
 fg='black',bg='green',).grid(row=0, column=2, sticky=N, pady=4)
Button(master, text='Get Links',
 fg='black',bg='green',command=link).grid(row=1, column=0, sticky=N, pady=4)

Button(master, text='Plain Text',
 fg='black',bg='green',command=plaintext).grid(row=1, column=1, sticky=N, pady=4)


Button(master, text='Source Code',
 fg='black',bg='green',command=source).grid(row=1, column=2, sticky=N, pady=4)


Button(master, text='Quit',
 fg='black',bg='Red',command=master.quit).grid(row=0, column=4, sticky=N, pady=4)

mainloop( )
