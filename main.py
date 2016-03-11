import speech_recognition_engine as engine
from tasks.music_player import MusicPlayer
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

if len(sys.argv) != 2:
  print "Usage %s <music_directory>" % str(sys.argv[0])
  sys.exit()

music_player = MusicPlayer(str(sys.argv[1]))

while True:
  text = engine.get_user_command()
  print text
  music_player.action(text)

