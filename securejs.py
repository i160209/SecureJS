
class AppGUI:

	def displayGUI(self):
		import webbrowser,os
		webbrowser.open('file://'+os.path.realpath('SECUREJS/index.html')) 
		print("AppGUI.displayGUI() executed")
		
class Documentation:

	def displayhelp(self):
		print("Documentation.displayhelp() executed")

class Model:

	def buildModel(self):
		print("Model.buildModel() executed")
		
class Dataset:

	def displayDataMetrics(self):
		print("Dataset.displayDataMetrics() executed")	
		
		
		
		
		
		
class SecureJS:

	def exectueCommand(self,command):
		if(command=="-help"):
			print("\ndisplayhelp() function from Documentation Will be executed :")
			doc = Documentation()

			doc.displayhelp()
			
		if(command=="-options"):
			print()
			print(" -help 		: Get help about usage of tool")
			print(" -dataset 	: Get help about usage of tool")
			print(" -buildModel  	: Build model on the data")
			print(" -displayGUI    : Display Application GUI")
		if(command=="-dataset"):
			print("\ndisplayDataMetric() function from Dataset Will be executed :")
			Data = Dataset()
			Data.displayDataMetrics()
		if(command=="-buildModel"):
			print("\nbuildModel() function from Model Will be executed :")
			modl = Model()

			modl.buildModel()
		if(command=="-displayGUI"):
			appgui = AppGUI()
			print("\nbuildModel() function from Model Will be executed :")
			appgui.displayGUI()



