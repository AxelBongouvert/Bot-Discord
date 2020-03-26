""""import discord"""
import random

class MyRunes:
	"""Runes fondamentale
	- petite rune 1
	- petite rune 2
	- petite rune 3"""

	rune1F = 0
	rune1C = 0
	rune2C = 0
	rune3C = 0

	rune2F = 0
	rune21C = 0
	rune22C = 0
	rune23C = 0

	basicRune1 = 0
	basicRune2 = 0
	basicRune3 = 0

	def __init__(self):
		"""Init runes"""
		self.runeF = 0
		self.rune1C = 0
		self.rune2C = 0
		self.rune3C = 0

		self.rune2F = 0
		self.rune21C = 0
		self.rune22C = 0
		self.rune23C = 0

		self.basicRune1 = 0
		self.basicRune2 = 0
		self.basicRune3 = 0

	def _random_RuneF(self):
		"""Random number to choose Fundamental Rune"""
		rnd.randint(1,4)

	def _random_Rune2F(self):
		"""Random number to choose Fundamental Rune"""
		rnd.randint(1,3)

	def _random_Number(self):
		"""Random number to choose basic Rune"""
		"""And basic rune"""
		rnd.randint(1,3)

	def _random_Number_Second_Rune(self):
		"""Random number to choose basic Rune"""
		"""And basic rune"""
		rnd.randint(1,3)

	def _give_Rand_Num(self):
		"""Give a number to our runes"""
		runeF._random_RuneF()
		rune1C._random_Number()
		rune2C._random_Number()
		rune3C._random_Number()

		rune2F._random_Rune2F()
		rune21C._random_Number_Second_Rune()
		rune22C._random_Number_Second_Rune()
		rune23C._random_Number_Second_Rune()

		basicRune1._random_Number()
		basicRune2._random_Number()
		basicRune3._random_Number()
		
	def _display(self):
		print ("Rune Fundamental : - ",rune1F)
		print ("Rune row 1 : - ",rune1C)
		print ("Rune row 2 : - ",rune2C)
		print ("Rune row 3 : - ",rune3C)
		print ("---------------")
		print ("Rune Fundamental : - ",rune2F)
		print ("Second Rune 1 : - ",rune21C)
		print ("Second Rune 2 : - ",rune22C)
		print ("Second Rune 3 : - ",rune23C)
		print ("---------------")
		print ("Basic Rune 1 : - ",basicRune1)
		print ("Basic Rune 1 : - ",basicRune2)
		print ("Basic Rune 1 : - ",basicRune3)
		