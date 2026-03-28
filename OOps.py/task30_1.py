#1. Create a Track Class
# Create a class Track with attributes:
# track_name
# artist
# popularity
# Create a method display_info() to print track details.

# class Track:
#     def __init__(self,track_name,artist,popularity):
#         self.track_name=track_name
#         self.artist=artist
#         self.popularity=popularity
#     def display(self):
#         print(self.track_name,self.artist,self.popularity)
# track_instance=Track("Lucky","Jason MrazColbie Caillat","74")
# track_instance.display()
# 2#
# # Track Duration
# # Create a class TrackDuration with attributes:
# # track_name
# # duration_ms
# # Create a method to convert duration from milliseconds to minutes.
# class TrackDuration:
#     def __init__(self,track_name,duration_ms):
#         self.track_name=track_name
#         self.duration_ms=duration_ms
#     def display(self):
#         print(self.track_name,self.duration_ms)
# track_instance=TrackDuration("comedy",230666)
# track_instance.display()

# 3. Popularity Check
# Create a class TrackPopularity.
# Add a method check_popularity() that prints:
# High Popularity if popularity > 80
# Medium Popularity if 50–80
# Low Popularity if below 50.

# class TrackPopularity:
#         def __init__(self,popularity):
#             self.popularity=popularity
#         def check_popularity(self):
#              if self.popularity>80:
#                   print("high popularity")
#              elif 50<= self.popularity<=80:
#                   print("mediumpopularity")
#              else:
#                   print("lowpopularity")

# track_instance=TrackPopularity(50)
# track_instance=TrackPopularity(85)
# track_instance=TrackPopularity(45)
# track_instance.check_popularity()
                  
                  
# 4. Genre Class
# Create a class Genre.
# Attributes:
# track_name
# track_genre
# Create a method show_genre() to display genre details.
class Genre:
     def __init__(self,track_name,track_genre):
          self.track_name=track_name
          self.track_genre=track_genre
     def show_genre(self):
          print("track_name",self.track_name)
          print("track_genre",self.track_genre)
genre_instance=Genre("mic drop","pop")
genre_instance.show_genre()
    
#5Energy Level
# Create a class EnergyLevel.
# Attributes:
# track_name
# energy
# Create a method that prints:
# High Energy Song
# Medium Energy Song
# Low Energy Song.
class EnergyLevel:
     def __init__(self,track_name,energy):
          self.track_name=track_name
          self.energy=energy
     def songs(self):
          print("track_name",self.track_name)
          print("energy",self.energy)
energy_instance=EnergyLevel("solo",0.317)
energy_instance.songs()
6# Danceability Class
# Create a class DanceTrack.
# Attributes:
# track_name
# danceability
# Create a method to check if the song is good for dancing (danceability > 0.7).
class DanceTrack:
     def __init__(self,track_name,danceability):
          self.track_name=track_name
          self.danceability=float(danceability)
     def chk_song(self):
          if self.danceability> 0.7:
               print("danceability",self.danceability)
               print("track_name",self.track_name)
          else:
               print("not good dancing")
dance_instance=DanceTrack("The Enemy",0.89)
dance_instance.chk_song()
7
# Tempo Analysis
# Create a class TempoAnalyzer.
# Attributes:
# track_name
# tempo
# Create a method to classify:
# Slow
# Medium
# Fast.
class TempoAnalyzer:
     def __init__(self,track_name,tempo):
          self.track_name=track_name
          self.tempo=tempo
     def classify(self):
          if self.tempo < 80:
               print("slow",self.track_name)
          elif 80<=self.tempo<=120:

               print("medium",self.track_name)
          elif self.tempo>120:

               print("high",self.track_name)

tempo_instance=TempoAnalyzer("i wont give up",70)
tempo_instance=TempoAnalyzer("i love you",100)
tempo_instance=TempoAnalyzer("lucky",140)
tempo_instance.classify()
tempo_instance.classify()
tempo_instance.classify()
#8Explicit Content Check
# Create a class TrackSafety.
# Attributes:
# track_name
# explicit
# Create a method check_content() to display whether the track is Explicit or Clean.
class TrackSafety:
     def __init__(self,trackname,explicit):
          self.trackname=trackname
          self.explicit=explicit
     def chk_content(self):
          print("explicit",self.trackname)
          print("clean",self.trackname)
obj=TrackSafety("false","i wont give up")
obj=TrackSafety("false","hunger")
obj.chk_content()
obj.chk_content()

# 9. Artist Information
# Create a class Artist.
# Attributes:
# artist_name
# track_name
# Create a method to print all details.
class Artist:
     def __init__(self,artistname,trackname):
          self.artistname=artistname
          self.trackname=trackname
     def names(self):
          print("artistname",self.artistname)
          print("trackname",self.trackname)
obj=Artist("charlie puth","september song")
obj.names()
# 10. Loudness Class
# Create a class LoudnessCheck.
# Attributes:
# track_name
# loudness
# Create a method to classify:
# Loud
# Medium
# Soft.

class Loudnesscheck:
     def __init__(self,trackname,loudness):
          self.trackname=trackname
          self.loudness=loudness
     def classify(self):
          if self.loudness > -5:
            print("Track:", self.trackname)
            print("Loud")
          elif -15 <= self.loudness <=-5:
            print("Track:", self.trackname)
            print("Medium")
          else:
            print("Track:", self.trackname)
            print("Soft")
loudness_instance=Loudnesscheck("songA", -5)
loudness_instance.classify()





     
          
          




    