## Making Movie with Music  * .mp3



def mzic(raw_audio,video,audio_length,Merged_video_root):
    
    
    from moviepy.editor import AudioFileClip,VideoFileClip
    import os
    import numpy as np
    from datetime import datetime
    cwd = os.path.dirname(os.path.realpath(__file__))
   

    musci_root = os.path.join(cwd,'musicroot')
    os.mkdir(musci_root)
    try:


        f=open(raw_audio,'r')
        del f
    
        audioclip=AudioFileClip(raw_audio)   
        
        
        video1=VideoFileClip(video)
        wav_duration=audioclip.duration
        
        start_wav=0
        end_wav=wav_duration
        
        pc=audioclip.subclip(start_wav,-end_wav+int(audio_length))  ## wav audio duration 3 seconds 
        # cwd = os.getcwd()
        cwd = os.path.dirname(os.path.realpath(__file__))
    

        croped_audio_dir = os.path.join(cwd,'croped_audio')
    
        croped_audio_videoname='nm'
        video_outputname=croped_audio_dir +"/"+croped_audio_videoname+'.mp3'
    
        croped_audio_file = os.path.join(croped_audio_dir , video_outputname)
        pc.write_audiofile(croped_audio_file)   
        del pc 
        audioclip=AudioFileClip(croped_audio_file)
        del_var1=[AudioFileClip,croped_audio_file]
        del del_var1
        ## VIDEO AUDIO MERGE 
        # cwd = os.getcwd()
        Merged_video = os.path.join(cwd,'musicroot')
        # Merged_video=Merged_video_root
        croped_audio_videoname='musicroot'
        mp4adi_dt=datetime.utcnow()
        mp4adi_timstmp=int(round(mp4adi_dt.timestamp()*1000))
        croped_audio_videoname=str(mp4adi_timstmp)
        video_outputname=Merged_video +"/"+croped_audio_videoname+'.mp4'  ## mp4 webm
        Merged_video_file = os.path.join(Merged_video , video_outputname)
        video1.audio=audioclip
        video2=video1
        del AudioFileClip,VideoFileClip
        video2.write_videofile(Merged_video_file)
        import mirage
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mirag_out=mirage.watermark(Merged_video_file,Merged_video_root)
        
        
        os.remove(video)   # remove first level video without music file
        os.remove(croped_audio_file) # remove cropped audio file
        # os.remove(Merged_video)
        os.rmdir(Merged_video)
        return [Merged_video]
        

        
    
    
    except (FileNotFoundError,IOError):
        print('Music File was not in root')
    
    
    

    
















    #################################################################
    ##################################################################
    
    # try:
    #     f=open(raw_audio,'r')
    #     del f
    #     # 
    #     audioclip=AudioFileClip(raw_audio)   
       
    #     video1=VideoFileClip(video)
    #     wav_duration=audioclip.duration
    #     start_wav=0
    #     end_wav=wav_duration
        
    #     pc=audioclip.subclip(start_wav,-end_wav+int(audio_length))  ## wav audio duration 3 seconds 
    #     cwd = os.getcwd()
    #     croped_audio_dir = os.path.join(cwd,'croped_audio')
    #     croped_audio_videoname='nm'
    #     video_outputname=croped_audio_dir +"/"+croped_audio_videoname+'.mp3'
    #     croped_audio_file = os.path.join(croped_audio_dir , video_outputname)
    #     pc.write_audiofile(croped_audio_file)   
    #     del pc 
    #     audioclip=AudioFileClip(croped_audio_file)
    #     del_var1=[AudioFileClip,croped_audio_file]
    #     del del_var1
    #     ## VIDEO AUDIO MERGE 
    #     cwd = os.getcwd()
    #     Merged_video = os.path.join(cwd,'Merged_video_out')
    #     Merged_video=Merged_video_root
    #     croped_audio_videoname='output'
    #     mp4adi_dt=datetime.utcnow()
    #     mp4adi_timstmp=int(round(mp4adi_dt.timestamp()*1000))
    #     croped_audio_videoname=str(mp4adi_timstmp)
    #     video_outputname=Merged_video +"/"+croped_audio_videoname+'.webm'  ## mp4 webm
    #     Merged_video_file = os.path.join(Merged_video , video_outputname)
    #     video1.audio=audioclip
    #     video2=video1
    #     del AudioFileClip,VideoFileClip
    #     video2.write_videofile(Merged_video_file)
        
        
    #     os.remove(video)   # remove first level video without music file
    #     os.remove(croped_audio_file) # remove cropped audio file
    #     return [video_outputname]
      

      
    
    
    # except (FileNotFoundError,IOError):
    #     print('Music File was not in root')
    
    
    

    
