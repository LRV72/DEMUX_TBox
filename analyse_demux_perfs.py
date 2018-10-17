from DEMUX_TBox.general_tools import get_conf, print_conf
from DEMUX_TBox.gbw import process_GBW
from DEMUX_TBox.dumps import process_dump, processIQ_multi
from DEMUX_TBox.energy_resol import meas_energy_r
import os

config=get_conf()
#dirname = '20181009_095800'
#dirname = '20181009_122600'
#dirname = '20181011_093000'
#dirname = '20181011_115900'
#dirname = '20181011_172100'
#dirname = '20181012_160900'
dirname = '20181017_091738'


fulldirname = os.path.join(config['path_tests'], dirname)

# -----------------------------------------------------------------------
# Processing "BIAS, FEEDBAC and INPUT" dump files 
process_dump(fulldirname, config, Max_duration=1.0)

# -----------------------------------------------------------------------
# Processing "Gain bandwidth characterization" 
chan=0
dumptype = "IQ-ALL"
process_GBW(fulldirname, dumptype, chan)
dumptype = "IQ-TST"
process_GBW(fulldirname, dumptype, chan)

# -----------------------------------------------------------------------
# Processing "Carriers spectra characterization"
pix=40 # test pixel
spt0dB = processIQ_multi(fulldirname, config, pix_zoom=pix, SR=False)

# -----------------------------------------------------------------------
# Processing "Energy resolution characterization"
meas_energy_r(fulldirname)