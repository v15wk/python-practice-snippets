def stringToInt(string):
	return sum([(ord(char)-ord('0')) * (10 ** index) for index, char in enumerate(reversed(string))])


if __name__ == '__main__':
	print stringToInt('12345')
