#!/usr/bin/python3

import os
import sys
import string
import subprocess

def main():
    documentationInputFile = "documentation_pirit_fm.md"
    documentationPirit1fFd2OutputFile = "documentation_pirit1f_1_05.md"
    documentationPirit1fFd3OutputFile = "documentation_pirit1f_1_1.md"
    documentationPirit2fFd2OutputFile = "documentation_pirit2f_1_05.md"
    documentationFm16Fd2OutputFile = "documentation_fm16_1_05.md"
    documentationPirit2fFd3OutputFile = "documentation_pirit2f_1_1.md"
    documentationFm16Fd3OutputFile = "documentation_fm16_1_1.md"

    controlStringLabel = "<<<<<< " # control line starts with this string
    pirit1fFd2Label = "Pirit1f 1.05"
    pirit2fFd2Label = "Pirit2f 1.05"
    fm16Fd2Label = "FM16 1.05"
    pirit1fFd3Label = "Pirit1f 1.1"
    pirit2fFd3Label = "Pirit2f 1.1"
    fm16Fd3Label = "FM16 1.1"
    commonLabel = "common"

    file_p1Fd2 = open(documentationPirit1fFd2OutputFile, 'w', encoding='utf8')
    file_p1Fd3 = open(documentationPirit1fFd3OutputFile, 'w', encoding='utf8')
    file_p2Fd2 = open(documentationPirit2fFd2OutputFile, 'w', encoding='utf8')
    file_p2Fd3 = open(documentationPirit2fFd3OutputFile, 'w', encoding='utf8')
    file_fm16Fd2 = open(documentationFm16Fd2OutputFile, 'w', encoding='utf8')
    file_fm16Fd3 = open(documentationFm16Fd3OutputFile, 'w', encoding='utf8')


    with open(documentationInputFile, 'r', encoding="utf8") as file:
        p1Fd2 = True # Pirit1f 1.05
        p2Fd2 = True # Pirit2f 1.05
        fm16Fd2 = True # FM16 1.05
        p1Fd3 = True # same devices with 1.1
        p2Fd3 = True
        fm16Fd3 = True

        for line in file:
            if line[:7] == controlStringLabel: # control line found
                p1Fd2 = False # reset flags at control line
                p2Fd2 = False
                fm16Fd2 = False
                p1Fd3 = False
                p2Fd3 = False
                fm16Fd3 = False

                if line.find(pirit1fFd2Label) != -1:
                    p1Fd2 = True

                if line.find(pirit1fFd3Label) != -1:
                    p1Fd3 = True

                if line.find(pirit2fFd2Label) != -1:
                    p2Fd2 = True

                if line.find(pirit2fFd3Label) != -1:
                    p2Fd3 = True

                if line.find(fm16Fd2Label) != -1:
                    fm16Fd2 = True

                if line.find(fm16Fd3Label) != -1:
                    fm16Fd3 = True

                if line.find(commonLabel) != -1:
                    p1Fd2 = True # set all flags for common part
                    p2Fd2 = True
                    fm16Fd2 = True
                    p1Fd3 = True
                    p2Fd3 = True
                    fm16Fd3 = True

                continue

            if p1Fd2 == True:
                file_p1Fd2.write(line)

            if p1Fd3 == True:
                file_p1Fd3.write(line)

            if p2Fd2 == True:
                file_p2Fd2.write(line)

            if p2Fd3 == True:
                file_p2Fd3.write(line)

            if fm16Fd2 == True:
                file_fm16Fd2.write(line)

            if fm16Fd3 == True:
                file_fm16Fd3.write(line)

    file_p1Fd2.close()
    file_p1Fd3.close()
    file_p2Fd2.close()
    file_p2Fd3.close()
    file_fm16Fd2.close()
    file_fm16Fd3.close()

    # proc = subprocess.Popen("python backdoc.py -t Pirit1F -s documentation_pirit1f_1_05.md > output/documentation_pirit1f_1_05.html", shell=True, stdout=subprocess.PIPE)
    # out = proc.stdout.readlines()

    # proc = subprocess.Popen("python backdoc.py -t Pirit1F -s documentation_pirit1f_1_1.md > output/documentation_pirit1f_1_1.html", shell=True, stdout=subprocess.PIPE)
    # out = proc.stdout.readlines()

    proc = subprocess.Popen("python backdoc.py -t Pirit2F -s documentation_pirit2f_1_05.md > output/documentation_pirit2f_1_05.html", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()

    proc = subprocess.Popen("python backdoc.py -t Pirit2F -s documentation_pirit2f_1_1.md > output/documentation_pirit2f_1_1.html", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()

    proc = subprocess.Popen("python backdoc.py -t FM16 -s documentation_fm16_1_05.md > output/documentation_fm16_1_05.html", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()

    proc = subprocess.Popen("python backdoc.py -t FM16 -s documentation_fm16_1_1.md > output/documentation_fm16_1_1.html", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()

    # proc = subprocess.Popen("rm documentation_pirit1f_1_05.md", shell=True, stdout=subprocess.PIPE)
    # out = proc.stdout.readlines()

    # proc = subprocess.Popen("rm documentation_pirit1f_1_1.md", shell=True, stdout=subprocess.PIPE)
    # out = proc.stdout.readlines()

    # proc = subprocess.Popen("rm documentation_pirit2f_1_05.md", shell=True, stdout=subprocess.PIPE)
    # out = proc.stdout.readlines()

    # proc = subprocess.Popen("rm documentation_pirit2f_1_1.md", shell=True, stdout=subprocess.PIPE)
    # out = proc.stdout.readlines()

    # proc = subprocess.Popen("rm documentation_fm16_1_05.md", shell=True, stdout=subprocess.PIPE)
    # out = proc.stdout.readlines()

    # proc = subprocess.Popen("rm documentation_fm16_1_1.md", shell=True, stdout=subprocess.PIPE)
    # out = proc.stdout.readlines()

    os.remove(documentationPirit1fFd2OutputFile)
    os.remove(documentationPirit1fFd3OutputFile)
    os.remove(documentationPirit2fFd2OutputFile)
    os.remove(documentationFm16Fd2OutputFile)
    os.remove(documentationPirit2fFd3OutputFile)
    os.remove(documentationFm16Fd3OutputFile)
    print("Done")

if __name__ == '__main__':
    main()
