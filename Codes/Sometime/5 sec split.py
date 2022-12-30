#modules
import os
import sys
from moviepy.editor import*
sys.path.append("/Users/shahoreertalha/Desktop/my modules/mypackage")
#import oswork as ow
import converter as cr
import moviepyvid as mv
import stringworker as sw
import jsonwork as jw

#customizable variables
#full_vid_path="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Machine/Others/1.MOV"
full_vid_path=input("full video path:")
ins=input("ins:")
save_path="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Machine/Others/5 sec vids"
json_data_path="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Machine/data/data.json"
#ins="6,24,44,100,120,136,158,213,233,250,309,322,336,350,410,427,448,508,528,540"

    #tittle
# tittle_must_have_1="Meme "
# tittle_must_have_2=" ✅🔥 Follow for 8x daily memes #TheBroMeme #TheBro"
# hashtags="#meme #memes #memestiktok #memesdaily #meme #jokes #jokess #funny #funnyvideo #funnyshit #funnystory #funnyscene #funnystuff #funnysound #funnystories #funnymeme #funnyjokes #lol #lamo"
# tittle_limit=150
gamename=input("Game Name:")

clip_length=5

#program variables
video=VideoFileClip(full_vid_path)
vidnum=int(input("start clip:"))-1

#def
def ready():
    global ins,hashtags

    #convert time: 120(1min 20sec)-> 80
    ins=ins.split(",")
    for idx,x in enumerate(ins):
        ins[idx]=cr.min_100_to_sec(int(x))
    #hashtags=hashtags.split(" ")
    #vidnum=jw.json_read_write(json_data_path,True,"num")

def write_tittle():
    global vidnum
    vidnum+=1
    # tittle=tittle_must_have_1+str(vidnum)+tittle_must_have_2+" "
    # return save_path+"/"+sw.make_variance(tittle,hashtags,tittle_limit-len(tittle))+".mp4"
    return save_path+"/"+gamename+" "+str(vidnum)+".mp4"


def done():
    new_num_json={ "num": vidnum}
    jw.json_read_write(json_data_path,False,data=new_num_json)

def write_vid(vidstart):
    print("start:",vidstart)
    print("end:",vidstart+clip_length)
    mv.write_vid(video.subclip(vidstart,vidstart+clip_length),write_tittle(),fps=24)



def cut_vids():
    i=0
    len_ins=len(ins)
    while i<len_ins:
        start=ins[i]
        end=ins[i+1]

        while start<=end-clip_length:
            write_vid(start)
            start+=clip_length
        i+=2
        print("done: i")

        



#starter
ready()
cut_vids()
#done()