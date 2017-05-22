# Python 3.5.2 Ver.
# Unstructured Data Analysis @ School of Industrial Management Engineering, Korea University
# Written by Sunung Kim

import numpy as np
import csv
from xml.etree.ElementTree import Element, ElementTree, SubElement, dump, parse, tostring
import codecs
import glob
import re

data = list()
errorDat = list()
count = 0
gakha = list()
inyoung = list()
gigak = list()
nulllist = list()

gigak_text = list()
nongigak_text = list()

hun_type = list()
num = re.compile('[0-9]')
hangul = re.compile('[^ ㄱ-ㅣ가-힣|0-9]+')

csv_col_name = ["num", "orderr", "reason", "jgdmtNm", "enclsr", "xmlContent", "eventNum", "panreType", "eventNo",
            "eventCtgry", "inqDate", "eventNm", "lawEvent", "jgdmtCort", "content", "rstaDate", "rstaRsta",
            "apiRegDate", "apiChgDate"]

csv_dat = list()
csv_dat.append(csv_col_name)

for i in range(25273, 38964):     # 449~38964
    print(i)

    xmlTarget = codecs.open("D:/panre_data/text_data_panreType_01/%d.txt" % (i), "r", "utf-8")

    try:
        tree = parse(xmlTarget)

    except:
        errorDat.append(i)

    else:
        root = tree.getroot()
        temp = [""] * 19

        for element in root.findall("body"):

            for element2 in element.findall("items"):

                for element3 in element2.findall("item"):

                    if element3.findtext("content") == "":

                        temp[0] = "%d" % i

                        for j in range(1, len(csv_col_name)):

                            temp[j] = element3.findtext(csv_col_name[j])
                            temp[j] = hangul.sub(' ', temp[j])

                            if j == len(csv_col_name)-1:

                                csv_dat.append(temp)

        xmlTarget.close()


with codecs.open("panre_data_jihye_homework.csv", 'wb', "UTF-8") as csvfile:

    writer = csv.writer(csvfile)

    for line in csv_dat:

        writer.writerow(line)
