#!/bin/bash
for n in lig_13 lig_14 lig_15 lig_16 lig_1 lig_2 lig_4 lig_5 lig_6 lig_7 lig_8 lig_9 lig_10 lig_11 lig_12
#for n in lig_16
do

bash I_antechamber.sh $n
bash II_parmchk2.sh $n
./new_gen_parm.sh $n > $n/in.leaprc
cd $n
/home/ppxasjsm/Software/amber18/bin/tleap -f in.leaprc
cd ..

done

