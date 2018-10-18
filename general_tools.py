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
    get_conf_csv()
    print_conf()

    """

# -----------------------------------------------------------------------
# Imports
import os, csv

# -----------------------------------------------------------------------
def get_conf_csv():
    r"""
        This function gets the configuration for the data processing of
        demux prototype files from a csv file.
        (path, ...).

        Returns
        -------
        config : dictionnary

        """

    config={}
    conffilename = "demux_tools_cfg.csv"

    if not os.path.exists(conffilename):
        print("Configuration file not found.")
        print("It is required to define the path.")
    else:
        with open(conffilename, newline='') as csvfile:
            conf_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in conf_reader:
                try:    # for numbers
                    config[row[0]]=float(row[1].replace(',','.'))
                except: # for strings
                    config[row[0]]=row[1].replace(',','.')

    return(config)

# -----------------------------------------------------------------------
def print_conf(config):
    r"""
        This function prints the parameters of a configuration set.
        (path, ...).

        Parameters
        ----------
        config: Dictionnary

        Returns
        -------
        Nothing

        """

    print('The configuration parameters are the following:')
    for key in config.keys():
        print(key, ': ', config[key])
    
    return()
# -----------------------------------------------------------------------