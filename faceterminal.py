import os,time

# curdir='/Users/abhishek/myApps/FaceID'
# curdir=os.getcwd()

k = os.system("clear && printf '\e[8;24;80t' && printf '\e[3;710;0t'")
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
database=np.load(curdir+dbpath, allow_pickle=True).item()
id_2_name = database['id_2_name']
name_2_id = database['name_2_id']
name_2_enc = database['name_2_enc']



#print(name_2_enc.keys(),name_2_id.keys(),id_2_name.keys())

def unlock(name,per):
    print(f'FaceID detected you as {name.upper()} with {(1-per[0])*100}% confidence :')
    os.system(f'Say "Welcome Sir"')
    os.system('clear')
    print('<<<<<<<< Welcome Your Workstation Sir >>>>>>>>')
    print('List of all your files are: ')
    os.system('ls -l /abhi/documents/programming/abhi')

    dir_path='/Users/abhishek/Desktop/Files/.Private_Folder/'
    dir_path = unhide_folder(dir_path)

    exit()

###### Added Extra
def decrypt(dirpath):
    files = os.listdir(dirpath)
    for file in files:
        if file.endswith('.enc'):
            file = os.path.abspath(file)
            #print(file)
            k = f"openssl aes-256-cbc -d -a -salt -in {file} -out {file[:-4]} -k 'ASIMO' && rm {file}"
            #print(k,'\n')
            k = os.system(k)
            #print("DONE")


def encrypt(dirpath):
    files = os.listdir(dirpath)
    for file in files:
        if file.endswith('.py'):
            file = os.path.abspath(file)
            k = f"openssl aes-256-cbc -a -salt -in {file} -out {file+'.enc'} -k 'ASIMO' && rm {file}"
            k = os.system(k)

def hide_folder(dirpath):
    parts=dirpath.split('/')
    parts[-2]='.'+parts[-2]
    to_path = '/'.join(parts)
    k = os.system(f'mv {dirpath} {to_path}')
    return to_path

def unhide_folder(dirpath):
    parts=dirpath.split('/')
    if parts[-2].startswith('.'): parts[-2]=parts[-2][1:]
    to_path = '/'.join(parts)
    k = f'mv {dirpath} {to_path}'
    k = os.system(k)
    return to_path
######
def lock():
    os.system('say -v daniel "Sorry Wrong Face, All the important files are encrypted. Mac is Locked."')
    dir_path='/Users/abhishek/Desktop/Files/Private_Folder/'
    dir_path = hide_folder(dir_path) #Added Extra
    os.system('pmset displaysleepnow')
    os.system('killall Terminal')

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
