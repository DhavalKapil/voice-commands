from task import Task

import os
from pygame import mixer

class MusicPlayer(Task):

  songs_name_location_hash = {}
  current_playing_song_name = None

  def __init__(self, music_dir):
    self.index_songs(music_dir)
    mixer.init()

  def action(self, user_text):

    words = user_text.split(" ")
    words = map(lambda x : x.lower(), words)

    if "play" in words:
      words.remove("play");
      self.play_song(words)
    elif "stop" in words:
      words.remove("stop")
      self.stop_song(words)

  def play_song(self, words):
    song_name = self.recognize_song(words);
    if song_name == None:
      # Song name not recognized
      return
    self.current_playing_song_name = song_name
    print "Playing " + self.songs_name_location_hash[song_name]
    mixer.music.load(self.songs_name_location_hash[song_name])
    mixer.music.play()

  def stop_song(self, words):
    if "song" in words:
      mixer.music.stop()
      self.current_playing_song_name = None
      return

  def index_songs(self, music_dir):
    for root, dirs, files in os.walk(music_dir):
      for name in files:
        if name.endswith(".mp3"):
          self.songs_name_location_hash[name.lower()] = root + "/" + name

  def recognize_song(self, words):
    max_count = -1
    max_song_name = None
    for song_name, song_location in self.songs_name_location_hash.iteritems():
      count = 0
      for word in words:
        if word in song_name:
          count = count + 1
      if count > max_count:
        max_count = count
        max_song_name = song_name
    if max_count > 0:
      return max_song_name
    else:
      return None