import face_recognition as fr
import os
np = fr.api.np

# curdir='/Users/abhishek/myApps/FaceID'
# curdir=os.getcwd()
print("Starting Abhi's FaceID System for Zeronn...Please Wait..")
curdir='/Users/abhishek/myApps/FaceID'
faces_path=curdir+'/faces'
dbpath = 'facebase.npy'
database=np.load(curdir+dbpath).item()
id_2_name = database['id_2_name']
name_2_id = database['name_2_id']
name_2_enc = database['name_2_enc']
#print(name_2_enc.keys(),name_2_id.keys(),id_2_name.keys())

def unlock(name,per):
    print(f'FaceID detected you as {name.upper()} with {(1-per[0])*100}% confidence :')
    os.system(f'Say Welcome Sir')
    exit()

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
    imageface_enc = fr.face_encodings(face)[0].reshape(1,-1)
    for name_face in name_2_enc:
        #print(f"checking for {name_face}")
        face_enc = name_2_enc[name_face][0].reshape(1,-1)
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

if __name__=='__main__':
    check_face()
