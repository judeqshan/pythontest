


# from dist import src

with open('dist\\src.py', 'r') as file:
    obfuscated_code = file.read()

# Execute the obfuscated code
exec(obfuscated_code)

# Call the obfuscated function


# hello()