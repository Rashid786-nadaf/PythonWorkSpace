# Parent class 1
class FitnessTracker:
    def __init__(self, steps):
        self.steps = steps

    def show_fitness(self):
        return f"Steps walked today: {self.steps}"


# Parent class 2
class MusicPlayer:
    def __init__(self, song):
        self.song = song

    def play_music(self):
        return f"Now playing: {self.song}"


# Child class (inherits from both parents)
class SmartWatch(FitnessTracker, MusicPlayer):
    def __init__(self, steps, song, brand):
        # Call constructors of both parent classes
        FitnessTracker.__init__(self, steps)
        MusicPlayer.__init__(self, song)
        self.brand = brand

    def show_details(self):
        return f"SmartWatch Brand: {self.brand}"


# -------- Object Creation --------
watch = SmartWatch(8500, "Imagine - John Lennon", "FitPro")

print(watch.show_details())
print(watch.show_fitness())   # from FitnessTracker
print(watch.play_music())     # from MusicPlayer
