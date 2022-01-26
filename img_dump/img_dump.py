import sys
import requests
import shutil
import threading
import os

threads = []
def download(cin):
    global full_u,ext
    ext = sys.argv[3]
    full_u = str(sys.argv[1])
    if (full_u[len(full_u)-1] != "/"):
        full_u=str(full_u)+"/"
    image_url = full_u+str(cin)+"."+str(ext)
    filename = str(sys.argv[4]) + "/" + image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw,f)
        print('[+][Image sucessfully Downloaded] : ',filename)
 
    else:
        print('[-][Download Fail] '+str(cin)+' '+str(r.status_code))

Lines=[]
def start():
    for i in range(len(Lines)):
        t=threading.Thread(target=download(Lines[i]))
        t.daemon = True 
        threads.append(t)

    for i in range(len(Lines)):
        threads[i].start()

    for i in range(len(Lines)):
        threads[i].join()
    
    print('[DONE] All Images dumped')


if (str(sys.argv[1]) == "help" or str(sys.argv[1]) == "-h"):
    print("[Syntaxe]  : img_dump.py [    URL     ] [LIST.txt] [TYPE/JPG] [PATH/img]")
    print("[Exemple]  : img_dump.py http//w.tet.tn list.txt jpg imglist")
else:
    if (len(sys.argv)<5):
         print("invalide arguments ! ")
    else:
        if (str(sys.argv[1]) == "" or str(sys.argv[2]) == "" or str(sys.argv[3]) == "" or str(sys.argv[4]) == ""):
            print("invalide arguments ! ")
        else:
            # img_dump.py http://ww.com list.txt jpg images
            print('[URL]['+str(sys.argv[1])+"]")
            print('[LIST]['+str(sys.argv[2])+"]")
            print('[TYPE]['+str(sys.argv[3])+"]")
            print('[PATH]['+str(sys.argv[4])+"]")
            list = str(sys.argv[2])
            f= open(list,'r')
            pp=f.readlines()
            f.close()
            Lines = [x[:-1] for x in pp]
            start()


    
    
