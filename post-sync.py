import os, sys

def main(**kwargs):
    print("Execute prebuild_download", file=sys.stdout)
    os.system("./build/prebuilts_download.sh")
    print("Execute repo forall git lfs pull", file=sys.stdout)
    os.system("repo forall -c git lfs pull")