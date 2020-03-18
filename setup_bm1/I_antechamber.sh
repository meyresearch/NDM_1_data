#babel -ixyz ade-D-ala.xyz -opd ade-D-ala.pdb
cd $1
$AMBERHOME/bin/antechamber -at 2 -i $1.pdb -fi pdb -o $1_prep.mol2 -fo mol2 -c bcc -s 2 -nc -1
cd ..
