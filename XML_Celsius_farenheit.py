import xml.etree.ElementTree as ET

class TemperatureConverter():
    
    def __init__(self, celsius):
        self.celsius = celsius
        
    def convert_celsius_to_fahrenheit(self):
        faren = 9/5 *(self.celsius) +32
        round(faren, 1)
        return faren
        
class ForecastXmlParser():
    tree = ET.parse('forecast.xml')
    root = tree.getroot()
    
    faren_list = []
    celsius_list = []
    
    for temp in root.iter('temperature_in_celsius'):
        
        celsius = int(temp.text)
        celsius_list.append(celsius)
        
        faren = TemperatureConverter(celsius).convert_celsius_to_fahrenheit()
        faren_list.append(faren)
        
    days_list = []     
    for day in root.iter('day'):
        day = day.text
        days_list.append(day)
    
    for i, value in enumerate(root):
        print('Day:{}, Celsius:{} , Faren:{} '.format(days_list[i], 
        celsius_list[i], faren_list[i]))
