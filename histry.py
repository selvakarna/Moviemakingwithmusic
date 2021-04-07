

def mvhistry(nearest_fram,movie_name,movie_duration):
    import os
    import datetime
    current_dir=os.getcwd()
    print('root is',current_dir)
    txt_file = os.path.join(current_dir,"movielog.txt")
    file2 = open(txt_file, "a")
    

    var=['Nearest_fram',nearest_fram,'Movie_name',movie_name,'Momvie_duration',movie_duration]
    file2.write(str(var)+'\n')
   
    file2.close()
