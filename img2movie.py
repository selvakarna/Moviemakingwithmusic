

def moviemk(input_dir,output_dir,past_seconds,futur_out_seconds,inp_img_timestamp):
    
    # import numpy as np
    from numpy import shape,where,array
    from os import path,system
    import glob
    from datetime import datetime
    from cv2 import imread,VideoWriter,VideoWriter_fourcc
    import os
    dt=datetime.utcnow()
    
    
    data_path = path.join(input_dir, '*jpg')#*jpg
    files = glob.glob(data_path)

    def nearest(lst,K):
        clear=lambda:system('clear')
        return lst[min(range(len(lst)),key=lambda i: abs(lst[i]-K))]
        clear()




   

    mls=[]
    lst=[]
    import timeit
    st1 = timeit.default_timer()
    for f1 in sorted(files):
        fName, ext = os.path.split(f1)
        fName, ext = os.path.splitext(ext)
        lst.append(int(fName))
        mls.append(fName)
    print('file len',len(lst),type(mls))
        

    dt=datetime.utcnow()
    # current_timestamp=int(round(dt.timestamp()*1000))
    # inp_img_timestamp=str(inp_img_timestamp)
    nea=nearest(lst,int(inp_img_timestamp))
    img_root=input_dir+"/"+str(nea)+'.jpg'
    img=imread(img_root)
    imgsz=shape(img)
    videoheight=imgsz[0]
    videowidth=imgsz[1] 
    nea=str(nea)
    past=past_seconds
    futr=futur_out_seconds
    p=where(array(mls)==nea)
    px=array(p)
    pxln=int(px)
    cc=pxln-past*30 
    cc2=pxln+futr*30
    # hol_centr=len(mls)-pxln
    # print('Hi i am pxln',pxln,'Hole length',len(mls),'Sum of future len',cc2,'sum of Past',cc,"Hole-center",hol_centr)
    sum_of_mls=len(mls)
    
    future_len=cc2
    ### FOR PAST  TIME STMAPE CHANGES--MID EDGE CHECKING
    actl_pst=past*30
    if pxln>=actl_pst:
        cc=cc
        # print('Ok past its equal to or approx center ','actal past',actl_pst,'center',pxln)
    elif pxln!=actl_pst:
        # cc=pxln
        print('Sufficient frames from Past seconds',cc)
        cc=1
    del actl_pst

    ### FOR FUTURE TIME STMAPE CHANGES--MID EDGE CHECKING
    if sum_of_mls>=future_len:
        cc2=cc2
        # print('hi this is hole len & future equal')
    elif sum_of_mls!=future_len:
        les=sum_of_mls-pxln
        cc2=pxln+les-1
        print('Sufficient frames from Future seconds')
    del future_len  
    segfrms=[]
    ### COLLECT PAST FRAMES 
    while cc<=pxln:
        lef=mls[cc]
        # print('Left',cc,lef)
        segfrms.append(lef)
        cc=cc+1
    # del cc,lef
    ### FOR FUTURE TIMESTAMP
    # print('before length',len(segfrms))
    ### COLLECT FUTURE FRAMES 
    gpsxln=pxln
    del pxln
    while gpsxln<cc2:
        rit=mls[gpsxln]
        segfrms.append(rit)
        # print("RIGHT",rit)
        gpsxln=gpsxln+1
    # del cc2,gpsxln,mls
    ############################################
    # segfrms=timstamp_logic(nrst_frm,mls,past_seconds,futur_out_seconds)
    ####################IMG2FRAMES2VIDEO########
    video_timstmp=int(round(dt.timestamp()*1000))
    out_videoname=str(video_timstmp)
    video_outputname=output_dir+"/"+out_videoname+'.mp4'
    video_out = os.path.join(output_dir, video_outputname)
    FPS =30
    wave_len=1
    out = VideoWriter(video_out,VideoWriter_fourcc(*'DIVX'), float(FPS), (videowidth,videoheight))
    for mx in segfrms:  ## alternate for ff new_frames
        video_root=input_dir+"/"+str(mx)+'.jpg' #.jpg
        wave_len=wave_len+1
        # print(segfrms)
       
        RGB=imread(video_root) 
        out.write(RGB)
    out.release()
    # del segfrms,video_root,mx,video_outputname
    # print('wavelength',wave_len)
    # print('Audio Length',wave_len)
    return [video_out,wave_len,nea]





