class ListInstance:
	"""
	Подмешиваемый класс, который предоставляет форматированную функцию
	print() или str () для экземпляров через наследование реализованного
	в нем метода __str__ ; отображает только атрибуты экземпляра; self
	является экземпляром самого нижнего класса;
	имена __ X предотвращают конфликты с атрибутами клиента
	"""

	def __attrnames(self):
		result = ""
		for attr in sorted(self.__dict__):
			result += "\t%s=%s\n" % (attr, self.__dict__[attr])
		return result

	def __str__(self):
		return "<Instanse of %s, address %s:\n%s>" % (
			self.__class__.__name__, # Имя класса
			id(self), # Адрес
			self.__attrnames() #  Список имя=значение
			)

class Spam(ListInstance):
	def __init__(self):
		self.data1 = "food"

x = Spam()
print(x)
y = Spam()
display = str(y)
print(display)
y.name = "Alex"
print(y) 
# При этом __repr__ выполняется обычно