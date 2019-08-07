import face_recognition as fr
import os
np = fr.api.np

# curdir='/Users/abhishek/myApps/FaceID/DB/'
curdir='/Users/abhishek/myApps/FaceID'
faces_path=curdir+'/faces'
dbpath = '/DB/facebase.npy'


if dbpath not in os.listdir(curdir):
    database = {}
    database['id_2_name'] = {}
    database['name_2_id'] = {}
    database['name_2_enc'] = {}
    np.save(curdir+dbpath , database)

database=np.load(curdir+dbpath).item()

id_2_name = database['id_2_name']
name_2_id = database['name_2_id']
name_2_enc = database['name_2_enc']

def image_to_face(image_path):
    image=fr.load_image_file(image_path)
    faces=fr.face_locations(image)
    if not len(faces)==1:
        if len(faces)==0: print("No face found in frame: ")
        if len(faces)>1: print("More than one person found in the frame: ")
        again = input("Try Again ? (y/n) :")
        if again=='y':
            image_path=get_image()
            image_to_face(image_path)
        else:
            exit()
    l=faces[0]
    face = image[l[0]:l[2],l[3]:l[1]]
    face_enc=fr.face_encodings(face)
    name_2_enc[name]=face_enc
    database['id_2_name'] = id_2_name
    database['name_2_id'] = name_2_id
    database['name_2_enc'] = name_2_enc
    np.save(curdir+dbpath,database)
    print(f'User {name} registered successfully!!!')
    exit()

def get_image():
    print("Please Look at the screen for accurate results : Face Scan Starts Now:")
    image_path=f'{faces_path}/{name}.jpg'
    log = os.system(f'imagesnap -w 1 {image_path} > /dev/null')
    return image_path


def register_new_ID(name):
    while(name in name_2_id):
        name = input(f'Name:{name} is already taken, Please enter another name :')
    id_now = len(id_2_name)
    id_2_name[id_now]=name
    name_2_id[name]=id_now
    image_path = get_image()
    image_to_face(image_path)
    pic_to_face(image)

if __name__=='__main__':
    name=input("Enter your name to store : ")
    register_new_ID(name)
