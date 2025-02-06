'''
A. ok
from pypack.pymod import pyfun 
pyfun()

B. ko
import pypack
pymod.pyfun()

C. ko
from pypack import *
pyfun()

D. ok
import pypack # Este import no hace nada, podríamos utilizar from pypack import *, junto con la declaración de la variable __all__ en el __init__ del package
import pypack.pymod
pypack.pymod.pyfun()

E. ok (Aparte, no está en el enunciado)
from pypack import * # Junto con la declaración de la variable __all__ en el __init__ del package
pymod.pyfun()
pymod2.pyfun2()
'''

if __name__=='__main__':
    from pypack.pymod import pyfun 
    pyfun()

