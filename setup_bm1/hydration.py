import BioSimSpace as BSS
import sys

lig1_name = sys.argv[1]
lig2_name = sys.argv[2]
device = sys.argv[3]
lig1_f_name = lig1_name+'/'+lig1_name
lig2_f_name = lig2_name+'/'+lig2_name

lig1 = BSS.IO.readMolecules([lig1_f_name+'.rst7',lig1_f_name+'.parm7'])[0]
lig2 = BSS.IO.readMolecules([lig2_f_name+'.rst7',lig2_f_name+'.parm7'])[0]

mapping = BSS.Align.matchAtoms(lig1, lig2)

#lig1_name = BSS.Align.rmsdAlign(lig1_name, lig2_name, mapping)

merged = BSS.Align.merge(lig1, lig2, mapping, allow_ring_breaking=True)

solvated = BSS.Solvent.tip3p(molecule=merged, box=3*[5*BSS.Units.Length.nanometer])

protocol = BSS.Protocol.FreeEnergy()
run_args = {'-c':'somd.rst7','-t':'somd.prm7', '-m': 'somd.pert', '-C': 'somd.cfg', '-p': 'CUDA'}
freenrg_somd = BSS.FreeEnergy.Solvation(solvated, protocol, engine="SOMD", work_dir=lig1_name+lig2_name)
freenrg_somd._update_run_args(run_args)

freenrg_somd.run()
freenrg_somd.analyse()

print("DONE!!! Let's have a beer!")
