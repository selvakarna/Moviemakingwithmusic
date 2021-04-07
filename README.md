# Moviemakingwithmusic
Moviemakingwithmusic
                                 Deployment Procedure of Moviemaker Module:
Packages and Installation:
Python3.6.10
OpenCV4.4.0.42
Moviepy
Downloads Links:
Python    : https://www.python.org/downloads/
Moviepy : https://pypi.org/project/moviepy/
Opencv   : https://pypi.org/project/opencv-python/
Installation:
Pip install moviepy
Pip install opencv-python
Terminal Commands for Moviemaker Module run procedure:
Library’s Import procedure:
Import moviemak
Parameters needed to run module:
Moviemak.filmake(input_dir,output_dir,past_seconds,future_out_seconds,Game_server_time_stamp,Music_mp3_root,wave_sequence,Merged_video_root)
Function parameters example:
Input_dir=’/image/frames_root’
Output_dir=’/movie_root’
Past_seconds=’2’  in seconds
Future_out_seconds=’10’ in seconds
Game_server_time_stamp=’20200423444900’
Music_mp3_root=’/mp3 music file root’
Merged_video_root=’/Merged movie root’
Individual Module run terminal commands:
Python3 Moviemak.filmake(input_dir,output_dir,past_seconds,future_out_seconds,Game_server_time_stamp,Music_mp3_root,wave_sequence,Merged_video_root)


Working Concept:
Frames to Movie:
Frames convert into Movie based on Timestamp( Past seconds + Future seconds)
Movie have 30 frames per seconds
 Movie merged with Music:
Music merging with movie based on movie length( duration in seconds)
So Music segment and automatically merged with movie
 Moviemaker Logic:
First checking (finding) Times stamp, from Game Server signal (or) EMO model, on the FFC Root.
The Timestamp (from Game server or EMO) is not there, then to finding the nearest timestamp based on Game server timestamp.
Past seconds: Collect the Past frames from the FFC Root.
Future seconds: Collect the frames based on Future seconds from the FFC root.
Make a movie from collected frames & merged with music.
This module able to make a video with sufficient frames.
Example: past seconds =’3sec’, future seconds= ‘4’
1 second=30 frames
Needed frames=210 frames
In folder frames= 120 frames
Reference & Nearest timestamp on approximately = 100th frame
Past =90 frames
Future=120 frames
But we have sufficient future frames 20 
Video length = ~3.5 seconds





