#!/usr/bin/python3

import os
import sys
import string
import subprocess
import backdoc


def html(name):
    return "output/documentation_" + name + ".html"


def md(name):
    return "documentation_" + name + ".md"


def write(type, name):
    out = open(html(name), 'w', encoding='utf8')
    backdoc.BackDoc(markdown_converter=backdoc.Markdown(extras=['toc', 'tables']),
                    template_html=backdoc.template_html,
                    stdin=sys.stdin,
                    stdout=out
                    ).run(argv=["-t", type, "-s", md(name)])
    out.close()


def dictSet(dict, bool):
    for key in dict:
        dict[key][3] = bool

def main():
    documentationInputFile = "documentation_pirit_fm.md"
    controlStringLabel = "<<<<<< "  # control line starts with this string
    commonLabel = "common"

    dict = {"Pirit2f 1.05": ["Pirit2F", "pirit2f_1_05", None, False],
            "Pirit2f 1.2": ["Pirit2F", "pirit2f_1_2", None, False],
            "Punix": ["Punix", "punix", None, False],
            "FM16 1.05": ["FM16", "fm16_1_05", None, False],
            "FM16 1.2": ["FM16", "fm16_1_2", None, False],
            commonLabel: [None, None, None, False]}

    for key in dict.keys():
        if dict[key][1]:
            dict[key][2] = open(md(dict[key][1]), 'w', encoding='utf8')


    with open(documentationInputFile, 'r', encoding="utf8") as file:

        for line in file:
            if line[:7] == controlStringLabel:  # control line found
                dictSet(dict, False)

                for key in dict:
                    dict[key][3] = key in line
                continue

            commonTitle, commonName, commonFile, commonStatus = dict[commonLabel]
            for title, name, file, status in dict.values():
                if (commonStatus or status) and file:
                    file.write(line)

    for title, name, file, status in dict.values():
        if file:
            file.close()
            write(title, name)
            os.remove(md(name))
    print("Done")


if __name__ == '__main__':
    main()
