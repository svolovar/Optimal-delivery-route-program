# Class for route optimization algorithms. Having a class for optimization algorithms allows for easy implementation
# of new algorithms in the future and allows each truck to deliver packages based on different algorithms depending
# on the company's preference

from ShippingData import ShippingData
import datetime


class RouteOptimizer:

    # Method to implement the nearest neighbor algorithm to sort a truck's packages
    # The complexity of this function is O(N) because there is a while loop that executes a block of code for each
    # package that needs to be sorted and this is the most complex part of the function
    @classmethod
    def nearest_neighbor(cls, truck, package_data, package_hashmap):
        # Make a list of the truck's packages that have not been delivered yet
        undelivered = []
        for package_ID in truck.package_list:
            # Look up the package with its ID number
            undelivered_package = package_hashmap.lookup_package(package_ID)

            # Add the returned package to the list
            undelivered.append(undelivered_package)

            # Update the package's departure time with the truck's departure time
            undelivered_package.package_departure_time = truck.truck_departure_time

            # Update the status to "en-route"
            undelivered_package.status.append("en-route")

        # Clear the truck's package list so it can be updated with the optimized list
        truck.package_list.clear()

        # Generate a list in optimal order based on the nearest neighbor algorithm and simulate the delivery of packages
        # given the truck's average speed
        # The time complexity of this while loop is O(N) which dictates the overall complexity of the nearest_neighbor
        # method
        while len(undelivered) > 0:
            closest_address = package_data.number_of_packages + 1
            next_package = None
            for package in undelivered:
                truck_address_num = ShippingData.get_address_number(package_data, truck.address)
                package_address_num = ShippingData.get_address_number(package_data, package.address)
                if ShippingData.find_distance(package_data, truck_address_num, package_address_num) <= closest_address:
                    closest_address = ShippingData.find_distance(package_data, truck_address_num, package_address_num)
                    next_package = package

            # Update the packages status to delivered
            next_package.status.append("delivered")

            # Remove the package from the undelivered list
            undelivered.remove(next_package)

            # Add the package to the trucks package list
            truck.package_list.append(next_package.package_ID)

            # Add the distance to the next address to the truck's mileage
            truck.mileage += closest_address

            # Update the truck's current address with the next package's address
            truck.address = next_package.address

            # Add the time it took to deliver the package given the trucks average speed of 18mph
            truck.tracking_time += datetime.timedelta(hours=closest_address / 18)

            # Update the package's delivery time with the time at which the truck arrived at the location
            next_package.delivery_time = truck.tracking_time
        return
