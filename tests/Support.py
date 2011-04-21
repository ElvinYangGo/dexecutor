import os
import sys

parentPath = os.path.join(os.path.dirname(sys.argv[0]), os.pardir)
absoluteParentPath = os.path.abspath(parentPath)
sys.path.append(absoluteParentPath)
