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

#customizable variable 1
video_length=5
    #tittle
tittle_must_have_1="Meme "
tittle_must_have_2=" ✅🔥 Follow for 8x daily memes #TheBroMeme #TheBro"
hashtags="#meme #memes #memestiktok #memesdaily #meme #jokes #jokess #funny #funnyvideo #funnyshit #funnystory #funnyscene #funnystuff #funnysound #funnystories #funnymeme #funnyjokes #lol #lamo"
tittle_limit=150
    #path
saved_vids_path_="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Videos/New" # folder to save finished vids
saveddata_path="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Machine/data/tbmnum.json"
done_ss_path_="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Video Needs/Screen Shots/Old"
done__background_path_="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Video Needs/Backgrounds/Old"
backgrounds_path_="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Video Needs/Backgrounds/New"
screen_shots_path_="/Users/shahoreertalha/Desktop/All Work/TheBro Meme/Video Needs/Screen Shots/New"

#program variable
vidnum=0


#def
def write_tittle():
    tittle=tittle_must_have_1+str(vidnum)+tittle_must_have_2+" "
    return saved_vids_path_+"/"+sw.make_variance(tittle,hashtags,tittle_limit-len(tittle))+".mp4"

def one_vid_done(ss_path,background_path):
    global vidnum
    vidnum+=1
    old_ss_path=done_ss_path_+"/"+ss_path.split("/")[-1]
    old_background_path=done__background_path_+"/"+background_path.split("/")[-1]
    os.rename(ss_path,old_ss_path)
    os.rename(background_path,old_background_path)


###### make modules ###### make modules ###### make modules ###### make modules ^^^^^^^


def makevid(ss_path,background_path):
    background=VideoFileClip(background_path).set_duration(5)
    ss = (ImageClip(ss_path).set_duration(video_length)
          .resize(width=background.size[0]-40)
          .set_pos(("center","center")))
    finalvid = CompositeVideoClip([background, ss])
    mv.write_vid(finalvid,write_tittle())
    one_vid_done(ss_path,background_path)

def ready():
    global hashtags,vidnum
    hashtags=hashtags.split(" ")
    vidnum=jw.json_read_write(saveddata_path,True,"num")

def program_done():
    new_num_json={ "num": vidnum}
    jw.json_read_write(saveddata_path,False,data=new_num_json)

def start():
    for idx,i in enumerate(sss):
        makevid(i,backgrounds[idx])
    program_done()


#customizable variable 2



#ready 2
sss= [screen_shots_path_+"/"+s for s in ow.load_folder(screen_shots_path_)] 
backgrounds=[backgrounds_path_+"/"+s for s in ow.load_folder(backgrounds_path_)] 


#starter
ready()
start()