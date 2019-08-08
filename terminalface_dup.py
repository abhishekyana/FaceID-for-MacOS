import numpy as np
import os #To control all the OS features
import time # TO have sleep delay and time control
os.system('clear')
print("\t\t\t     Welcome To The WorkStation!\n\n\t\t\t    <<<  Enter The Password  >>> \n")
print("\n"*1+"-"*80+"\n"*1)
os.system('tput setaf 140')
os.system('tput bold')
print("""    A)aa    B)bbbb    H)    hh  I)iiii   S)ssss   H)    hh  E)eeeeee  K)   kk
   A)  aa   B)   bb   H)    hh    I)    S)    ss  H)    hh  E)        K)  kk
  A)    aa  B)bbbb    H)hhhhhh    I)     S)ss     H)hhhhhh  E)eeeee   K)kkk
  A)aaaaaa  B)   bb   H)    hh    I)         S)   H)    hh  E)        K)  kk
  A)    aa  B)    bb  H)    hh    I)    S)    ss  H)    hh  E)        K)   kk
  A)    aa  B)bbbbb   H)    hh  I)iiii   S)ssss   H)    hh  E)eeeeee  K)    kk""")
os.system('tput sgr0')
print("\n"*2+"-"*80+"\n"*2)
print("Starting Abhi's FaceID System for Zeronn...Please Wait..")


import face_recognition as fr
np = fr.api.np
curdir='/Users/abhishek/myApps/FaceID'
faces_path=curdir+'/faces'
dbpath = '/DB/facebase.npy'
database=np.load(curdir+dbpath).item()
id_2_name = database['id_2_name']
name_2_id = database['name_2_id']
name_2_enc = database['name_2_enc']
#print(name_2_enc.keys(),name_2_id.keys(),id_2_name.keys())

def unlock(name,per):
    print(f'FaceID detected you as {name.upper()} with {(1-per[0])*100}% confidence :')
    os.system(f'Say -v daniel Welcome Sir')
    os.system('clear')
    print('<<<<<<<< Welcome Your Workstation Sir >>>>>>>>')
    print('List of all your files are: ')
    os.system('ls -l /abhi/documents/programming/abhi')
    exit()

def lock():
    os.system('say -v daniel "Sorry Wrong Face, All the files are encrypted. Zeronn is Locked "')
    os.system('pmset displaysleepnow')
    time.sleep(5)
    os.system('say "This Mac is Locked Abhishek"')
    #os.system('killall Terminal')

def get_image(n,N):
    name='temptester'
    image_path = f'{faces_path}/{name}.jpg'
    log = os.system(f'imagesnap -w 1 {image_path} > /dev/null')
    image=fr.load_image_file(image_path)
    faces=fr.face_locations(image)
    if not len(faces)==1:
        if len(faces)==0: print(f"{n} time No face found in frame: "); return False
        if len(faces) > 1: print(f"{n} More than one person found in the frame: "); return False
        if n==N:
            exit()
    l=faces[0]
    face = image[l[0]:l[2],l[3]:l[1]]
    imageface_enc = np.array(fr.face_encodings(face)).reshape(-1,128)
    for name_face in name_2_enc:
        #print(f"checking for {name_face}")
        face_enc = name_2_enc[name_face][0].reshape(-1,128)
        #print(type(face_enc),type(imageface_enc))
        conf = fr.face_distance(imageface_enc,face_enc)
        result = np.array(conf)<=0.4
        if np.array(result).sum()>0:
            unlock(name_face,conf)
            return True
    return False

def check_face(N=3):
    name='temptester'
    image_path = f'{faces_path}/{name}.jpg'
    for i in range(1,N+1):
        o = get_image(i,N)
    if o is False:
        print("Didnt recognize the face Sorry . Zeronn is Locked :")
        lock()

if __name__=='__main__':
    check_face()
