# Start ROS Code

print('Loading ROS Code')

# Prepare Debug Enabled Variable For Toggling Debug Mode
def debug_debugstatesetup():
	global debugenabled
	debugenabled = False

debug_debugstatesetup()

# DEBUG: Enable Or Disable Debug Mode
def debugstate(state):
    if state == 'Enable':
        debugenabled = True
        print('Debug Mode Has Been Enabled')
    elif state == 'Disable':
        debugenabled = False
        print('Debug Mode Has Been Disabled')
    else:
        raise RuntimeError('An Error Has Occured: Invalid Debug State Entered (0005)')
		
# DEBUG: Make ROS Code Variables Global
def debug_varglobal():
	if debugenabled == True:
		global ros_output
		global ros_stored
	else:
		raise RuntimeError('An Error Has Occured: Debug Mode Not Enabled (0006)')
		
# DEBUG: Supress All Warnings
def debug_supresswarnings():
	if debugenabled == True:
		import warnings
		warnings.filterwarnings("ignore")
	else:
		raise RuntimeError('An Error Has Occured: Debug Mode Not Enabled (0006)')

# Check If A Number Is A Prime Number
def isprime(number):
	if number == 1:
		return False
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			return False
	return True
	
# Make A Paragraph Space
def paraspace(paragraphspaces=1):
	for i in range(paragraphspaces):
			print('', end='\n')
			
# Execute A Shell Command
def shellcommand(command):
  from subprocess import call
  call(str(command), shell=True)
  
# Update All Packages Installed By Pip
def pipupdate():
  import pip
  from subprocess import call
  packages = [dist.project_name for dist in pip.get_installed_distributions()]
  call("pip install --upgrade " + ' '.join(packages), shell=True)
		
# Get The Absolute Value Of A Number
def absolutenum(number):
	return abs(number)
			
# Split A String
def splitstring(string, split_character=' '):
	return str(string).split(split_character)
	
# Split A String And Get A Specific Part
def splitstringpart(string, split_character=' ', part=1):
	return str(string).split(split_character)[int(part - 1)]
	
# Sort A List Into A Specific Order
def sort(list, key=None):
	if key == None:
		return sorted(list)
	return sorted(list, key)

# Check If A Keyword Relates To Python
def pykeyword(operation='list', keywordtotest=None):
	import keyword
	if operation == 'list':
		return str(keyword.kwlist)
	elif operation == 'check':
		return keyword.iskeyword(str(keywordtotest))
		
# Check If A Number Is In The Fibonacci Sequence
def isfib(number):
	num1 = 1
	num2 = 1
	while True:
		if num2 <= number:
			if num2 == number:
				return True
			else:
				tempnum = num2
				num2 += num1
				num1 = tempnum
		else:
			return False
			
# Do Paper Scissors Rock
def psr(choice):
	from random import randint as randomnum
	choice = choice.lower()
	choices = {'paper': 1, 'papers': 1, 'scissor': 2, 'scissors': 2, 'rock': 3, 'rocks': 3}
	pcchoice = randomnum(0, 3)
	if pcchoice == choices[choice]:
		return 'Tie'
	elif pcchoice < choices[choice]:
		return 'Win'
	elif pcchoice > choices[choice]:
		return 'Loose'
	
# Check If The User Is A Person
def captcha():
	from random import randint as randomnum
	from random import choice as randomitem
	from time import sleep as delay
	numbervalues = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
	numbertext = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
	if randomnum(1, 2) == 2:
		parta = randomitem(numbertext)
	else:
		parta = randomnum(1, 10)
	if randomnum(1, 2) == 2:
		partb = randomitem(numbertext)
	else:
		partb = randomnum(1, 10)
	tryanswer = input('CAPTCHA: What\'s ' + str(parta) + ' + ' + str(partb) + '? Your Answer (In Digits): ')
	if not bool(isinstance(parta, int)):
		parta = numbervalues[parta]
	if not bool(isinstance(partb, int)):
		partb = numbervalues[partb]
	try:
		tryanswer = int(tryanswer)
	except:
		return False
	if parta + partb == tryanswer:
		return True
	else:
		return False

# Set Or Get The Content In The Clipbaord
def clipboard(action='get', text=None):
	import clipboard
	if action == 'get':
		return clipboard.paste()
	elif action == 'set':
		clipboard.copy(str(text))
	elif action == 'append':
		clipboard.copy(str(clipboard.paste) + str(text))
	elif action == 'preceed':
		clipboard.copy(str(text) + str(clipboard.paste))
		
# Convert 0 Or 1 To False Or True
def bintobool(integer):
	if isinteger(integer) and integer < 2 and integer > -1:
		if integer == 0:
			return False
		elif integer == 1:
			return True

# Reload A Module
def modulereload(modulename):
	import importlib
	importlib.reload(modulename)

# Exit The Execution
def exitexecution(arguments=None):
	import sys
	sys.exit(arguments)

# Configure Warnings
def warnconfig(action='default'):
	import warnings
	if action == 'default':
		warnings.filterwarnings("default")
	elif action == 'error':
		warnings.filterwarnings("error")
	elif action == 'ignore':
		warnings.filterwarnings("ignore")
	elif action == 'always':
		warnings.filterwarnings("always")
	elif action == 'module':
		warnings.filterwarnings("module")
	elif action == 'once':
		warnings.filterwarnings("once")
		
# Print Python Copyright Information
def pycopyright():
	import sys
	return sys.copyright

# Print A Message
def message_print(text, times=1):
	for i in range(times):
		print(text)
	
# Solve A Maths Equation
def equation(operation, firstnum, secondnum):
	if not isnumber(firstnum) and isnumber(secondnum):
		raise RuntimeError('An Error Has Occured: One Of The Values Specified Is Not A Number (0002)')
	if operation == 'plus':
		return (firstnum + secondnum)
	elif operation == 'minus':
		return (firstnum - secondnum)
	elif operation == 'multiply':
		return (firstnum * secondnum)
	elif operation == 'divide':
		return (firstnum / secondnum)
	else:
		raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')

# Preform Scientific Operations
def scientific(number, operation, logbase=10):
	import math
	if operation == 'log':
		return math.log(number, logbase)
	elif operation == 'acos':
		return math.acos(number)
	elif operation == 'asin':
		return math.asin(number)
	elif operation == 'atan':
		return math.atan(number)
	elif operation == 'cos':
		return math.cos(number)
	elif operation == 'hypot':
		return math.hypot(number)
	elif operation == 'sin':
		return math.sin(number)
	elif operation == 'tan':
		return math.tan(number)

# Get The Lowest Common Multiple In Two Numbers
def lcm(num1, num2):
	if num1 > num2:
		bigger = num1
	else:
		bigger = num2
	while True:
		if bigger % num1 == 0 and bigger % num2 == 0:
			return bigger
		else:
			bigger += 1
	
# Get The Higest Common Factor In Two Numbers
def hcf(num1, num2):
	if num1 > num2:
		smaller = num2
	else:
		smaller = num1
	for i in range(2, smaller + 1):
		if num1 % i == 0 and num2 % i == 0:
			return i
			
# Get The Factors Of A Number
def factors(number):
	factors = ''
	for i in range(1, number + 1):
		if number % i == 0:
			factors += (str(i) + ', ')
	factors = factors.split(str(number))[0] + str(number)
	return factors
	
# Generate A Completely Random Password
def randpassword(length):
	import string
	from random import randint as randomnum
	charstouse = string.ascii_letters + string.digits + string.punctuation
	password = ''
	for i in range(length):
		password += str(charstouse[randomnum(1, len(charstouse))])
	return password
	
# Generate A Random Character
def randchar():
	from string import printable as charlist
	from string import whitespace as unwanted
	from random import randint as randomnum
	while True:
		try:
			trychar = charlist[randomnum(1, len(charlist))]
			if len(trychar) == 1 and not(trychar in unwanted):
				return trychar
		except:
			nothing = None

# Compare 2 Values
def compare(value1, value2, comparision):
	import operator
	if comparision == 'is':
		return operator.is_(value1, value2)
	elif comparision == 'or':
		return operator.or_(value1, value2)
	elif comparision == 'and':
		return operator.and_(value1, value2)
		
# Use Euler's Formula
def eulercalc(faces, edges, verticies):
	return verticies + edges - faces
		
