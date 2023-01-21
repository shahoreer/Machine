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

#path
_vid_f_path="/Users/shahoreertalha/Desktop/All Work/TheBro Music/Video Needs/Music 2"+"/"
save_folder="/Users/shahoreertalha/Desktop/All Work/TheBro Music/Videos/15 sec"+"/"


length=60
clip_length=15
min_clip_length=13
hashtags="#pop #music #lyrics #song #newsong #englishsong #englishmusic #happysong".split(" ")

def write_tittle(full_fid_path,pt,save_folder):
    full_fid_path=full_fid_path.split("/")[-1].split("#")[0]+" p"+str(pt)+" #TheBroMusic English Song #TheBro English Music"
    return save_folder+sw.make_variance(full_fid_path,hashtags,100)+".mov"

def make_vid(vid_path):
    video=VideoFileClip(vid_path)
    start=0
    i=1
    vid_dr=video.duration
    while(start<vid_dr):
        end=start+clip_length
        if vid_dr-end<min_clip_length: end=vid_dr
        #print("write:"+str(start)+":"+str(end))
        # print(write_tittle(vid_path,i,save_folder))
        # print(start," ",end)
        clip=video.subclip(start,end)
        mv.write_vid(clip,write_tittle(vid_path,i,save_folder))
        start=end
        i+=1
        
def target_videos():
    videos=[_vid_f_path+x for x in ow.load_folder(_vid_f_path)]
    for i in videos:
        make_vid(i)

target_videos()