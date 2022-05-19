from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# setting calc size

Window.size = (500,700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'

	# Making a button

	def button_press(self, button):
		prior = self.ids.calc_input.text
		
		# error handling

		if "Error" in prior:
			prior = ''
		if prior == "0":
				self.ids.calc_input.text = ''
				self.ids.calc_input.text = f'{button}'
		else: 
			self.ids.calc_input.text = f'{prior}{button}'

	# backspace func

	def remove(self):
		prior = self.ids.calc_input.text
		prior = prior[:-1]
		self.ids.calc_input.text = prior
	
	def pos_neg(self):
		prior = self.ids.calc_input.text
		if "-" in prior:
			self.ids.calc_input.text = f'{prior.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{prior}'

	# decimals func

	def dot(self):
		prior = self.ids.calc_input.text
		num_list = prior.split("+")
		if "+" in prior and "." not in num_list[-1]:
			prior = f'{prior}.'
			self.ids.calc_input.text = prior

		elif "." in prior:
			pass
		else:
			prior = f'{prior}.'
			self.ids.calc_input.text = prior

	# add func
	def math_sign(self, sign):
		prior = self.ids.calc_input.text
		self.ids.calc_input.text = f'{prior}{sign}'

	
	# equal func
	def equals(self):
		prior = self.ids.calc_input.text
		 # Error Handling
		try:
			answer = eval(prior)
			self.ids.calc_input.text = str(answer)
		except:
			self.ids.calc_input.text = "Error"

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()

