"""
Setup script to install the MiniDrugBank molecule set as a python package
"""

import sys,os
from os.path import relpath, join
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_package_data(data_root, package_root):
    files = []
    for root, dirnames, filenames in os.walk(data_root):
        for fn in filenames:
            files.append(relpath(join(root, fn), package_root))
    return files

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

descr = """
This provides the molecule set MiniDrugBank and the jupyter notebook used to create it. This set was generated by the Open Force Field to test chemical perception sampling tools. This set is provided with parm@frosst and tripos atom types. The goal is to include any parm@frosst atom types and smirnoff99Frosst parameters found in the complete DrugBank set.
"""

setup(
    name                 = 'minidrugbank',
    version              = '0.0.0',
    description          = 'MiniDrugBank molecule set',
    long_description     = descr,
    url                  = 'https://github.com/openforcefield/MiniDrugBank',
    author               = 'Caitlin C. Bannan, David L. Mobley',
    author_email         = 'dmobley@uci.edu',
    license              = 'MIT',
    platforms            = ['Linux-64', 'Mac OSX-64', 'Unix-64'],
    packages             = ['minidrugbank/tests/'],
    package_data = {'minidrugbank': find_package_data('minidrugbank/', 'minidrugbank')},
    include_package_data = True
)
