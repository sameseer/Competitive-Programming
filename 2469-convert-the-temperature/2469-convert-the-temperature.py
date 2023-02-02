class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        ans = []
        
        ans.append(kelvin)
        ans.append(fahrenheit)
        
        return ans