#!/usr/bin/env python3

# Define all single operations within a mastrix

class Matrix(object):

	def __init__(self, row, columns):
		self.rows = rows
		self.columns = columns
		self.m = []

	def create_