# Create class for trucks

class Truck:
    def __init__(self, package_capacity, speed, package_list, mileage, address, truck_departure_time):
        self.package_capacity = package_capacity
        self.speed = speed
        self.package_list = package_list
        self.mileage = mileage
        self.address = address
        self.truck_departure_time = truck_departure_time
        self.tracking_time = truck_departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.package_capacity, self.speed, self.package_list, self.mileage,
                                           self.address, self.truck_departure_time)
