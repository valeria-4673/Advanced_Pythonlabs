import abc

class BluePrintScan(abc.ABC):

    @abc.abstractmethod
    def scan_document(self):
        pass
    
class BluePrintPrinter(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass
    @abc.abstractmethod
    def get_printer_status(self):
        pass
    
class MFD1(BluePrintScan,BluePrintPrinter):
    
    def print_document(self):
        return("Document was printed MFD1")
    
    def scan_document(self):
        return("Document was scanned")
    
    def get_printer_status(self):
        print("Max print resolution is low, S/N: ", BluePrintScan.counter)

class MFD2(BluePrintScan,BluePrintPrinter):
    
    BluePrintScan.counter += 1
    
    def print_document(self):
        return("Document was printed ")
    
    def scan_document(self):
        return("Document was scanned")
    
    def get_printer_status(self):
        print("Max print resolution is medium, S/N: ", BluePrintScan.counter)

mfd1 = MFD1()
print(mfd1.print_document())
mfd1.get_printer_status()

mfd2 = MFD2()
print(mfd2.print_document())
mfd2.get_printer_status()
