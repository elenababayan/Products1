

with open('shopping_list') as f:
    content = f.readlines()

content = [x.strip() for x in content]