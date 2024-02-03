# classmethods Vs staticmethod

class Item(object):
    @staticmethod
    def isInteger(num):
        '''
        used to do something which is not unique per class instance/object
        but is somehow related to class
        '''

    @classmethod
    def instantiateFromCsv(cls):
        '''
        for instantiating instances using some external data source
        '''

# can be called from instances too, but usually not done in practice
i = Item()
i.instantiateFromCsv()
i.isInteger(5)