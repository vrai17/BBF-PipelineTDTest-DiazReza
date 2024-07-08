def string_appender(name, append_str):
    return "%s_%s" % (name, append_str)

if __name__ == '__main__':
    name_list = ["kenny", "hippo", "peter", "kelly", "john", "bob"]
    funcs = []
    for n in name_list:
        funcs.append(lambda _n = n: string_appender(_n, "char")) # _n captures value by reference n

    # Don’t modify the code below:
    for f in funcs:
        print(f())