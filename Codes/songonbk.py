#modules
import os
import sys
from moviepy.editor import*
sys.path.append("/Users/shahoreertalha/Desktop/my modules/mypackage")
import oswork as ow
import converter as cr
import moviepyvid as mv
import stringworker as sw
import jsonwork as jw

#v2
#helpful source
temp_folder="/Users/shahoreertalha/Desktop/temp/"

#program variable 1


#customizable variables
    #important
video_length=14


    #one time change
background_file_extensions="MOV"
        #tittle
tittle_must_1="Music"
tittle_must_2="✅🎸 Follow for 10x daily videos #TheBroMusic #TheBro"
hashtag="#music #song #newmusic #lyrics #spotify #sweatmusic #pop #fyp #foryou #englishsong #romanticsong #romanticmusic #goodmusic #happymusic"
tittle_limit=149
vid_index=1

    #path
saved_vid_folder_path_="/Users/shahoreertalha/Desktop/All Work/TheBro Music/Videos/New"+"/"
background_folder_path_="/Users/shahoreertalha/Desktop/All Work/TheBro Music/Video Needs/Backgrounds"
audio_folder_path_="/Users/shahoreertalha/Desktop/All Work/TheBro Music/Video Needs/Music"

#def
    #starter
def ready():
    global audios_path_,hashtag
    audios_path_=ow.load_folder(audio_folder_path_)
    hashtag=hashtag.split(" ")

    #function
def loopmusic():
    for i in audios_path_:
        #load background and audio
        audiopath=audio_folder_path_+"/"+i
        backgroundpath=background_folder_path_+"/"+i.split(".")[0]+"."+background_file_extensions
        audio=AudioFileClip(audiopath).subclip(0,video_length)
        background=VideoFileClip(backgroundpath).subclip(0,video_length)

        #write video
        video=background
        video.audio=audio
        mv.write_vid(video,tittle())
            #return
def tittle(): 
    global vid_index
    tittle_must_have=tittle_must_1+" "+str(vid_index)+" "+tittle_must_2
    vid_index+=1
    return saved_vid_folder_path_+sw.make_variance(tittle_must_have,hashtag,tittle_limit)+"."+background_file_extensions

#program varaibles 2
    #folder / lists holder
audios_path_=[]

#starter
ready()
loopmusic()


#test

# vd_link="/Users/shahoreertalha/Desktop/All Work/TheBro Music/Video Needs/Backgrounds/1.MOV"
# vd=VideoFileClip(vd_link)
# mv.write_vid(vd,temp_folder+"a.MOV")