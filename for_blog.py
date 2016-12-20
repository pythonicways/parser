import re
import time
from time import strftime

def main():
    log_file_path = r"C:\ios logs\sfbios.log"
    export_file_path = r"C:\ios logs\filtered"

    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

    file = "\\" + "Parser Output " + time_now + ".txt"
    export_file = export_file_path + file

    regex = '(<property name="(.*?)">(.*?)<\/property>)'

    parseData(log_file_path, export_file, regex, read_line=True, reparse=True)


def parseData(log_file_path, export_file, regex, read_line=True, reparse=False):
    with open(log_file_path, "r") as file:
        match_list = []
        if read_line == True:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
        else:
            data = file.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group();
                match_list.append(match_text)
    file.close()

    if reparse == True:
        match_list = reparseData(match_list, '(property name="(.{1,50})">(Enabled)<\/property>)')

    with open(export_file, "w+") as file:
        file.write("EXPORTED DATA:\n")
        match_list_clean = list(set(match_list))
        for item in xrange(0, len(match_list_clean)):
            print match_list_clean[item]
            file.write(match_list_clean[item] + "\n")
    file.close()
    return match_list_clean

def reparseData(parsed_data, regex):
    data_string = ''.join(parsed_data)
    match_list = [];
    for match in re.finditer(regex, data_string, re.S):
        match_text = match.group();
        match_list.append(match_text)
    return match_list

if __name__ == '__main__':
    main()

