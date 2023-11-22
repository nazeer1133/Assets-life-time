
class Asset:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def calculate_depreciation(self, years):
        pass

class DepreciableAsset(Asset):
    def __init__(self, name, value, depreciation_rate):
        super().__init__(name, value)
        self.depreciation_rate = depreciation_rate

    def calculate_depreciation(self, years):
        depreciation = self.value * self.depreciation_rate * years
        return max(0, self.value - depreciation)

class NonDepreciableAsset(Asset):
    def calculate_depreciation(self, years):
        return self.value

# Example usage:
car = DepreciableAsset("Car", 30000, 0.1)
land = NonDepreciableAsset("Land", 50000)

print(f"Original value of {car.name}: ${car.value}")
print(f"Depreciated value of {car.name} after 5 years: ${car.calculate_depreciation(5)}")

print(f"Original value of {land.name}: ${land.value}")
print(f"Depreciated value of {land.name} after 5 years: ${land.calculate_depreciation(5)}")