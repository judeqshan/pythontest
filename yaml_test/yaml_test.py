import yaml
with open("D:\workspace\workspace\pythontest\pythontest\yaml_test\yaml_test.yaml", 'r') as file:
    data = yaml.safe_load(file)

print(data['test_info'])
print(data['test_info']["description2"])
print(data['test_info']["description"])