__author__ = 'SuturkinAA'

import configparser

class Config:

    #defaults settings
    restPort = 8000
    resourcesMax = 3

    def save(self):
        config = configparser.ConfigParser()
        config['general'] = {'RestPort': self.restPort,
                            'ResourcesCount': self.resourcesMax}
        with open('resm.cfg', 'w') as configfile:
            config.write(configfile)

    def load(self):
        config = configparser.ConfigParser()
        config.read('resm.cfg')
        preferences = config['general']
        self.restPort = int(preferences['RestPort'])
        self.resourcesMax = int(preferences['ResourcesCount'])