import os

def p_t(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        print(full_path)
        if os.path.isdir(full_path):
            p_t(full_path)

#print(o)
p_t("e:\\stg")