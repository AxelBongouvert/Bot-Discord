import discord
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

	def randomRuneF(self):
		"""Random number to choose Fundamental Rune"""
		rnd.randint(1,4)

	def randomRune2F(self):
		"""Random number to choose Fundamental Rune"""
		rnd.randint(1,4)

	def randomNumber(self):
		"""Random number to choose basic Rune"""
		rnd.randint(1,3)

	def giveRandNum(self):
		"""Give a number to our runes"""
		runeF.randomRuneF()
		print ("Rune Fundamental : - ",rune1F)
		rune1C.randomNumber()
		print ("Rune row 1 : - ",rune1C)
		rune2C.randomNumber()
		print ("Rune row 2 : - ",rune2C)
		rune3C.randomNumber()
		print ("Rune row 3 : - ",rune3C)
