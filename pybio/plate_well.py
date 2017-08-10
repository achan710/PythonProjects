'''
Created on Aug 9, 2017

@author: allanchan
'''
import string


class PlateWell(object):
    
    ROWS = string.ascii_uppercase
    
    def __init__(self, nrows, nwells):
        self.nrows = nrows
        self.nwells = nwells
        self.totalwells = nrows * nwells

    def display(self):
        print (self.nrows, self.nwells)
        
    def decode_to_list(self, bits):
        plate_rows = []
        idx = 0     #index for bits
        
        if len(bits) is not self.totalwells:
            raise ValueError
        
        while (idx < self.totalwells):
            plate_wells = []
            for well in range(self.nwells):
                plate_wells.append(bits[idx])
                idx = idx + 1
            plate_rows.append(plate_wells)
                
        return plate_rows
    
    def display_as_list(self, bits):
        mapping = self.decode_to_list(bits)
        for row in mapping:
            print (row)

class PlateWell96(PlateWell):
    
    def __init__(self, nrows=3, nwells=4):
        super(PlateWell96, self).__init__(nrows, nwells)
        

        
        

if __name__ == '__main__':
    pw = PlateWell96()
    bits = '011101110111'
    pw.display_as_list(bits)
    