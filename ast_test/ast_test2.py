import ast
import astor

# Define a Python function as a string
python_code = """
def add(a, b):
    return a + b

result = add(10, 20)
"""

# Parse the Python code into an Abstract Syntax Tree (AST)
tree = ast.parse(python_code)

# Define a visitor to modify the AST by adding print statements to function calls
class AddPrintVisitor(ast.NodeTransformer):
    def visit_Call(self, node):
        print_node = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Str(s='Calling function:', ctx=ast.Load()), node], keywords=[]))
        return [print_node, node]

# Apply the visitor to the AST
modified_tree = AddPrintVisitor().visit(tree)

# Convert the modified AST back to Python code
modified_code = astor.to_source(modified_tree)
print(modified_code)