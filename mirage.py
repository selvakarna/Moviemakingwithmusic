import moviepy.editor as mp
import os
from datetime import datetime
def watermark(vidopath,output_dir):
#     cwd = os.getcwd()
    # vidopath = os.path.join(cwd,'result','output.mp4')
    video = mp.VideoFileClip(vidopath)
#     cwd = os.getcwd()
    dir_path = os.path.dirname(os.path.realpath(__file__))
   
    input_dir = os.path.join(dir_path,'nlog')
    data_path = os.path.join(input_dir, 'nlog.png')
    
    files=str(data_path)

    logo = (mp.ImageClip(files)

            .set_duration(video.duration)
            .resize(height=117) # if you need to resize...15
            .margin(right=14, bottom=14, opacity=0) 
            .set_pos(("right","bottom")))


    final = mp.CompositeVideoClip([video, logo])
    

    dt=datetime.utcnow()
    video_timstmp=int(round(dt.timestamp()*1000))
    out_videoname=str(video_timstmp)
    video_outputname=output_dir+"/"+out_videoname+'.webm'
    video_out = os.path.join(output_dir, video_outputname)

 
    

    final.write_videofile(video_out)
    os.remove(vidopath) 
    return [video_out]
