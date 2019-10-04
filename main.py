
import sys
import securejs
class mainClass:


	def __init__(self):
		print()

arguments = sys.argv

secjs = securejs.SecureJS()
secjs.exectueCommand(arguments[1])
