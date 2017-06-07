#!/usr/bin/env python3

import sys
import os
import os.path as osp
import subprocess as sub

sizes = [48, 64, 160, 256, 512, 1024, 1536]

usageMsg = """\
Usage : convert.py file1 [file2 ...]

Input : High resolution SQUARE images. Tested on jpg and png files.
Output: Corresponding jpg and png files of the following sizes,
        {sizes}

"""
usageMsg = usageMsg.format(sizes=sizes)

errMsg1 = "convert.py Err: Only files with extentinos allowed '{}'"

cmd = "convert -thumbnail {size} {filename} {newfilename}"

def convert(filename, extention):
    if not extention:
        print(errMsg1.format(filename), file=sys.err)
        return

    newfilename = osp.splitext(filename)[0]

    for size in sizes:
        currcmd = cmd.format(size=size, filename=filename, newfilename=(newfilename + "-" + str(size) + extention))

        print(currcmd)
        sub.run(currcmd, shell=True)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(usageMsg)
        exit(1)

    filenames = sys.argv[1:]
    extentions = [osp.splitext(filename)[1] for filename in filenames]

    for i, filename in enumerate(filenames):
        convert(filename, extentions[i])


