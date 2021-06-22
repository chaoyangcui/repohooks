import os, sys

def main(**kwargs):
    #print("Execute prebuild_download", file=sys.stdout)
    #os.system("prebuild_download")
    print("Execute repo forall git lfs pull", file=sys.stdout)
    os.system("repo forall -c git lfs pull")