# Get The Sides Of A Shape
def shapesides(inputtocheck):
	inputtocheck = inputtocheck.lower()
	shapestosides = {'triangle': 3, 'square': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octagon': 8, 'nonagon': 9, 'decagon': 10, \
	'hendecagon': 11, 'dodecagon': 12, 'triskaidecagon': 13, 'tetrakaidecagon': 14, 'pentadecagon': 15, 'hexakaidecagon': 16, 'heptadecagon': 17, 'octakaidecagon': 18, 'enneadecagon': 19, 'Icosagon': 20, \
	'triacontagon': 30, 'tetracontagon': 40, 'pentacontagon': 50, 'hexacontagon': 60, 'heptacontagon': 70, 'octacontagon': 80, 'enneacontagon': 90, 'hectagon': 100, \
	'chiliagon': 1000, 'myriagon': 10000, 'megagon': 1000000, 'googolgon': pow(10, 100)}
	if inputtype == 'shape':
		return shapestosides[inputtocheck]
		
# Compare 2 Numbers
def comparenum(value1, value2, comparison):
	if isnumber(value1) and isnumber(value2):
		comparison = comparison.lower()
		if comparison == 'equals':
			return value1 == value2
		elif comparison == 'not equal':
			return value1 != value2
		elif comparison == 'less than':
			return value1 < value2
		elif comparison == 'greater than':
			return value1 > value2
		elif comparison == 'more than':
			return value1 > value2
		elif comparison == 'less than or equal to':
			return value1 <= value2
		elif comparison == 'greater than or equal to':
			return value1 >= value2
		elif comparison == 'more than or equal to':
			return value1 >= value2
	
# Print Text A Specific Amount Of Times
def texttimes(text, times):
	return times * str(text)
			
# Get The Quadrant Of Coordinates
def quadrant(xcoord,  ycoord):
	xneg = bool(xcoord < 0)
	yneg = bool(ycoord < 0)
	if xneg == True:
		if yneg == False:
			return 2
		else:
			return 3
	elif xneg == False:
		if yneg == False:
			return 1
		else:
			return 4
			
# Flip Coordinates Over A Specific Axis
def flipcoords(xcoord, ycoord, axis):
	axis = axis.lower()
	if axis == 'y':
		if xcoord > 0:
			return str(xcoord - xcoord - xcoord) + ', ' + str(ycoord)
		elif xcoord < 0:
			return str(xcoord + abs(xcoord) * 2) + ', ' + str(ycoord)
		elif xcoord == 0:
			return str(xcoord) + ', ' + str(ycoord)
	elif axis == 'x':
		if ycoord > 0:
			return str(xcoord) + ', ' + str(ycoord - ycoord - ycoord)
		elif ycoord < 0:
			return str(ycoord + abs(ycoord) * 2) + ', ' + str(xcoord)
		elif ycoord == 0:
			return str(xcoord) + ', ' + str(ycoord)

			
# Get The Day Of The Week For A Specific Day
def dayofweek(day, month, year, format=True):
	import calendar
	if format == False:
		return calendar.weekday(year, month, day) + 1
	else:
		if calendar.weekday(year, month, day) == 0:
			return 'Monday'
		elif calendar.weekday(year, month, day) == 1:
			return 'Tuesday'
		elif calendar.weekday(year, month, day) == 2:
			return 'Wednesday'
		elif calendar.weekday(year, month, day) == 3:
			return 'Thursday'
		elif calendar.weekday(year, month, day) == 4:
			return 'Friday'
		elif calendar.weekday(year, month, day) == 5:
			return 'Saturday'
		elif calendar.weekday(year, month, day) == 6:
			return 'Sunday'
			
# Check If A Year Is A Leap Year
def leapyear(year, querytype='is'):
	import calendar
	querytype == querytype.lower()
	if querytype == 'is':
		return calendar.isleap(year)
	elif querytype == 'closest':
		return year % 4

# Return A Random String In Hexadecimal
def tokhex(length=10, urlsafe=False):
	import secrets
	if urlsafe == True:
		return secrets.token_urlsafe(length)
	else:
		return secrets.token_hex(length)
	
# Show A Type Of Face
def face(facetype='smiley'):
	facetype = facetype.lower()
	if facetype == 'smiley':
		print('😃')
	elif facetype == 'straight':
		print('😐')
	elif facetype == 'sad':
		print('☹')

# Simplify A Fraction
def fracsimplify(numerator, denominator):
	if numerator == denominator:
		return '1/1'
	elif numerator > denominator:
		limit = int(numerator / 2)
	elif numerator < denominator:
		limit = int(denominator / 2)
	for i in range(2, limit):
		checknum = limit - i
		if numerator % checknum == 0 and denominator % checknum == 0:
			numerator = numerator / checknum
			denominator = denominator / checknum
	return str(int(numerator)) + '/' + str(int(denominator))
	
# Convert A Circle Measurement
def circleconvert(amount, currentformat, newformat):
	from math import pi
	currentformat = currentformat.lower()
	newformat = newformat.lower()
	if currentformat == newformat:
		return amount
	if currentformat == 'radius':
		if newformat == 'diameter':
			return amount * 2
		elif newformat == 'circumference':
			return amount * 2 * pi
	elif currentformat == 'diameter':
		if newformat == 'radius':
			return amount / 2
		elif newformat == 'circumference':
			return amount * pi
	elif currentformat == 'circumference':
		if newformat == 'radius':
			return amount / pi / 2
		elif newformat == 'diameter':
			return amount / pi

# Get The Amount Of Nummbers Divisable By A Number
def amountdiv(number, minnum, maxnum):
	amount = 0
	for i in range(minnum, maxnum + 1):
		if number % i == 0:
			amount += 1
	return amount
		
# Get A Constant
def constant(constanttype):
	import math
	constanttype = constanttype.lower()
	if constanttype == 'pi':
		return math.pi
	elif constanttype == 'e':
		return math.e
	elif constanttype == 'tau':
		return math.tau
	elif constanttype == 'inf':
		return math.inf
	elif constanttype == 'nan':
		return math.nan
	
# Find The Power Of A Number
def power(number, power):
	import math
	return math.pow(number, power)

# Find The Squareroot Of A number
def squareroot(number):
	import math
	return math.sqrt(number)

# Do An Average Command
def average(numbers, type='mean'):
	import statistics
	type = type.lower()
	try:
		statistics.mean(numbers)
	except:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
	if type == 'mean':
		return statistics.mean(numbers)
	elif type == 'mode':
		return statistics.mode(numbers)
	elif type == 'median':
		return statistics.median(numbers)
	elif type == 'min':
		return min(numbers)
	elif type == 'max':
		return max(numbers)
	elif type == 'range':
		return max(numbers) - min(numbers)
	else:
		raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')

# Throw A Runtime Error
def throwerror(errortext):
	raise RuntimeError(errortext, ' (0001)')
	
# Store A Value In The ros_stored Variable
def store(value):
	global ros_stored
	ros_stored = value
	
# Get The Stored Variable
def getstored():
	return ros_stored
	
# Delay For A Specific Amount Of Seconds
def delay(seconds):
    from time import sleep as rosfunc_sleep
    rosfunc_sleep(seconds)
	
# Waits For The User To Press Enter
def wait_enter(times=1):
	for i in range(times):
		input('')
	
# Convert A Variable To A String
def convertstring(value):
	return str(value)

# Return The Opposite Of A Boolean
def opposite(boolean):
	try:
		return not boolean
	except:
		raise RuntimeError('An Error Has Occured: Nor A Bool Or Len Was Provided (0014)')
	
# Check If A Number Is A Decimal
def isdecimal(value):
	return bool(isinstance(value, float))
	
# Check If A Variable Is A String 
def isstring(variable):
	return bool(isinstance(variable, str))

# Check If A Variable Is A Specific Type
def istype(variable, typeexpected):
	return bool(isinstance(variable, typeexpected))
		
# Check If A Number Is An Integer (Full Number)
def isinteger(value):
	return bool(isinstance(value, int))

# Check For A Boolean
def isboolean(value):
	return isinstance(value, bool)
	
# Check If A Value Is Convertable To A Number (Decimal And Integer)
def isnumber(value):
	try:
		return bool(isinteger(value) or isnumber(value))
	except:
		return False
		
# Sing Happy Birthday
def happybirthday(person):
	from time import sleep as delay
	print('Happy Birthday To You')
	delay(2)
	print('Happy Birthday To You')
	delay(2)
	print('Happy Birthday Dear ' + str(case(person, argument='sentence')))
	delay(2)
	print('Happy Birthday To You')
		
# Change The Casing Of Text
def case(variable, argument='uppercase'):
	if argument == 'uppercase':
		return variable.upper()
	elif argument == 'lowercase':
		return variable.lower()
	elif argument == 'sentence':
		return str(variable[0].upper()) + str(variable[1:])

# Check If A Number Is A Type
def numprop(value, propertyexpected):
	if propertyexpected == 'triangular':
		import math
		x = (math.sqrt(8*value + 1) - 1) / 2
		return bool(x - int(x) > 0)
	elif propertyexpected == 'square':
		from math import sqrt
		return sqrt(value).is_integer()
	elif propertyexpected == 'cube':
		x = value**(1/3)
		x = int(round(x))
		return bool(x**3 == value)
	elif propertyexpected == 'even':
		return value % 2 == 0
	elif propertyexpected == 'odd':
		return not(value % 2 == 0)
	elif propertyexpected == 'positive':
		return bool(value > 0)
	elif propertyexpected == 'negative':
		return bool(value < 0)
	elif propertyexpected == 'zero':
		return bool(value == 0)
		
# Toggle A Number Between Positive And Negative
def posnegtoggle(number):
	if bool(number > 0):
		return number - number * 2
	elif bool(number < 0):
		return number + abs(number) * 2
	elif bool(number == 0):
		return number
		
# Find The Difference Between 2 Numbers
def difference(num1, num2):
	return abs(num1-num2)
		
# Check If A Number Is Divisable By Another Number
def divisable(num1, num2):
	return bool(num1 % num2 == 0)

# Check If A Variable Is Empty
def isempty(variable):
	return bool(variable == '')
	
# Check If A Variable Is Infinite
def isinfinite(variable):
	import math
	return bool(math.isfinite(variable))
	
# Find The Length Of A Value
def length(value):
	try:
		return len(convertstring(value))
	except OverflowError:
		raise RuntimeError('An Error Has Occured: The Length Exceeds The Limit (', charlimit(), ') (0015)')

# Simulate A Cow Saying Text
def cowsay(text='', align='centre'):
	align = align.lower()
	cowtext = str(text)
	topbar = ' '
	bottombar = ' '
	spacing = ''
	for i in range (len(text) + 2):
		topbar = topbar + '_'
		bottombar = bottombar + '-'
	if align == 'centre' or align == 'center':
		for ii in range ((int(len(topbar) / 2)) + 1):
			spacing = spacing + ' '
	elif align == 'left':
		spacing = ' '
	elif align == 'right':
		for iii in range (len(text) + 2):
			spacing = spacing + ' '
	print(topbar)
	print("( " + cowtext + " )")
	print(bottombar)
	print(spacing + 'o   ^__^ ')
	print(spacing + ' o  (oO)\_______' )
	print(spacing + '    (__)\       )\/\ ')
	print(spacing + '     U  ||----w | ')
	print(spacing + '        ||     || ')
	
# Get The Corresponding Letter In A String
def getletter(variable, letternumber):
	return str(variable)[letternumber - 1]

# Play A Chance Game
def chancegame(gamename='dice'):
	gamename = gamename.lower()
	if gamename == 'dice':
		return randomnum(1, 6)
	elif gamename == 'die':
		return randomnum(1, 6)
	elif gamename == 'coin':
		if randomnum(1, 2) == 1:
			return 'Heads'
		else:
			return 'Tails'
	elif gamename == 'truth':
		truthnum = randomnum(1, 4)
		if truthnum == 1:
			return 'Truth'
		elif truthnum == 2:
			return 'Maybe'
		elif truthnum == 3:
			return 'Maybe'
		else:
			return 'Lie'
	elif gamename == 'yes':
		if randomnum(1, 2) == 1:
			return 'Yes'
		else:
			return 'No'

# Check If Something Is On The List
def onlist(list, item):
	return item in list

# Get The Character Limit
def charlimit():
	import sys
	return sys.maxsize

# Get The Highest Unicode Value
def unilimit():
	import sys
	return sys.maxunicode

# Get The Current Platform
def platform():
	import sys
	return sys.platform

# Get The Largest Integer Less Than Or Equal To
def less_or_equal(number):
	import math
	try:
		return math.floor(number)
	except:
		raise RuntimeError('An Error Has Occured: Number Not Provided (0016)')
		
# Join Two Strings
def jointext(firststring, secondstring):
	return str(firststring) + str(secondstring)

# Tools For Directories (If Exists, Make And Delete)
def dirtool(operation, directory):
	operation = operation.lower()
	import os
	if operation == 'exists':
		return bool(os.path.exists(directory))
	elif operation == 'create':
		if os.path.exists(directory):
			raise RuntimeError('An Error Has Occured: Directory Already Exists (0007)')
		else:
			os.makedirs(directory)
	elif operation == 'delete':
		if os.path.exists(directory):
			os.rmdir(directory)
		else:
			raise RuntimeError('An Error Has Occured: Directory Doesn\'t Exist (0009)')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')

# Download A File
def filedownload(source, destination):
	import urllib
	if not isempty(source):
		if not isempty(destination):
			try:
				urllib.request.urlretrieve(source, destination)
			except:
				raise RuntimeError('An Error Has Occured: File Download Error (0010)')
		else:
			raise RuntimeError('An Error Has Occured: Source Or Destination Invalid (0011)')
	else:
		raise RuntimeError('An Error Has Occured: Source Or Destination Invalid (0011)')
	
# Tools For Files (If Exists, Make And Delete)
def file(operation, path):
	operation = operation.lower()
	if operation == 'exists':
		import os.path
		return bool(os.path.isfile(path))
	elif operation == 'read':
		if file('exists', path):
			F = open(path, "w") 
			return F
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'delete':
		import os
		if file('exists', path):
			os.remove(path)
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'create':
		if not file('exists', path):
			f = open(path, "w+")
			f.close()
		else:
			raise RuntimeError('An Error Has Occured: File Already Exists (0013)')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
	
# Tools For Text Files
def text(operation, path, argument):
	operation = operation.lower()
	if operation == 'write':
		if file('exists', path):
			fh = open(path, "w")
			fh.write(argument)
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'append':
		if file('exists', path):
			fh = open(path, "a") 
			fh.write(argument) 
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
			
# About Information
def about():
	print('You Are Using ROS Code')
	print('ROS Code Is Licenced Under The Apache License 2.0')
	print('Type "ros.licence()" To Read The Licence')
	
# Convert Text To Binary Form
def convertbinary(value, argument):
	if argument == 'to':
		try:
			return bin(value)
		except:
			raise RuntimeError('Invalid Value (0016)')
	elif argument == 'from':
		try:
			return format(value)
		except:
			raise RuntimeError('Invalid Value (0016)')
			
# Make The Text Forwards Or Backwards
def reversetext(text, ignoretype=False):
	if ignoretype == False:
		if isinteger(text):
			return int(str(text)[::-1])
		elif isdecimal(text):
			return float(str(text)[::-1])
		else:
			return str(text)[::-1]
	else:
		return str(text)[::-1]
		
# Convert A Time Peroid To Another One
def converttime(time, currentformat, newformat):
	currentformat = currentformat.lower()
	newformat = newformat.lower()
	if currentformat == newformat:
		return time
	if currentformat == 'seconds':
		if newformat == 'milliseconds':
			return time * 1000
		elif newformat == 'minutes':
			return time / 60
		elif newformat == 'hours':
			return time / 60 / 60
		elif newformat == 'days':
			return time / 60 / 60 / 24
		elif newformat == 'weeks':
			return time / 60 / 60 / 24 / 7
		elif newformat == 'fortnights':
			return time / 60 / 60 / 24 / 14
		elif newformat == 'years':
			return time / 60 / 60 / 24 / 365
		elif newformat == 'decades':
			return time / 60 / 60 / 24 / 365 / 10
		elif newformat == 'centuaries':
			return time / 60 / 60 / 24 / 365 / 100
		elif newformat == 'millenniums':
			return time / 60 / 60 / 24 / 365 / 1000
	elif currentformat == 'minutes':
		if newformat == 'milliseconds':
			return time * 60 * 1000
		elif newformat == 'seconds':
			return time * 60
		elif newformat == 'hours':
			return time / 60
		elif newformat == 'days':
			return time / 60 / 24
		elif newformat == 'weeks':
			return time / 60 / 24 / 7
		elif newformat == 'fortnights':
			return time / 60 / 24 / 14
		elif newformat == 'years':
			return time / 60 / 24 / 365
		elif newformat == 'decades':
			return time / 60 / 24 / 365 / 10
		elif newformat == 'centuaries':
			return time / 60 / 24 / 365 / 100
		elif newformat == 'millenniums':
			return time / 60 / 24 / 365 / 1000
	elif currentformat == 'hours':
		if newformat == 'milliseconds':
			return time * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 60 * 60
		elif newformat == 'minutes':
			return time / 60
		elif newformat == 'days':
			return time / 24
		elif newformat == 'weeks':
			return time / 24 / 7
		elif newformat == 'fortnights':
			return time / 24 / 14
		elif newformat == 'years':
			return time / 24 / 7 / 365
		elif newformat == 'decades':
			return time / 24 / 365 / 10
		elif newformat == 'centuaries':
			return time / 24 / 365 / 100
		elif newformat == 'millenniums':
			return time / 24 / 365 / 1000
	elif currentformat == 'days':
		if newformat == 'milliseconds':
			return time * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 24 * 60
		elif newformat == 'hours':
			return time * 24
		elif newformat == 'weeks':
			return time / 24 / 7
		elif newformat == 'fortnights':
			return time / 60 / 24 / 14
		elif newformat == 'years':
			return time / 60 / 24 / 7 / 365
		elif newformat == 'decades':
			return time / 7 / 365 / 10
		elif newformat == 'centuaries':
			return time / 7 / 365 / 100
		elif newformat == 'millenniums':
			return time / 7 / 365 / 1000
	elif currentformat == 'weeks':
		if newformat == 'milliseconds':
			return time * 7 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 7 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 7 * 24 * 60
		elif newformat == 'hours':
			return time * 7 * 24
		elif newformat == 'fortnights':
			return time * 7 / 14
		elif newformat == 'years':
			return time * 7 / 365
		elif newformat == 'decades':
			return time * 7 / 365 / 10
		elif newformat == 'centuaries':
			return time * 7 / 365 / 100
		elif newformat == 'millenniums':
			return time * 7 / 365 / 1000
	elif currentformat == 'fortnights':
		if newformat == 'milliseconds':
			return time * 14 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 14 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 14 * 24 * 60
		elif newformat == 'hours':
			return time * 14 * 24
		elif newformat == 'weeks':
			return time * 14
		elif newformat == 'years':
			return time * 14 / 365
		elif newformat == 'decades':
			return time * 14 / 365 / 10
		elif newformat == 'centuaries':
			return time * 14 / 365 / 100
		elif newformat == 'millenniums':
			return time * 14 / 365 / 1000
	elif currentformat == 'years':
		if newformat == 'milliseconds':
			return time * 365 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 365 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 365 * 24 * 60
		elif newformat == 'hours':
			return time * 365 * 24
		elif newformat == 'days':
			return time * 365
		elif newformat == 'weeks':
			return time * 365 / 7
		elif newformat == 'fortnights':
			return time * 365 / 14
		elif newformat == 'decades':
			return time / 10
		elif newformat == 'centuaries':
			return time / 100
		elif newformat == 'millenniums':
			return time / 1000
	elif currentformat == 'decades':
		if newformat == 'milliseconds':
			return time * 10 * 365 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 10 * 365 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 10 * 365 * 24 * 60
		elif newformat == 'hours':
			return time * 10 * 365 * 24
		elif newformat == 'days':
			return time * 10 * 365
		elif newformat == 'weeks':
			return time *10 * 365 / 7
		elif newformat == 'fortnights':
			return time * 10 * 365 / 14
		elif newformat == 'years':
			return time * 10
		elif newformat == 'centuaries':
			return time * 10 / 100
		elif newformat == 'millenniums':
			return time * 10 / 1000
	elif currentformat == 'centuaries':
		if newformat == 'milliseconds':
			return time * 100 * 365 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 100 * 365 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 100 * 365 * 24 * 60
		elif newformat == 'hours':
			return time * 100 * 365 * 24
		elif newformat == 'days':
			return time * 100 * 365
		elif newformat == 'weeks':
			return time *100 * 365 / 7
		elif newformat == 'fortnights':
			return time * 100 * 365 / 14
		elif newformat == 'years':
			return time * 100
		elif newformat == 'decades':
			return time * 100 / 10
		elif newformat == 'millenniums':
			return time * 100 / 1000
	elif currentformat == 'millenniums':
		if newformat == 'milliseconds':
			return time * 1000 * 365 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 1000 * 365 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 1000 * 365 * 24 * 60
		elif newformat == 'hours':
			return time * 1000 * 365 * 24
		elif newformat == 'days':
			return time * 1000 * 365
		elif newformat == 'weeks':
			return time *1000 * 365 / 7
		elif newformat == 'fortnights':
			return time * 1000 * 365 / 14
		elif newformat == 'years':
			return time * 1000
		elif newformat == 'decades':
			return time * 1000 / 10
		elif newformat == 'centuaries':
			return time * 1000 / 100
		
# Reverse A List
def reverselist(list):
	return list.reverse()
	
# Replace Text In A Variable
def replacetext(string, texttofind, texttoreplace):
	return string.replace(texttofind, texttoreplace)

# Convert A Base 10 Number To A Custom Base
def convertbase(number, base=10):
	import string
	integer = number
	if not integer: return '0'
	sign = 1 if integer > 0 else -1
	alphanum = string.digits + string.ascii_lowercase
	nums = alphanum[:base]
	res = ''
	integer *= sign
	while integer:
                integer, mod = divmod(integer, base)
                res += nums[mod]
	return ('' if sign == 1 else '-') + res[::-1]

# Convert A ASCII Value To A Symbol
def convertsymbol(value, command):
	command = command.lower()
	if command == 'to':
		try:
			return chr(value)
		except ValueError:
			raise RuntimeError('Invalid Symbol Value (0014)')
	elif command == 'from':
		try:
			return ord(value)
		except ValueError:
			raise RuntimeError('Invalid Symbol (0015)')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
			
# Get The Type Of A Value
def gettype(value):
	return type(value)
			
# Get All Available Charaters For A Type
def availchar(charactertype):
	import string
	if charactertype == 'letters':
			return string.ascii_letters
	elif charactertype == 'lowercase':
			return string.ascii_lowercase
	elif charactertype == 'uppercase':
			return string.ascii_uppercase
	elif charactertype == 'digits':
			return string.digits
	elif charactertype == 'hexdigits':
			return string.hexdigits
	elif charactertype == 'punctuation':
			return string.punctuation
	elif charactertype == 'printable':
			return string.printable
	elif charactertype == 'whitespace':
			return string.whitespace
	else:
			raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')

# Get The Value Of A Word
def wordvalue(word):
	total = 0
	for i in range(len(word)):
		total += letternum(word[i])
	return total

# Get The Text Between Two Parts
def textbetween(variable, firstnum=None, secondnum=None, type='regular'):
	if type == 'regular':
		return variable[firstnum:secondnum]
	elif type == 'toend':
		return variable[firstnum:]
	elif type == 'tostart':
		return variable[:secondnum]

# Get The Number Corresponding To A Letter
def letternum(letter):
	if len(letter) == 1 and isstring(letter) :
		letter = letter.lower
		alphaletters = availchar('lowercase')
		for i in range(len(alphaletters)):
			if getletter(letter, 1) == getletter(alphaletters, i + 1):
				return i + 1

# Get Maximum And Minimum Years
def yearlimit(limittype):
	import datetime
	if limittype == 'min':
			return datetime.MINYEAR
	elif limittype == 'max':
			return datetime.MAXYEAR
	else:
			raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
			
# Get The Timezone Code
def timezone():
	import time
	return time.timezone
		
# Get A Random Number
def randomnum(minimum, maximum):
	if isnumber(minimum):
		if isnumber(maximum):
			from random import randint as randomnumber
			return randomnumber(minimum, maximum)
		else:
			raise RuntimeError('Invalid Value (0016)')
	else:
		raise RuntimeError('Invalid Value (0016)')
		
# Open A Link In A Webbrowser
def openurl(url):
	import webbrowser
	try:
		webbrowser.open(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Open A Link In A New Window Of A Webbrowser
def newwindow(url):
	import webbrowser
	try:
		webbrowser.open_new(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Open A Link In A New Tab Of A Webbrowser
def newtab(url):
	import webbrowser
	try:
		webbrowser.open_new_tab(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Get The Name Of The Browser Currently Being Used
def getbrowser():
	import webbrowser
	try:
		webbrowser.get(using=None)
	except:
		return None
	
# Choose A Random Item From A List
def randomstr(valuelist):
	from random import choice
	try:
		return choice(valuelist)
	except IndexError:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
		
# Return The List Equally Spaced
def spacelist(list):
	output = ''
	space = ''
	output += str(list[0])
	space += ' '
	for listnum in range(1, len(list)):
		output += space
		output += str(list[listnum])
	return output

# List Or Count The Numbers Between Two Numbers
def numlistbetween(num1, num2, option='list', listoption='string'):
	if option == 'list':
		if listoption == 'string':
			output = ''
			output += str(num1)
			for currentnum in range(num1 + 1, num2 + 1):
				output += ','
				output += str(currentnum)
		elif listoption == 'list':
			output = []
			for currentnum in range(num1, num2 + 1):
				output.append(str(currentnum))
			return output
	elif option == 'count':
		return num2 - num1
	
# Align Text When Given Full Length
def textalign(text, maxlength, align='left'):
	spaces = ''
	if align == 'left':
		return text
	elif align == 'centre' or align == 'center':
		for i in range(int((maxlength - len(text)) / 2)):
			spaces += ' '
	elif align == 'right':
		for i in range(maxlength - len(text)):
			spaces += ' '
	return spaces + text
		
# Get The Time Since 00:00 On 1 January 1970
def timesince():
	from time import time as time_now
	return time_now()
	
# Fix The Formatting Of Decimals And Integers
def decintfix(decorint=0):
	if str(decorint)[-2:] == '.0':
		return int(decorint)
	else:
		return float(decorint)

# Get The Current Date Or Time
def getdatetime(timedateformat='complete'):
	from datetime import datetime
	timedateformat = timedateformat.lower()
	if timedateformat == 'day':
		return ((str(datetime.now())).split(' ')[0]).split('-')[2]
	elif timedateformat == 'month':
		return ((str(datetime.now())).split(' ')[0]).split('-')[1]
	elif timedateformat == 'year':
		return ((str(datetime.now())).split(' ')[0]).split('-')[0]
	elif timedateformat == 'hour':
		return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
	elif timedateformat == 'minute':
		return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1]
	elif timedateformat == 'second':
		return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2]
	elif timedateformat == 'millisecond':
		return (str(datetime.now())).split('.')[1]
	elif timedateformat == 'yearmonthday':
		return (str(datetime.now())).split(' ')[0]
	elif timedateformat == 'daymonthyear':
		return ((str(datetime.now())).split(' ')[0]).split('-')[2] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[1] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[0]
	elif timedateformat == 'hourminutesecond':
		return ((str(datetime.now())).split(' ')[1]).split('.')[0]
	elif timedateformat == 'secondminutehour':
		return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
	elif timedateformat == 'complete':
		return str(datetime.now())
	elif timedateformat == 'datetime':
		return (str(datetime.now())).split('.')[0]
	elif timedateformat == 'timedate':
		return ((str(datetime.now())).split('.')[0]).split(' ')[1] + ' ' + ((str(datetime.now())).split('.')[0]).split(' ')[0]	
	
# Get User input
def userinput(prompttext):
	try:
		return input(prompttext)
	except:
		return input(str(prompttext))
		
# Licence Information
def licence(raw=False):
	if raw == False:
		print('ROS Code Is Licenced Under The Apache License 2.0')
		print(u'\u2714' + ' Permissions: Commercial use, Modification, Distribution, Patent use And Private use')
		print(u'\u274c' + ' Limitations: Trademark use, Liability And Warranty')
		print(u'\u2139' + ' Conditions: License and copyright notice And State changes')
		print('To View The Full Licence, Go To: https://rosurl.ga/ROS-Code-Licence')
	else:
		print('ROS Code Is Licenced Under The Apache License 2.0')
		print('Permissions: Commercial use, Modification, Distribution, Patent use And Private use')
		print('Limitations: Trademark use, Liability And Warranty')
		print('Conditions: License and copyright notice And State changes')
		print('To View The Full Licence, Go To: https://rosurl.ga/ROS-Code-Licence')

print('Finished Loading ROS Code')

# End ROS Code# Start ROS Code

print('Loading ROS Code')

# Prepare Debug Enabled Variable For Toggling Debug Mode
def debug_debugstatesetup():
	global debugenabled
	debugenabled = False

debug_debugstatesetup()

# DEBUG: Enable Or Disable Debug Mode
def debugstate(state):
    if state == 'Enable':
        debugenabled = True
        print('Debug Mode Has Been Enabled')
    elif state == 'Disable':
        debugenabled = False
        print('Debug Mode Has Been Disabled')
    else:
        raise RuntimeError('An Error Has Occured: Invalid Debug State Entered (0005)')
		
# DEBUG: Make ROS Code Variables Global
def debug_varglobal():
	if debugenabled == True:
		global ros_output
		global ros_stored
	else:
		raise RuntimeError('An Error Has Occured: Debug Mode Not Enabled (0006)')
		
# DEBUG: Supress All Warnings
def debug_supresswarnings():
	if debugenabled == True:
		import warnings
		warnings.filterwarnings("ignore")
	else:
		raise RuntimeError('An Error Has Occured: Debug Mode Not Enabled (0006)')

# Check If A Number Is A Prime Number
def isprime(number):
	if number == 1:
		return False
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			return False
	return True
	
# Make A Paragraph Space
def paraspace(paragraphspaces=1):
	for i in range(paragraphspaces):
			print('', end='\n')
		
# Get The Absolute Value Of A Number
def absolutenum(number):
	return abs(number)
			
# Split A String
def splitstring(string, split_character=' '):
	return str(string).split(split_character)
	
# Split A String And Get A Specific Part
def splitstringpart(string, split_character=' ', part=1):
	return str(string).split(split_character)[int(part - 1)]
	
# Sort A List Into A Specific Order
def sort(list, key=None):
	if key == None:
		return sorted(list)
	return sorted(list, key)

# Check If A Keyword Relates To Python
def pykeyword(operation='list', keywordtotest=None):
	import keyword
	if operation == 'list':
		return str(keyword.kwlist)
	elif operation == 'check':
		return keyword.iskeyword(str(keywordtotest))
		
# Check If A Number Is In The Fibonacci Sequence
def isfib(number):
	num1 = 1
	num2 = 1
	while True:
		if num2 <= number:
			if num2 == number:
				return True
			else:
				tempnum = num2
				num2 += num1
				num1 = tempnum
		else:
			return False
			
# Do Paper Scissors Rock
def psr(choice):
	from random import randint as randomnum
	choice = choice.lower()
	choices = {'paper': 1, 'papers': 1, 'scissor': 2, 'scissors': 2, 'rock': 3, 'rocks': 3}
	pcchoice = randomnum(0, 3)
	if pcchoice == choices[choice]:
		return 'Tie'
	elif pcchoice < choices[choice]:
		return 'Win'
	elif pcchoice > choices[choice]:
		return 'Loose'
	
# Check If The User Is A Person
def captcha():
	from random import randint as randomnum
	from random import choice as randomitem
	from time import sleep as delay
	numbervalues = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
	numbertext = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
	if randomnum(1, 2) == 2:
		parta = randomitem(numbertext)
	else:
		parta = randomnum(1, 10)
	if randomnum(1, 2) == 2:
		partb = randomitem(numbertext)
	else:
		partb = randomnum(1, 10)
	tryanswer = input('CAPTCHA: What\'s ' + str(parta) + ' + ' + str(partb) + '? Your Answer (In Digits): ')
	if not bool(isinstance(parta, int)):
		parta = numbervalues[parta]
	if not bool(isinstance(partb, int)):
		partb = numbervalues[partb]
	try:
		tryanswer = int(tryanswer)
	except:
		return False
	if parta + partb == tryanswer:
		return True
	else:
		return False

# Set Or Get The Content In The Clipbaord
def clipboard(action='get', text=None):
	import clipboard
	if action == 'get':
		return clipboard.paste()
	elif action == 'set':
		clipboard.copy(str(text))
	elif action == 'append':
		clipboard.copy(str(clipboard.paste) + str(text))
	elif action == 'preceed':
		clipboard.copy(str(text) + str(clipboard.paste))
		
# Convert 0 Or 1 To False Or True
def bintobool(integer):
	if isinteger(integer) and integer < 2 and integer > -1:
		if integer == 0:
			return False
		elif integer == 1:
			return True

# Reload A Module
def modulereload(modulename):
	import importlib
	importlib.reload(modulename)

# Exit The Execution
def exitexecution(arguments=None):
	import sys
	sys.exit(arguments)

# Configure Warnings
def warnconfig(action='default'):
	import warnings
	if action == 'default':
		warnings.filterwarnings("default")
	elif action == 'error':
		warnings.filterwarnings("error")
	elif action == 'ignore':
		warnings.filterwarnings("ignore")
	elif action == 'always':
		warnings.filterwarnings("always")
	elif action == 'module':
		warnings.filterwarnings("module")
	elif action == 'once':
		warnings.filterwarnings("once")
		
# Print Python Copyright Information
def pycopyright():
	import sys
	return sys.copyright

# Print A Message
def message_print(text, times=1):
	for i in range(times):
		print(text)
	
# Solve A Maths Equation
def equation(operation, firstnum, secondnum):
	if not isnumber(firstnum) and isnumber(secondnum):
		raise RuntimeError('An Error Has Occured: One Of The Values Specified Is Not A Number (0002)')
	if operation == 'plus':
		return (firstnum + secondnum)
	elif operation == 'minus':
		return (firstnum - secondnum)
	elif operation == 'multiply':
		return (firstnum * secondnum)
	elif operation == 'divide':
		return (firstnum / secondnum)
	else:
		raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')

# Preform Scientific Operations
def scientific(number, operation, logbase=10):
	import math
	if operation == 'log':
		return math.log(number, logbase)
	elif operation == 'acos':
		return math.acos(number)
	elif operation == 'asin':
		return math.asin(number)
	elif operation == 'atan':
		return math.atan(number)
	elif operation == 'cos':
		return math.cos(number)
	elif operation == 'hypot':
		return math.hypot(number)
	elif operation == 'sin':
		return math.sin(number)
	elif operation == 'tan':
		return math.tan(number)

# Get The Lowest Common Multiple In Two Numbers
def lcm(num1, num2):
	if num1 > num2:
		bigger = num1
	else:
		bigger = num2
	while True:
		if bigger % num1 == 0 and bigger % num2 == 0:
			return bigger
		else:
			bigger += 1
	
# Get The Higest Common Factor In Two Numbers
def hcf(num1, num2):
	if num1 > num2:
		smaller = num2
	else:
		smaller = num1
	for i in range(2, smaller + 1):
		if num1 % i == 0 and num2 % i == 0:
			return i
			
# Get The Factors Of A Number
def factors(number):
	factors = ''
	for i in range(1, number + 1):
		if number % i == 0:
			factors += (str(i) + ', ')
	factors = factors.split(str(number))[0] + str(number)
	return factors
	
# Generate A Completely Random Password
def randpassword(length):
	import string
	from random import randint as randomnum
	charstouse = string.ascii_letters + string.digits + string.punctuation
	password = ''
	for i in range(length):
		password += str(charstouse[randomnum(1, len(charstouse))])
	return password
	
# Generate A Random Character
def randchar():
	from string import printable as charlist
	from string import whitespace as unwanted
	from random import randint as randomnum
	while True:
		try:
			trychar = charlist[randomnum(1, len(charlist))]
			if len(trychar) == 1 and not(trychar in unwanted):
				return trychar
		except:
			nothing = None

# Compare 2 Values
def compare(value1, value2, comparision):
	import operator
	if comparision == 'is':
		return operator.is_(value1, value2)
	elif comparision == 'or':
		return operator.or_(value1, value2)
	elif comparision == 'and':
		return operator.and_(value1, value2)
		
# Use Euler's Formula
def eulercalc(faces, edges, verticies):
	return verticies + edges - faces
		
# Get The Sides Of A Shape
def shapesides(inputtocheck):
	inputtocheck = inputtocheck.lower()
	shapestosides = {'triangle': 3, 'square': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octagon': 8, 'nonagon': 9, 'decagon': 10, \
	'hendecagon': 11, 'dodecagon': 12, 'triskaidecagon': 13, 'tetrakaidecagon': 14, 'pentadecagon': 15, 'hexakaidecagon': 16, 'heptadecagon': 17, 'octakaidecagon': 18, 'enneadecagon': 19, 'Icosagon': 20, \
	'triacontagon': 30, 'tetracontagon': 40, 'pentacontagon': 50, 'hexacontagon': 60, 'heptacontagon': 70, 'octacontagon': 80, 'enneacontagon': 90, 'hectagon': 100, \
	'chiliagon': 1000, 'myriagon': 10000, 'megagon': 1000000, 'googolgon': pow(10, 100)}
	if inputtype == 'shape':
		return shapestosides[inputtocheck]
		
# Compare 2 Numbers
def comparenum(value1, value2, comparison):
	if isnumber(value1) and isnumber(value2):
		comparison = comparison.lower()
		if comparison == 'equals':
			return value1 == value2
		elif comparison == 'not equal':
			return value1 != value2
		elif comparison == 'less than':
			return value1 < value2
		elif comparison == 'greater than':
			return value1 > value2
		elif comparison == 'more than':
			return value1 > value2
		elif comparison == 'less than or equal to':
			return value1 <= value2
		elif comparison == 'greater than or equal to':
			return value1 >= value2
		elif comparison == 'more than or equal to':
			return value1 >= value2
	
# Print Text A Specific Amount Of Times
def texttimes(text, times):
	return times * str(text)
			
# Get The Quadrant Of Coordinates
def quadrant(xcoord,  ycoord):
	xneg = bool(xcoord < 0)
	yneg = bool(ycoord < 0)
	if xneg == True:
		if yneg == False:
			return 2
		else:
			return 3
	elif xneg == False:
		if yneg == False:
			return 1
		else:
			return 4
			
# Flip Coordinates Over A Specific Axis
def flipcoords(xcoord, ycoord, axis):
	axis = axis.lower()
	if axis == 'y':
		if xcoord > 0:
			return str(xcoord - xcoord - xcoord) + ', ' + str(ycoord)
		elif xcoord < 0:
			return str(xcoord + abs(xcoord) * 2) + ', ' + str(ycoord)
		elif xcoord == 0:
			return str(xcoord) + ', ' + str(ycoord)
	elif axis == 'x':
		if ycoord > 0:
			return str(xcoord) + ', ' + str(ycoord - ycoord - ycoord)
		elif ycoord < 0:
			return str(ycoord + abs(ycoord) * 2) + ', ' + str(xcoord)
		elif ycoord == 0:
			return str(xcoord) + ', ' + str(ycoord)

			
# Get The Day Of The Week For A Specific Day
def dayofweek(day, month, year, format=True):
	import calendar
	if format == False:
		return calendar.weekday(year, month, day) + 1
	else:
		if calendar.weekday(year, month, day) == 0:
			return 'Monday'
		elif calendar.weekday(year, month, day) == 1:
			return 'Tuesday'
		elif calendar.weekday(year, month, day) == 2:
			return 'Wednesday'
		elif calendar.weekday(year, month, day) == 3:
			return 'Thursday'
		elif calendar.weekday(year, month, day) == 4:
			return 'Friday'
		elif calendar.weekday(year, month, day) == 5:
			return 'Saturday'
		elif calendar.weekday(year, month, day) == 6:
			return 'Sunday'
			
# Check If A Year Is A Leap Year
def leapyear(year, querytype='is'):
	import calendar
	querytype == querytype.lower()
	if querytype == 'is':
		return calendar.isleap(year)
	elif querytype == 'closest':
		return year % 4

# Return A Random String In Hexadecimal
def tokhex(length=10, urlsafe=False):
	import secrets
	if urlsafe == True:
		return secrets.token_urlsafe(length)
	else:
		return secrets.token_hex(length)
	
# Show A Type Of Face
def face(facetype='smiley'):
	facetype = facetype.lower()
	if facetype == 'smiley':
		print('😃')
	elif facetype == 'straight':
		print('😐')
	elif facetype == 'sad':
		print('☹')

# Simplify A Fraction
def fracsimplify(numerator, denominator):
	if numerator == denominator:
		return '1/1'
	elif numerator > denominator:
		limit = int(numerator / 2)
	elif numerator < denominator:
		limit = int(denominator / 2)
	for i in range(2, limit):
		checknum = limit - i
		if numerator % checknum == 0 and denominator % checknum == 0:
			numerator = numerator / checknum
			denominator = denominator / checknum
	return str(int(numerator)) + '/' + str(int(denominator))
	
# Convert A Circle Measurement
def circleconvert(amount, currentformat, newformat):
	from math import pi
	currentformat = currentformat.lower()
	newformat = newformat.lower()
	if currentformat == newformat:
		return amount
	if currentformat == 'radius':
		if newformat == 'diameter':
			return amount * 2
		elif newformat == 'circumference':
			return amount * 2 * pi
	elif currentformat == 'diameter':
		if newformat == 'radius':
			return amount / 2
		elif newformat == 'circumference':
			return amount * pi
	elif currentformat == 'circumference':
		if newformat == 'radius':
			return amount / pi / 2
		elif newformat == 'diameter':
			return amount / pi

# Get The Amount Of Nummbers Divisable By A Number
def amountdiv(number, minnum, maxnum):
	amount = 0
	for i in range(minnum, maxnum + 1):
		if number % i == 0:
			amount += 1
	return amount
		
# Get A Constant
def constant(constanttype):
	import math
	constanttype = constanttype.lower()
	if constanttype == 'pi':
		return math.pi
	elif constanttype == 'e':
		return math.e
	elif constanttype == 'tau':
		return math.tau
	elif constanttype == 'inf':
		return math.inf
	elif constanttype == 'nan':
		return math.nan
	
# Find The Power Of A Number
def power(number, power):
	import math
	return math.pow(number, power)

# Find The Squareroot Of A number
def squareroot(number):
	import math
	return math.sqrt(number)

# Do An Average Command
def average(numbers, type='mean'):
	import statistics
	type = type.lower()
	try:
		statistics.mean(numbers)
	except:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
	if type == 'mean':
		return statistics.mean(numbers)
	elif type == 'mode':
		return statistics.mode(numbers)
	elif type == 'median':
		return statistics.median(numbers)
	elif type == 'min':
		return min(numbers)
	elif type == 'max':
		return max(numbers)
	elif type == 'range':
		return max(numbers) - min(numbers)
	else:
		raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')

# Throw A Runtime Error
def throwerror(errortext):
	raise RuntimeError(errortext, ' (0001)')
	
# Store A Value In The ros_stored Variable
def store(value):
	global ros_stored
	ros_stored = value
	
# Get The Stored Variable
def getstored():
	return ros_stored
	
# Delay For A Specific Amount Of Seconds
def delay(seconds):
    from time import sleep as rosfunc_sleep
    rosfunc_sleep(seconds)
	
# Waits For The User To Press Enter
def wait_enter(times=1):
	for i in range(times):
		input('')
	
# Convert A Variable To A String
def convertstring(value):
	return str(value)

# Return The Opposite Of A Boolean
def opposite(boolean):
	try:
		return not boolean
	except:
		raise RuntimeError('An Error Has Occured: Nor A Bool Or Len Was Provided (0014)')
	
# Check If A Number Is A Decimal
def isdecimal(value):
	return bool(isinstance(value, float))
	
# Check If A Variable Is A String 
def isstring(variable):
	return bool(isinstance(variable, str))

# Check If A Variable Is A Specific Type
def istype(variable, typeexpected):
	return bool(isinstance(variable, typeexpected))
		
# Check If A Number Is An Integer (Full Number)
def isinteger(value):
	return bool(isinstance(value, int))

# Check For A Boolean
def isboolean(value):
	return isinstance(value, bool)
	
# Check If A Value Is Convertable To A Number (Decimal And Integer)
def isnumber(value):
	try:
		return bool(isinteger(value) or isnumber(value))
	except:
		return False
		
# Sing Happy Birthday
def happybirthday(person):
	from time import sleep as delay
	print('Happy Birthday To You')
	delay(2)
	print('Happy Birthday To You')
	delay(2)
	print('Happy Birthday Dear ' + str(case(person, argument='sentence')))
	delay(2)
	print('Happy Birthday To You')
		
# Change The Casing Of Text
def case(variable, argument='uppercase'):
	if argument == 'uppercase':
		return variable.upper()
	elif argument == 'lowercase':
		return variable.lower()
	elif argument == 'sentence':
		return str(variable[0].upper()) + str(variable[1:])

# Check If A Number Is A Type
def numprop(value, propertyexpected):
	if propertyexpected == 'triangular':
		import math
		x = (math.sqrt(8*value + 1) - 1) / 2
		return bool(x - int(x) > 0)
	elif propertyexpected == 'square':
		from math import sqrt
		return sqrt(value).is_integer()
	elif propertyexpected == 'cube':
		x = value**(1/3)
		x = int(round(x))
		return bool(x**3 == value)
	elif propertyexpected == 'even':
		return value % 2 == 0
	elif propertyexpected == 'odd':
		return not(value % 2 == 0)
	elif propertyexpected == 'positive':
		return bool(value > 0)
	elif propertyexpected == 'negative':
		return bool(value < 0)
	elif propertyexpected == 'zero':
		return bool(value == 0)
		
# Toggle A Number Between Positive And Negative
def posnegtoggle(number):
	if bool(number > 0):
		return number - number * 2
	elif bool(number < 0):
		return number + abs(number) * 2
	elif bool(number == 0):
		return number
		
# Find The Difference Between 2 Numbers
def difference(num1, num2):
	return abs(num1-num2)
		
# Check If A Number Is Divisable By Another Number
def divisable(num1, num2):
	return bool(num1 % num2 == 0)

# Check If A Variable Is Empty
def isempty(variable):
	return bool(variable == '')
	
# Check If A Variable Is Infinite
def isinfinite(variable):
	import math
	return bool(math.isfinite(variable))
	
# Find The Length Of A Value
def length(value):
	try:
		return len(convertstring(value))
	except OverflowError:
		raise RuntimeError('An Error Has Occured: The Length Exceeds The Limit (', charlimit(), ') (0015)')

# Simulate A Cow Saying Text
def cowsay(text='', align='centre'):
	align = align.lower()
	cowtext = str(text)
	topbar = ' '
	bottombar = ' '
	spacing = ''
	for i in range (len(text) + 2):
		topbar = topbar + '_'
		bottombar = bottombar + '-'
	if align == 'centre' or align == 'center':
		for ii in range ((int(len(topbar) / 2)) + 1):
			spacing = spacing + ' '
	elif align == 'left':
		spacing = ' '
	elif align == 'right':
		for iii in range (len(text) + 2):
			spacing = spacing + ' '
	print(topbar)
	print("( " + cowtext + " )")
	print(bottombar)
	print(spacing + 'o   ^__^ ')
	print(spacing + ' o  (oO)\_______' )
	print(spacing + '    (__)\       )\/\ ')
	print(spacing + '     U  ||----w | ')
	print(spacing + '        ||     || ')
	
# Get The Corresponding Letter In A String
def getletter(variable, letternumber):
	return str(variable)[letternumber - 1]

# Play A Chance Game
def chancegame(gamename='dice'):
	gamename = gamename.lower()
	if gamename == 'dice':
		return randomnum(1, 6)
	elif gamename == 'die':
		return randomnum(1, 6)
	elif gamename == 'coin':
		if randomnum(1, 2) == 1:
			return 'Heads'
		else:
			return 'Tails'
	elif gamename == 'truth':
		truthnum = randomnum(1, 4)
		if truthnum == 1:
			return 'Truth'
		elif truthnum == 2:
			return 'Maybe'
		elif truthnum == 3:
			return 'Maybe'
		else:
			return 'Lie'
	elif gamename == 'yes':
		if randomnum(1, 2) == 1:
			return 'Yes'
		else:
			return 'No'

# Check If Something Is On The List
def onlist(list, item):
	return item in list

# Get The Character Limit
def charlimit():
	import sys
	return sys.maxsize

# Get The Highest Unicode Value
def unilimit():
	import sys
	return sys.maxunicode

# Get The Current Platform
def platform():
	import sys
	return sys.platform

# Get The Largest Integer Less Than Or Equal To
def less_or_equal(number):
	import math
	try:
		return math.floor(number)
	except:
		raise RuntimeError('An Error Has Occured: Number Not Provided (0016)')
		
# Join Two Strings
def jointext(firststring, secondstring):
	return str(firststring) + str(secondstring)

# Tools For Directories (If Exists, Make And Delete)
def dirtool(operation, directory):
	operation = operation.lower()
	import os
	if operation == 'exists':
		return bool(os.path.exists(directory))
	elif operation == 'create':
		if os.path.exists(directory):
			raise RuntimeError('An Error Has Occured: Directory Already Exists (0007)')
		else:
			os.makedirs(directory)
	elif operation == 'delete':
		if os.path.exists(directory):
			os.rmdir(directory)
		else:
			raise RuntimeError('An Error Has Occured: Directory Doesn\'t Exist (0009)')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')

# Download A File
def filedownload(source, destination):
	import urllib
	if not isempty(source):
		if not isempty(destination):
			try:
				urllib.request.urlretrieve(source, destination)
			except:
				raise RuntimeError('An Error Has Occured: File Download Error (0010)')
		else:
			raise RuntimeError('An Error Has Occured: Source Or Destination Invalid (0011)')
	else:
		raise RuntimeError('An Error Has Occured: Source Or Destination Invalid (0011)')
	
# Tools For Files (If Exists, Make And Delete)
def file(operation, path):
	operation = operation.lower()
	if operation == 'exists':
		import os.path
		return bool(os.path.isfile(path))
	elif operation == 'read':
		if file('exists', path):
			F = open(path, "w") 
			return F
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'delete':
		import os
		if file('exists', path):
			os.remove(path)
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'create':
		if not file('exists', path):
			f = open(path, "w+")
			f.close()
		else:
			raise RuntimeError('An Error Has Occured: File Already Exists (0013)')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
	
# Tools For Text Files
def text(operation, path, argument):
	operation = operation.lower()
	if operation == 'write':
		if file('exists', path):
			fh = open(path, "w")
			fh.write(argument)
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'append':
		if file('exists', path):
			fh = open(path, "a") 
			fh.write(argument) 
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
			
# About Information
def about():
	print('You Are Using ROS Code')
	print('ROS Code Is Licenced Under The Apache License 2.0')
	print('Type "ros.licence()" To Read The Licence')
	
# Convert Text To Binary Form
def convertbinary(value, argument):
	if argument == 'to':
		try:
			return bin(value)
		except:
			raise RuntimeError('Invalid Value (0016)')
	elif argument == 'from':
		try:
			return format(value)
		except:
			raise RuntimeError('Invalid Value (0016)')
			
# Make The Text Forwards Or Backwards
def reversetext(text, ignoretype=False):
	if ignoretype == False:
		if isinteger(text):
			return int(str(text)[::-1])
		elif isdecimal(text):
			return float(str(text)[::-1])
		else:
			return str(text)[::-1]
	else:
		return str(text)[::-1]
		
# Convert A Time Peroid To Another One
def converttime(time, currentformat, newformat):
	currentformat = currentformat.lower()
	newformat = newformat.lower()
	if currentformat == newformat:
		return time
	if currentformat == 'seconds':
		if newformat == 'milliseconds':
			return time * 1000
		elif newformat == 'minutes':
			return time / 60
		elif newformat == 'hours':
			return time / 60 / 60
		elif newformat == 'days':
			return time / 60 / 60 / 24
		elif newformat == 'weeks':
			return time / 60 / 60 / 24 / 7
		elif newformat == 'fortnights':
			return time / 60 / 60 / 24 / 14
		elif newformat == 'years':
			return time / 60 / 60 / 24 / 365
		elif newformat == 'decades':
			return time / 60 / 60 / 24 / 365 / 10
		elif newformat == 'centuaries':
			return time / 60 / 60 / 24 / 365 / 100
		elif newformat == 'millenniums':
			return time / 60 / 60 / 24 / 365 / 1000
	elif currentformat == 'minutes':
		if newformat == 'milliseconds':
			return time * 60 * 1000
		elif newformat == 'seconds':
			return time * 60
		elif newformat == 'hours':
			return time / 60
		elif newformat == 'days':
			return time / 60 / 24
		elif newformat == 'weeks':
			return time / 60 / 24 / 7
		elif newformat == 'fortnights':
			return time / 60 / 24 / 14
		elif newformat == 'years':
			return time / 60 / 24 / 365
		elif newformat == 'decades':
			return time / 60 / 24 / 365 / 10
		elif newformat == 'centuaries':
			return time / 60 / 24 / 365 / 100
		elif newformat == 'millenniums':
			return time / 60 / 24 / 365 / 1000
	elif currentformat == 'hours':
		if newformat == 'milliseconds':
			return time * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 60 * 60
		elif newformat == 'minutes':
			return time / 60
		elif newformat == 'days':
			return time / 24
		elif newformat == 'weeks':
			return time / 24 / 7
		elif newformat == 'fortnights':
			return time / 24 / 14
		elif newformat == 'years':
			return time / 24 / 7 / 365
		elif newformat == 'decades':
			return time / 24 / 365 / 10
		elif newformat == 'centuaries':
			return time / 24 / 365 / 100
		elif newformat == 'millenniums':
			return time / 24 / 365 / 1000
	elif currentformat == 'days':
		if newformat == 'milliseconds':
			return time * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 24 * 60
		elif newformat == 'hours':
			return time * 24
		elif newformat == 'weeks':
			return time / 24 / 7
		elif newformat == 'fortnights':
			return time / 60 / 24 / 14
		elif newformat == 'years':
			return time / 60 / 24 / 7 / 365
		elif newformat == 'decades':
			return time / 7 / 365 / 10
		elif newformat == 'centuaries':
			return time / 7 / 365 / 100
		elif newformat == 'millenniums':
			return time / 7 / 365 / 1000
	elif currentformat == 'weeks':
		if newformat == 'milliseconds':
			return time * 7 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 7 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 7 * 24 * 60
		elif newformat == 'hours':
			return time * 7 * 24
		elif newformat == 'fortnights':
			return time * 7 / 14
		elif newformat == 'years':
			return time * 7 / 365
		elif newformat == 'decades':
			return time * 7 / 365 / 10
		elif newformat == 'centuaries':
			return time * 7 / 365 / 100
		elif newformat == 'millenniums':
			return time * 7 / 365 / 1000
	elif currentformat == 'fortnights':
		if newformat == 'milliseconds':
			return time * 14 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 14 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 14 * 24 * 60
		elif newformat == 'hours':
			return time * 14 * 24
		elif newformat == 'weeks':
			return time * 14
		elif newformat == 'years':
			return time * 14 / 365
		elif newformat == 'decades':
			return time * 14 / 365 / 10
		elif newformat == 'centuaries':
			return time * 14 / 365 / 100
		elif newformat == 'millenniums':
			return time * 14 / 365 / 1000
	elif currentformat == 'years':
		if newformat == 'milliseconds':
			return time * 365 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 365 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 365 * 24 * 60
		elif newformat == 'hours':
			return time * 365 * 24
		elif newformat == 'days':
			return time * 365
		elif newformat == 'weeks':
			return time * 365 / 7
		elif newformat == 'fortnights':
			return time * 365 / 14
		elif newformat == 'decades':
			return time / 10
		elif newformat == 'centuaries':
			return time / 100
		elif newformat == 'millenniums':
			return time / 1000
	elif currentformat == 'decades':
		if newformat == 'milliseconds':
			return time * 10 * 365 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 10 * 365 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 10 * 365 * 24 * 60
		elif newformat == 'hours':
			return time * 10 * 365 * 24
		elif newformat == 'days':
			return time * 10 * 365
		elif newformat == 'weeks':
			return time *10 * 365 / 7
		elif newformat == 'fortnights':
			return time * 10 * 365 / 14
		elif newformat == 'years':
			return time * 10
		elif newformat == 'centuaries':
			return time * 10 / 100
		elif newformat == 'millenniums':
			return time * 10 / 1000
	elif currentformat == 'centuaries':
		if newformat == 'milliseconds':
			return time * 100 * 365 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 100 * 365 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 100 * 365 * 24 * 60
		elif newformat == 'hours':
			return time * 100 * 365 * 24
		elif newformat == 'days':
			return time * 100 * 365
		elif newformat == 'weeks':
			return time *100 * 365 / 7
		elif newformat == 'fortnights':
			return time * 100 * 365 / 14
		elif newformat == 'years':
			return time * 100
		elif newformat == 'decades':
			return time * 100 / 10
		elif newformat == 'millenniums':
			return time * 100 / 1000
	elif currentformat == 'millenniums':
		if newformat == 'milliseconds':
			return time * 1000 * 365 * 24 * 60 * 60 * 1000
		elif newformat == 'seconds':
			return time * 1000 * 365 * 24 * 60 * 60
		elif newformat == 'minutes':
			return time * 1000 * 365 * 24 * 60
		elif newformat == 'hours':
			return time * 1000 * 365 * 24
		elif newformat == 'days':
			return time * 1000 * 365
		elif newformat == 'weeks':
			return time *1000 * 365 / 7
		elif newformat == 'fortnights':
			return time * 1000 * 365 / 14
		elif newformat == 'years':
			return time * 1000
		elif newformat == 'decades':
			return time * 1000 / 10
		elif newformat == 'centuaries':
			return time * 1000 / 100
		
# Reverse A List
def reverselist(list):
	return list.reverse()
	
# Replace Text In A Variable
def replacetext(string, texttofind, texttoreplace):
	return string.replace(texttofind, texttoreplace)

# Convert A Base 10 Number To A Custom Base
def convertbase(number, base=10):
	import string
	integer = number
	if not integer: return '0'
	sign = 1 if integer > 0 else -1
	alphanum = string.digits + string.ascii_lowercase
	nums = alphanum[:base]
	res = ''
	integer *= sign
	while integer:
                integer, mod = divmod(integer, base)
                res += nums[mod]
	return ('' if sign == 1 else '-') + res[::-1]

# Convert A ASCII Value To A Symbol
def convertsymbol(value, command):
	command = command.lower()
	if command == 'to':
		try:
			return chr(value)
		except ValueError:
			raise RuntimeError('Invalid Symbol Value (0014)')
	elif command == 'from':
		try:
			return ord(value)
		except ValueError:
			raise RuntimeError('Invalid Symbol (0015)')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
			
# Get The Type Of A Value
def gettype(value):
	return type(value)
			
# Get All Available Charaters For A Type
def availchar(charactertype):
	import string
	if charactertype == 'letters':
			return string.ascii_letters
	elif charactertype == 'lowercase':
			return string.ascii_lowercase
	elif charactertype == 'uppercase':
			return string.ascii_uppercase
	elif charactertype == 'digits':
			return string.digits
	elif charactertype == 'hexdigits':
			return string.hexdigits
	elif charactertype == 'punctuation':
			return string.punctuation
	elif charactertype == 'printable':
			return string.printable
	elif charactertype == 'whitespace':
			return string.whitespace
	else:
			raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')

# Get The Value Of A Word
def wordvalue(word):
	total = 0
	for i in range(len(word)):
		total += letternum(word[i])
	return total

# Get The Text Between Two Parts
def textbetween(variable, firstnum=None, secondnum=None, type='regular'):
	if type == 'regular':
		return variable[firstnum:secondnum]
	elif type == 'toend':
		return variable[firstnum:]
	elif type == 'tostart':
		return variable[:secondnum]

# Get The Number Corresponding To A Letter
def letternum(letter):
	if len(letter) == 1 and isstring(letter) :
		letter = letter.lower
		alphaletters = availchar('lowercase')
		for i in range(len(alphaletters)):
			if getletter(letter, 1) == getletter(alphaletters, i + 1):
				return i + 1

# Get Maximum And Minimum Years
def yearlimit(limittype):
	import datetime
	if limittype == 'min':
			return datetime.MINYEAR
	elif limittype == 'max':
			return datetime.MAXYEAR
	else:
			raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
			
# Get The Timezone Code
def timezone():
	import time
	return time.timezone
		
# Get A Random Number
def randomnum(minimum, maximum):
	if isnumber(minimum):
		if isnumber(maximum):
			from random import randint as randomnumber
			return randomnumber(minimum, maximum)
		else:
			raise RuntimeError('Invalid Value (0016)')
	else:
		raise RuntimeError('Invalid Value (0016)')
		
# Open A Link In A Webbrowser
def openurl(url):
	import webbrowser
	try:
		webbrowser.open(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Open A Link In A New Window Of A Webbrowser
def newwindow(url):
	import webbrowser
	try:
		webbrowser.open_new(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Open A Link In A New Tab Of A Webbrowser
def newtab(url):
	import webbrowser
	try:
		webbrowser.open_new_tab(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Get The Name Of The Browser Currently Being Used
def getbrowser():
	import webbrowser
	try:
		webbrowser.get(using=None)
	except:
		return None
	
# Choose A Random Item From A List
def randomstr(valuelist):
	from random import choice
	try:
		return choice(valuelist)
	except IndexError:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
		
# Return The List Equally Spaced
def spacelist(list):
	output = ''
	space = ''
	output += str(list[0])
	space += ' '
	for listnum in range(1, len(list)):
		output += space
		output += str(list[listnum])
	return output

# List Or Count The Numbers Between Two Numbers
def numlistbetween(num1, num2, option='list', listoption='string'):
	if option == 'list':
		if listoption == 'string':
			output = ''
			output += str(num1)
			for currentnum in range(num1 + 1, num2 + 1):
				output += ','
				output += str(currentnum)
		elif listoption == 'list':
			output = []
			for currentnum in range(num1, num2 + 1):
				output.append(str(currentnum))
			return output
	elif option == 'count':
		return num2 - num1
	
# Align Text When Given Full Length
def textalign(text, maxlength, align='left'):
	spaces = ''
	if align == 'left':
		return text
	elif align == 'centre' or align == 'center':
		for i in range(int((maxlength - len(text)) / 2)):
			spaces += ' '
	elif align == 'right':
		for i in range(maxlength - len(text)):
			spaces += ' '
	return spaces + text
		
# Get The Time Since 00:00 On 1 January 1970
def timesince():
	from time import time as time_now
	return time_now()
	
# Fix The Formatting Of Decimals And Integers
def decintfix(decorint=0):
	if str(decorint)[-2:] == '.0':
		return int(decorint)
	else:
		return float(decorint)

# Get The Current Date Or Time
def getdatetime(timedateformat='complete'):
	from datetime import datetime
	timedateformat = timedateformat.lower()
	if timedateformat == 'day':
		return ((str(datetime.now())).split(' ')[0]).split('-')[2]
	elif timedateformat == 'month':
		return ((str(datetime.now())).split(' ')[0]).split('-')[1]
	elif timedateformat == 'year':
		return ((str(datetime.now())).split(' ')[0]).split('-')[0]
	elif timedateformat == 'hour':
		return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
	elif timedateformat == 'minute':
		return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1]
	elif timedateformat == 'second':
		return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2]
	elif timedateformat == 'millisecond':
		return (str(datetime.now())).split('.')[1]
	elif timedateformat == 'yearmonthday':
		return (str(datetime.now())).split(' ')[0]
	elif timedateformat == 'daymonthyear':
		return ((str(datetime.now())).split(' ')[0]).split('-')[2] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[1] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[0]
	elif timedateformat == 'hourminutesecond':
		return ((str(datetime.now())).split(' ')[1]).split('.')[0]
	elif timedateformat == 'secondminutehour':
		return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
	elif timedateformat == 'complete':
		return str(datetime.now())
	elif timedateformat == 'datetime':
		return (str(datetime.now())).split('.')[0]
	elif timedateformat == 'timedate':
		return ((str(datetime.now())).split('.')[0]).split(' ')[1] + ' ' + ((str(datetime.now())).split('.')[0]).split(' ')[0]	
	
# Get User input
def userinput(prompttext):
	try:
		return input(prompttext)
	except:
		return input(str(prompttext))
		
# Licence Information
def licence(raw=False):
	if raw == False:
		print('ROS Code Is Licenced Under The Apache License 2.0')
		print(u'\u2714' + ' Permissions: Commercial use, Modification, Distribution, Patent use And Private use')
		print(u'\u274c' + ' Limitations: Trademark use, Liability And Warranty')
		print(u'\u2139' + ' Conditions: License and copyright notice And State changes')
		print('To View The Full Licence, Go To: https://rosurl.ga/ROS-Code-Licence')
	else:
		print('ROS Code Is Licenced Under The Apache License 2.0')
		print('Permissions: Commercial use, Modification, Distribution, Patent use And Private use')
		print('Limitations: Trademark use, Liability And Warranty')
		print('Conditions: License and copyright notice And State changes')
		print('To View The Full Licence, Go To: https://rosurl.ga/ROS-Code-Licence')

print('Finished Loading ROS Code')

# End ROS Code
