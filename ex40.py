# ex40

# class ClassName(object):
#     def __init__(self, aaa, bbb):
#     	self.aaa = bbb
#     	self.aaa = bbb

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
	               "I don't want to get sued",
	               "So I will stop right there"])
# print(happy_bday)
# print(happy_bday.lyrics)  # => self.lyrics
happy_bday.sing_me_a_song()

bulls_on_parad = Song(["They rally on there family",
	                   "With pockets full of shells"])
bulls_on_parad.sing_me_a_song()



