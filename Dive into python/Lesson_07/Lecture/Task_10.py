"""Added file for demonstration"""
import shutil

shutil.rmtree('for_shutil/new_dir') # was removed with internal file
shutil.rmtree('for_shutil_1') # was removed only internal file, not current dir

