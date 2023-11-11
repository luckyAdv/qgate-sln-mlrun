import qgate.solution as qgate
import os.path
from qgate.uc.uc101 import UC101
from qgate.uc import ucsetup, ucoutput
import sys

def test():
    setup= ucsetup.UCSetup("0-size-100",
                         ["qgate-sln-mlrun-private.env", "qgate-sln-mlrun.env"])

    ucoutput.UCOutput(setup)
    aa=UC101(setup)
    aa.exec()

if __name__ == '__main__':

    args = sys.argv[1:]
    if args[0]=="test":
        # in-progress new solution with splitting scenarios based on use cases
        test()
    else:
        # old, stable solution
        sln = qgate.Solution("0-size-100",
                             ["qgate-sln-mlrun-private.env", "qgate-sln-mlrun.env"])
        try:
            sln.create(force=True)
        finally:
            sln.delete()
