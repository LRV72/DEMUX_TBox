# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------
"""
    General_tools module
    ====================

    Developped by: L. Ravera

    Project: Athena X-IFU / DRE-DEMUX

    General purpose tools needed for the DRE data processing

    Routine listing
    ===============
    get_conf()
    """

# -----------------------------------------------------------------------
# Imports
import os


# -----------------------------------------------------------------------
def get_conf(local=True):
    r"""
        This function gets the configuration for the data processing
        (path, ...).

        Parameters
        ----------
        local : boolean
        If True, the data are located locally on the computer
        If False, the data are processed remotely on the GSE
        (default is True)

        Returns
        -------
        conf : dictionnary

        """

    config={\
        'path_tests': '', \
        'dir_data': 'data', \
        'dir_hk': 'hk', \
        'dir_plots': 'plots', \
        'dir_logs': 'logs', \
        'ScBandMin': 20., \
        'ScBandMax': 600., \
        'SNR_pix': -131.4, \
        'DRD': -166, \
        'Cf': 4.5 }


    conffilename = "demux_tools.config"
    
    if not os.path.exists(conffilename):
        print("Configuration file not found.")
        print("It is required to define the path.")
    else:
        print("Loading project path from file ", conffilename)
        conffile = open(conffilename, 'r')
        line = conffile.readline().split(' ')
        config['path_tests'] = line[1][:-1]
        line = conffile.readline().split(' ')
        config['dir_data'] = line[1][:-1]
        line = conffile.readline().split(' ')
        config['dir_hk'] = line[1][:-1]
        line = conffile.readline().split(' ')
        config['dir_plots'] = line[1][:-1]
        line = conffile.readline().split(' ')
        config['dir_logs'] = line[1][:-1]
        line = conffile.readline().split(' ')
        config['ScBandMin'] = float(line[1][:-1])
        line = conffile.readline().split(' ')
        config['ScBandMax'] = float(line[1][:-1])
        line = conffile.readline().split(' ')
        config['SNR_pix'] = float(line[1][:-1])
        line = conffile.readline().split(' ')
        config['DRD'] = float(line[1][:-1])
        line = conffile.readline().split(' ')
        config['Cf'] = float(line[1][:-1])
        conffile.close()
        
        return(config)


# -----------------------------------------------------------------------
def print_conf(config):
    r"""
        This function prints the parameters of a configuration set.
        (path, ...).

        Parameters
        ----------
        Config: Dictionnary

        Returns
        -------
        Nothing

        """

    print('The configuration parameters are the following:')
    for key in config.keys():
        print(key, ': ', config[key])
    
    return()

# -----------------------------------------------------------------------