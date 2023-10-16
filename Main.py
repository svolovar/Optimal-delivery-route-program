# Author: Steven Volovar
# Student ID: 001511268
# Title: C950 Performance Assessment
import datetime
import Truck

from ShippingData import ShippingData
from RouteOptimizer import RouteOptimizer
from Package import Package
from builtins import ValueError

# Load data for program from CSV files
# The complexity of this code is O(N)
WGUPS_data = ShippingData("CSV_files/package_data.csv", "CSV_files/address_data.csv", "CSV_files/distance_table.csv")

# Create a hash table to store the package information with a time parameter to indicate the time at which the packages
# arrived in the hub
# The complexity of this code is O(N)
WGUPS_package_hashmap = WGUPS_data.import_packages(datetime.timedelta(hours=8))

# Create truck objects
# The complexity of these three lines of code is O(1)
truck1 = Truck.Truck(16, 18, [], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truck2 = Truck.Truck(16, 18, [], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truck3 = Truck.Truck(16, 18, [], 0.0, "4001 South 700 East", datetime.timedelta(hours=10))

# Create RouteOptimizer
# The complexity of this code is O(1)
optimal_route = RouteOptimizer()

# Load the trucks with respect to the special notes
# The complexity of these three lines of code is O(N)
truck1.package_list = [5, 10, 17, 21, 24, 26, 27, 37, 13, 14, 15, 16, 19, 29, 31, 34]
truck2.package_list = [3, 6, 25, 28, 32, 36, 38, 2, 7, 11, 18, 22, 30, 33, 35, 40]
truck3.package_list = [9, 4, 8, 12, 20, 23, 39, 1]

# Optimize route for truck1 using the nearest neighbor method
# The complexity of this code is O(N)
optimal_route.nearest_neighbor(truck1, WGUPS_data, WGUPS_package_hashmap)

# Optimize route for truck2 using the nearest neighbor method
# The complexity of this code is O(N)
optimal_route.nearest_neighbor(truck2, WGUPS_data, WGUPS_package_hashmap)

# Ensure truck 3 can only leave when trucks 1 and 2 get back because there are only two drivers and to account for the
# possibility of an address update
# The complexity of this code is O(1)
truck3.truck_departure_time = min(truck1.tracking_time, truck2.tracking_time, datetime.timedelta(hours=10, minutes=20))

# Update address for package 9 on truck 3
# Create updated package
# The complexity of this code is O(1)
updatedPackage = Package(9, "410 S State St", "Salt Lake City", "UT", 84103, "EOD", 2, "undelivered")
updatedPackage.load_time = datetime.timedelta(hours=8)

# Update package 9
# The complexity of this code is O(1)
WGUPS_package_hashmap.add_package(9, updatedPackage)

# Optimize route for truck3 using nearest neighbor algorithm
# The complexity of this code is O(N)
optimal_route.nearest_neighbor(truck3, WGUPS_data, WGUPS_package_hashmap)


class Main:
    # User interface for the program
    # Show the day's route mileage and present the user with an interface to check the status of packages
    # The complexity of this code is O(1)
    print("............................................")
    print("Welcome to the package program")
    print("............................................")
    print("")

    # Show the day's route mileage and present the user with an interface to check the status of packages
    # The complexity of this code is O(1)
    print(".........Today's Route mileage..............")
    print("(Displayed to first two decimal places)")
    # Show the mileage for each truck limited to two decimal places
    print("Truck 1: " + str('%.2f' % truck1.mileage))
    print("Truck 2: " + str('%.2f' % truck2.mileage))
    print("Truck 3: " + str('%.2f' % truck3.mileage))
    # Add the mileage for all 3 trucks to get to total route mileage
    total_miles = truck1.mileage + truck2.mileage + truck3.mileage
    print("Total mileage: " + str('%.2f' % total_miles))
    print("............................................")
    print("")

    # Present the user with options for checking the status of packages
    # The complexity of this code is O(1)
    print("USER OPTIONS")
    print("t  -  Lookup up status of package or packages at a certain time")
    print("p  -  Lookup up specific package's tracking information at EOD")
    print("m  -  Show total mileage traveled by all trucks")
    print("Enter an option or enter 'x' to exit")
    user_input = input("Input > ")

    # Exit the program if user chooses 'x' option
    # The complexity of this code is O(1)
    if user_input == "x":
        exit()

    # If user enters "t"
    if user_input == "t":
        try:
            print("Enter a time in HH:MM:SS format")
            input_time = input("Input > ")
            (hours, mins, secs) = input_time.split(":")
            time_conversion = datetime.timedelta(hours=int(hours), minutes=int(mins), seconds=int(secs))
            print("To view a specific package at this time, enter the package ID number, otherwise, enter 'a'")
            input_two = input("Input > ")
            if input_two == "a":
                # The complexity of this code is O(N)
                WGUPS_data.status_of_packages(WGUPS_package_hashmap, time_conversion)
            elif int(input_two) > 0:
                # The complexity of this code is O(1)
                package_individual = WGUPS_package_hashmap.lookup_package(int(input_two))
                print("...............................................")
                package_individual.show_tracking_info(time_conversion)
                print(".......................")
                print("Package number " + str(input_two) + " info and EOD status:")
                print(str(package_individual))
                print("...............................................")
                print("")
        except ValueError:
            print("Invalid entry, program exiting")

    if user_input == "p":
        try:
            print("Enter a package ID number")

            # The complexity of this code is O(1) (average)
            lookup_id = input("Input > ")
            package_p = WGUPS_package_hashmap.lookup_package(int(lookup_id))
            print("...............................................")
            print("Information and EOD status for package number " + str(lookup_id))
            print(str(package_p))
            print(".......................")
            package_p.show_tracking_info("EOD")
            print("...............................................")
        except ValueError:
            print("Invalid entry, program exiting")

    if user_input == "m":
        # The complexity of this code is O(1)
        print("...............Route mileage............... ")
        print("Truck 1: " + str('%.2f' % truck1.mileage))
        print("Truck 2: " + str('%.2f' % truck2.mileage))
        print("Truck 3: " + str('%.2f' % truck3.mileage))
        total_miles = truck1.mileage + truck2.mileage + truck3.mileage
        print("Total mileage: " + str('%.2f' % total_miles))
        print("............................................")
