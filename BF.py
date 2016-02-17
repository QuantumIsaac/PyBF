import sys

MAX_OUT = 100

class BF:
	cells = [0]
	tokens = []
	pointer = 0
	def __init__( self, tokens ):
		for i in tokens:
			self.tokens.append( i )  #Initialize program data
	def execute( self ):
		i = 0
		counter = 0
		did_jump = False
		while i < len(self.tokens):
			if counter >= MAX_OUT:
				break
			counter += 1
			if not did_jump:
				i += 1
			else:
				did_jump = False
			tok = self.tokens[i]
			print i
			if tok=='>':
				self.pointer += 1
				if len(self.cells) >= self.pointer:
					self.cells.append(0)
			elif tok=='<':
				if self.pointer<=0:
					sys.stderr.write("bf error: Cannot set pointer below 0")
					sys.exit(1)
				else:
					self.pointer -= 1
			elif tok=='+':
				self.cells[self.pointer] += 1
			elif tok=='-':
				self.cells[self.pointer] -= 1
			elif tok==',':
				value = sys.stdin.read(1)
				value = ord(sys.stdin.read(1))
				self.cells[self.pointer] = value
			elif tok=='.':
				value = chr(self.cells[self.pointer])
				print value
				sys.stdout.write(value)
			elif tok=='[':
				value = self.cells[self.pointer]
				found = False
				do_break = False
				if( value == 0 ):
					for j in xrange(i,len(self.tokens)):
						if(self.tokens[j] == ']'):
							i = j
							found = True
							if i >= len(self.tokens):
								do_break = True
							did_jump = True
							break
					if not found:
						#If we've reached this point, the user did not specify a closing ]!
						print "bf error: Could not find a closing ] to match [!"
						sys.exit(1)
					else:
						if do_break:
							break
						else:
							continue
			elif tok==']':
				value = self.cells[self.pointer]
				found = False
				print "Value == 0: " + str(value == 0)
				if value != 0 :
					for j in xrange(i,0,-1):
						if( self.tokens[j] == '['):
							i = j
							found = True
							did_jump = True
							break
					if not found:
						sys.stderr.write("bf error: Could not find opening [ to match ]!");
						sys.exit(1)
					else:
						continue
			else:
				continue #Ignore other characters.

def tokenize(c):
	toks = []
	for tok in c:
		if tok == "<" or tok == ">" or tok=="+" or tok=="-" or tok=="," or tok=="." or tok=="[" or tok=="]":
			toks.append(tok)
	return toks

if __name__ == '__main__':
	if len(sys.argv) > 1:
		f = sys.argv[1]
		o = open(f, 'r')
		c = o.read()
		bf = BF(tokenize(c))
		bf.execute()
	else:
		print "bf error: no input file! exiting."
				
