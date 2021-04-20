file_path = "templates/"
file_name_postfix = ".html"
files = ["template"]
need_find = "\"img/"
need_find2 = "\"img/"
replace = "\"static/img/"
for file_name in files:
    new_file = ""
    with open(file_path + file_name + file_name_postfix, "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if need_find in line:
                line = line.replace(need_find, replace)
            new_file += line
    with open(file_path + file_name + file_name_postfix, "w" , encoding='utf-8') as file:
        file.writelines(new_file)


