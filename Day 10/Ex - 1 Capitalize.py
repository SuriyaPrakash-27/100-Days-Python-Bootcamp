import string

def format_name(s):
    name_list = s.split(' ')

    f_name = name_list[0].capitalize()
    l_name = name_list[1].capitalize()

    return f"{f_name} {l_name}"

if __name__ == "__main__":
    s = input()

    print(format_name(s))


