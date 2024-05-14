from pydub import AudioSegment
import magic
import os

main_folder = os.listdir()

def rewrite_as_mp3(input, output):
    AudioSegment.from_file(input).export(output, format="mp3")


for file_name in main_folder:
    if os.path.isdir(file_name) == False:
        file_without_endswitch = (os.path.splitext(file_name)[0]+'.mp3')
        file_format = magic.from_file(file_name, mime=True)
        if file_format == 'audio/x-m4a':
            rewrite_as_mp3(file_name, file_without_endswitch)
            print("----> ",file_name ,"converted to", file_without_endswitch)
