import moviemak
from datetime import datetime
import timeit
import os,random
st1 = timeit.default_timer()
output_dir=r'/home/dev/moviesk/testing/output'
# input_dir=r'I:\work_from_home_Kryptos\Update_09_06\To_GIt_Test_upload\img2muzideo\update_05_06_2020\JSON_work\update_12_06_2020\bmp_utci
input_dir=r'/home/dev/integrated_module/front-face-camera/rest_project/media/images/team/user'
#input_dir=r'/home/dev/integrated_module/front-face-camera/rest_project/media/images/ddd/ssss'
# input_dir=r'I:\work_from_home_Kryptos\wfm\jpg'
# input_dir=r'I:\work_from_home_Kryptos\wfm\jpeg' ## jpeg root
past_seconds='2'
#17 sec -video lenth 6sec
futur_out_seconds='4'
dt=datetime.utcnow()
current_timestamp=int(round(dt.timestamp()*1000))
inp_img_timestamp=str(current_timestamp)
# print('Current inp_img_timestamp',inp_img_timestamp)
inp_img_timestamp='20200923110901939' # from datas {1315 frames folder}

#########inp_img_timestamp= "20200709113923298"
wave_sequence='2'
Merged_video_root=output_dir
wave_root=r'/home/dev/moviesk/testing/Ana.mp3'

moviemak.filmake(input_dir,output_dir,past_seconds,futur_out_seconds,inp_img_timestamp,wave_root,wave_sequence,Merged_video_root)
st2 = timeit.default_timer()
print("RUN TIME : {0}".format(st2-st1))
