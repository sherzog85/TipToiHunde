import gtts
import xlrd
from pydub import AudioSegment
import os


#sudo apt-get install ffmpeg lame flac vorbis-tools


s_file='dogs.xls'
wb=xlrd.open_workbook(s_file)
sheet=wb.sheet_by_index(0)
s_yaml='dogs.yaml'
s_out='product-id: 950\r\ncomment: Wer kennt alle Hunde für den TipToi\r\nscripts:\r\n'

for i in range(sheet.nrows):
    s_dog=sheet.cell_value(i,0)
    if len(s_dog)>0:
        s_out=s_out+'  '+sheet.cell_value(i,1)+": P("+sheet.cell_value(i,1)+")\r\n"
        s_file=sheet.cell_value(i,1) + '.wav'
        s_lang=sheet.cell_value(i,2)
        tts = gtts.gTTS(s_dog,lang=s_lang)
        tts.save(s_file)
        tts.save('temp.mp3')
        AudioSegment.from_mp3('temp.mp3').export(s_file,format='wav')
        os.system('oggenc ' + s_file)
        os.system('rm ' + s_file)
        print(s_dog)
    
f=open(s_yaml,'w+')
f.write(s_out)
f.close()