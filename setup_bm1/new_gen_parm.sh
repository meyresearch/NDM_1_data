#!/bin/bash
echo "source leaprc.gaff"
echo "source leaprc.water.tip3p"
echo "loadamberparams $1.frcmod"
echo "test = loadmol2 $1_prep.mol2"
#echo "solvateoct test TIP3PBOX 12 iso 0.75"
echo "saveamberparm test $1.parm7 $1.rst7"
echo "quit"

