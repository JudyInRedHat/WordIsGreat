from lxml import etree
import requests
import random
import tkinter
# !-- 函数--
def n1ext():
    global key
    global li
    if key==0:
        wordsv.set(li[key]["words"])
        meaningsv.set(li[key]["meaning"])
        key+=1
    elif key==10:
        root.destroy()
    else:
        wordsv.set(li[key]["words"])
        meaningsv.set(li[key]["meaning"])
        key+=1
# !--爬取--
words = []
meaning = []
choice = random.choice([(11, 226), (12, 105), (122, 35), (123, 25)])
url = "http://word.iciba.com/?action=words&class=" + str(choice[0]) + "&course=" + str(
    random.randint(1, choice[1]))
r = requests.get(url)
r.encoding = r.apparent_encoding
if r.status_code == 200:
    text = r.text
    doc = etree.HTML(text)
    words = doc.xpath('//*[@class="word_main_list"]/li/div[@class="word_main_list_w"]/span//text()')
    meaning = doc.xpath('//*[@class="word_main_list"]/li/div[@class="word_main_list_s"]/span//text()')
    li = []
    for i in range(len(words)):
        dic = {'words': words[i].replace("\t","").replace("\r","").replace("\n",""), 'meaning': meaning[i].replace("\t","").replace("\r","").replace("\n",""),}
        li.append(dic)
# ！--GUI--
root = tkinter.Tk()
root.configure(bg="black")
root.geometry("500x500")
root.title("Word Is Great")
key = 0
wordsv = tkinter.StringVar()
meaningsv = tkinter.StringVar()
wordl = tkinter.Label(root,textvariable=wordsv,bg='green', fg='white').pack()
meaningl = tkinter.Label(root,textvariable=meaningsv,bg='green', fg='white').pack()
doer = tkinter.Button(root,text="继续",command=n1ext).pack()
n1ext()
root.mainloop()
"""
for word in li:
    input(word["words"]+":"+word["meaning"])
"""
