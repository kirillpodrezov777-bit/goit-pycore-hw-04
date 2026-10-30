
path = 'Data2.txt'

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file.readlines():
                id, name, age = line.strip().split(',')
                cat_info = {'id': '', 'name': '', 'age': ''}
                cat_info['id'] = id
                cat_info['name'] = str(name)
                try:
                    cat_info['age'] = int(age)
                except ValueError:
                    print("incorrect age")
                    cat_info['age'] = ''
                cat_info['age'] = str(age)
                cats_info.append(cat_info)
            return cats_info
    except FileNotFoundError:
        return "File not found"
print(get_cats_info(path))
