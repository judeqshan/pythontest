#import imp
import importlib

def test_import():
	module_name = "class_define"
	my_module = __import__(module_name)
	print("test_import imported module: ", my_module)
	print("test_import module: ", dir(my_module))
	
	class_name = "MyClass"
	class_ = getattr(my_module, class_name)
	print("test_import get class: ", class_)
	
	obj = class_()
	#for attr in dir(obj):
	print("test_import obj attr: ", dir(obj))
		
def test_import_class():
	module_name = "class_define"
	class_name = "MyClass"
	my_module = __import__(module_name, globals(), locals(), fromlist=[class_name])
	print("test_import_class imported module: ", my_module)
	print("test_import_class module: ", dir(my_module))
	
	
def test_importlib():
	module_name = "class_define"
	class_name = "MyClass"
	my_module = importlib.import_module(".", module_name)
	print("test_importlib imported module: ", my_module)
	print("test_importlib module: ", dir(my_module))
	
	importlib.reload(my_module)
	
def test_exec():
	lo = locals()
	module_name = "class_define"
	class_name = "MyClass"
	import_str = "import {}".format(module_name)
	
	my_module = exec(import_str)
	print("test_exec imported module: ", lo[module_name])
	print("test_exec module: ", dir(lo[module_name]))
	
	
	
if __name__ == "__main__":
	test_import()
	test_import_class()
	test_importlib()
	test_exec()
