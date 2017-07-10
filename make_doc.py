#!/usr/bin/env python3

import os
import sys
import string
import subprocess

def main():
    documentationInputFile = "documentation_1_05.md"
    documentationPirit2fOutputFile = "documentation_pirit2f_1_05.md"
    documentationFm16OutputFile = "documentation_fm16_1_05.md"

    pirit2fStartLabel = "<<<<<< Pirit2f start >>>>>>"
    pirit2fEndLabel = "<<<<<< Pirit2f end >>>>>>"
    fm16StartLabel = "<<<<<< FM16 start >>>>>>"
    fm16EndLabel = "<<<<<< FM16 end >>>>>>"

    file_pirit2f = open(documentationPirit2fOutputFile, 'w', encoding='utf8')
    file_fm16 = open(documentationFm16OutputFile, 'w', encoding='utf8')

    with open(documentationInputFile, 'r', encoding="utf8") as file:
        pirit2fOnly = False
        fm16Only = False
        for line in file:
            if line.find(pirit2fStartLabel) != -1:
                pirit2fOnly = True
                fm16Only = False
                continue

            if line.find(pirit2fEndLabel) != -1:
                pirit2fOnly = False
                continue

            if line.find(fm16StartLabel) != -1:
                fm16Only = True
                pirit2fOnly = False
                continue

            if line.find(fm16EndLabel) != -1:
                fm16Only = False
                continue

            if fm16Only == False:
                file_pirit2f.write(line)
            if pirit2fOnly == False:
                file_fm16.write(line)

    file_pirit2f.close()
    file_fm16.close()
    proc = subprocess.Popen("python backdoc.py -t FM16 -s documentation_fm16_1_05.md > output/documentation_fm16_1_05.html", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()

    proc = subprocess.Popen("python backdoc.py -t Pirit2F -s documentation_pirit2f_1_05.md > output/documentation_pirit2f_1_05.html", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()

    proc = subprocess.Popen("rm documentation_pirit2f_1_05.md", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()

    proc = subprocess.Popen("rm documentation_fm16_1_05.md", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()

    print("Done")

if __name__ == '__main__':
    main()