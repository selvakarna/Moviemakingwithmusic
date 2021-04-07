def filmake(input_dir,output_dir,past_seconds,futur_out_seconds,inp_img_timestamp,wave_root,wave_sequence,Merged_video_root):
    import datetime
    import sys,os
    strt_time = datetime.datetime.now()
    import img2movie
    # import mirage

    import mucvid
  
    import numpy as np
    import datetime
    import histry
    strt_time = datetime.datetime.now()
   
    video_out=img2movie.moviemk(input_dir,output_dir,int(past_seconds),int(futur_out_seconds),int(inp_img_timestamp))
    # mirag_out=mirage.watermark(video_out,output_dir)

    music_duration=video_out[1]/30 ## based on frames length
    nearest_fram=video_out[2]

    wave_sequence=wave_sequence
    
    
    # mp4adi_timstmp=mucvid.mzic(wave_root,mirag_out,int(music_duration),Merged_video_root)  ## wave_sequence
    # print('Mp3 root',wave_root,'dura',music_duration)
    mp4adi_timstmp=mucvid.mzic(wave_root,video_out[0],int(music_duration),Merged_video_root)  ## wave_sequence
 
    
    
    end_time = datetime.datetime.now()
    def sizeof_fun(parms):
        sz=sys.getsizeof(parms)
        gb_sz=sz/1024*3
        return [sz,gb_sz]

    # size_by_gb=parms/int(gb_sz)
    p1=sizeof_fun(mucvid)
    p2=sizeof_fun(video_out)
    current_dir=os.getcwd()
    
    txt_file = os.path.join(current_dir,"movibook.txt")
    file = open(txt_file, "a")
    end_time = datetime.datetime.now()
    rt=end_time-strt_time
    # var=['Start time',strt_time,'End time',end_time,'Running Duration',rt,'img2movie in bytes',p2[0],'img2movie in Gb',p2[1],'movie2muscimerge in bytes',p1[0],'movie2muscimerge in Gb',p1[1]]
    var=['Start time',strt_time,'End time',end_time,'Running Duration',rt,'img2movie in bytes',p2[0],'img2movie in Gb',p2[1]]

    file.write(str(var)+'\n')
    # file.write("World\n")
    file.close()
    del sizeof_fun,var,txt_file,p1,p2
   
    histry.mvhistry(nearest_fram,mp4adi_timstmp,music_duration)
    del histry

