# -*- coding: utf-8 -*-
import os
import re
import sys

from res import Res

# section in res_names.txt
# ...
# anim.close_enter_left_to_right, anim.eui_support_close_enter_left_to_right
# anim.close_exit_left_to_right, anim.eui_support_close_exit_left_to_right
# ...
#
# -- Your should modify RES_NAMES_FILE value
gRES_NAMES_FILE = r"C:\Users\thomas.XancL-NB\Desktop\EUI-Support-Demos\EuiSupport\res_names.txt"
gRES_NAME_LIST = []

gCLIENT_FILE_LIST = []

# resource name dictionary
# old and new name
gRES_NAME_DICT = {}
gFILE_NAME_DICT = {}


def parse_res_names(res_names_file):
    with open(res_names_file) as in_file:
        for line in in_file:
            line = line.rstrip()
            name_pair = line.split(", ")
            old_name = name_pair[0]
            new_name = name_pair[1]

            gRES_NAME_LIST.append(old_name)
            gRES_NAME_DICT[old_name] = new_name

    # print len(name_dict)
    for key in gRES_NAME_DICT:
        print "%s, %s" % (key, gRES_NAME_DICT[key])

    name_list = []
    for value in gRES_NAME_DICT.values():
        if value not in name_list:
            name_list.append(value)
        else:
            print "[warn] resource name: " + value

    pass


# -- You should modify the CLIENT_DIR value
CLIENT_DIR = r"C:\Users\thomas.XancL-NB\Desktop\EUI-Support-Demos\open-apidemo\src\main"


def parse_line(old_res, line):
    src_pattern = r'(@[\+]?)%s/%s' % (old_res._type, old_res._name)
    p = re.compile(src_pattern)
    print line
    m = re.match(p, line)
    print re.sub(p, r'\1%s/%s' % (old_res._type, "es_" + old_res._name), line)

    return m


def rename_res_names():
    for src_file in gCLIENT_FILE_LIST:
        print 'process: ' + src_file
        tmp_file = src_file + '.tmp'
        os.rename(src_file, tmp_file)
        with open(src_file, 'w') as out_file:
            with open(tmp_file) as in_file:
                for line in in_file:
                    new_line = line

                    old_res = Res("", "")
                    new_res = Res("", "")

                    if src_file.endswith('.xml'):
                        for res_name in gRES_NAME_LIST:
                            old_res.from_text(res_name)
                            new_res.from_text(gRES_NAME_DICT[res_name])

                            # definition
                            src_pattern = 'name="%s"' % old_res._name
                            dst_pattern = 'name="%s"' % new_res._name
                            if line.find(src_pattern) >= 0:
                                new_line = line.replace(src_pattern, dst_pattern)

                            # reference
                            if line.find("/%s" % old_res._name) >= 0:
                                src_pattern = r'(@[\+\*]?)%s/%s' % (old_res._type, old_res._name)
                                p = re.compile(src_pattern)
                                new_line = re.sub(p, r'\1%s/%s' % (new_res._type, new_res._name), line)
                                line = new_line
                    else:
                        for res_name in gRES_NAME_LIST:
                            old_res.from_text(res_name)
                            new_res.from_text(gRES_NAME_DICT[res_name])

                            # reference
                            src_pattern = 'R.%s.%s' % (old_res._type, old_res._name)
                            dst_pattern = 'R.%s.%s' % (new_res._type, new_res._name)
                            if line.find(src_pattern) >= 0:
                                new_line = line.replace(src_pattern, dst_pattern)
                                line = new_line

                    out_file.write(new_line)
            os.remove(tmp_file)
    pass


def main(argv):
    if len(argv) < 2:
        print 'usage: res_name_parser.py $res_name.txt $client_dir'
        exit(1)

    res_names_file = gRES_NAMES_FILE
    client_dir = CLIENT_DIR

    res_names_file = argv[0]
    client_dir = argv[1]

    parse_res_names(res_names_file)
    # if os._exists(client_dir):
    walk(client_dir)

    # rename files
    for path in gFILE_NAME_DICT:
        print 'mv %s -> %s' % (path, gFILE_NAME_DICT[path])
        os.rename(path, gFILE_NAME_DICT[path])

    # rename resource name in client files
    rename_res_names()
    pass


def is_file_res(path):
    # resource
    # - file resource
    # - xml resource
    folder_list = ['anim', 'color', 'drawable', 'layout']
    for folder in folder_list:
        if path.find(folder):
            return True
    return False


def walk(root_dir):
    for my_dir in os.listdir(root_dir):
        path = os.path.join(root_dir, my_dir)
        if os.path.isfile(path):

            if is_file_res(path):
                # the file need to rename
                print "file resource: " + path

                for res_name in gRES_NAME_LIST:
                    old_res = Res("", "")
                    old_res.from_text(res_name)

                    new_res = Res("", "")
                    new_res.from_text(gRES_NAME_DICT[res_name])

                    if my_dir.find(old_res._name) == 0:
                        print "matched: %s, %s" % (res_name, my_dir)
                        new_path = path.replace(old_res._name, new_res._name)
                        gFILE_NAME_DICT[path] = new_path

                        break
                    pass

            if path.endswith('.java') or path.endswith('.xml'):
                # source file need to parse and replace
                print "client: " + path
                if gFILE_NAME_DICT.has_key(path):
                    gCLIENT_FILE_LIST.append(gFILE_NAME_DICT[path])
                else:
                    gCLIENT_FILE_LIST.append(path)

        if os.path.isdir(path):
            walk(path)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
