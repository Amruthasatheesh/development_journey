
# 11. Acoustic Song Check
# Create a class AcousticTrack.
# Attributes:
# track_name
# acousticness
# Create a method to check if the track is Acoustic or Non-Acoustic.
class AcousticTrack:
    def __init__(self,trackname,acousticness):
        self.trackname=trackname
        self.acousticness=acousticness
    def chk(self):
        if self.acousticness>= 0.2:
            print("trackname",self.trackname)
            print("Acoustic")
        else:
            print("trackname",self.trackname)
            print("Non-Acoustic")
acou_instance=AcousticTrack("i'm yours",0.2)
acou_instance.chk()

# 12. Instrumental Track
# Create a class InstrumentalTrack.
# Attributes:
# track_name
# instrumentalness
# Create a method to check whether the song contains vocals or only instruments.
class InstrumentalTrack:
    def __init__(self,trackname,instrumentalness):
        self.trackname=trackname
        self.instrumentalness=instrumentalness
    def chk(self):
        if self.instrumentalness > 0.5:
            print("Track:", self.trackname)
            print("Instrumental (No vocals)")
        else:
            print("Track:", self.trackname)
            print("Contains Vocals")


# Example usage
track1 = InstrumentalTrack("Track A", 0.8)
track1.chk()

track2 = InstrumentalTrack("Track B", 0.3)
track2.chk()

13 #  Valence Mood Detector
# Create a class MoodDetector.
# Attributes:
# track_name
# valence
# Create a method to determine if the song mood is:
# Happy
# Neutral
# Sad.
class MoodDetector:
    def __init__(self,trackname,valence):
        self.trackname=trackname
        self.valence=valence
    def song_mood(self):
        if self.valence <= 0.2:
            print("track",self.trackname)
            print("happy")
        elif 0.3 >=self.valence <=0.5:
            print("track",self.trackname)
            print("neutral")
        elif self.valence > 0.6:
            print("track",self.trackname)
            print("sad")
mood_instance=MoodDetector("lucky",0.2)
mood_instance.song_mood()
mood_instance=MoodDetector("mic drop",0.7)
mood_instance.song_mood()


# 14. Track Summary Class
# Create a class TrackSummary.
# Attributes:
# track_name
# artist
# genre
# popularity
# Create a method summary() to print all information.
class TrackSummary:
    def __init__(self,trackname,artist,genre,popularity):
        self.trackname=trackname
        self.artist=artist
        self.genre=genre
        self.popularity=popularity
    def summary(self):
        print("trackname",self.trackname)
        print("artist",self.artist)
        print("genre",self.genre)
        print("popularity",self.popularity)
track_instance=TrackSummary("fire","jungkook","kpop",76)
track_instance.summary()


# 15. Playlist Class
# Create a class Playlist.
# Store multiple Track objects in a list.
# Create methods to:
# Add tracks
# Display all tracks
# Count total tracks.

