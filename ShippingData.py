# Create class for taking in the CSV data and loading it into the proper data structures for the program

import csv
from Package import Package
from PackageTable import MakePackageTable


class ShippingData:
    def __init__(self, path_to_package_csv, path_to_address_csv, path_to_distance_csv):
        self.path_to_package_csv = path_to_package_csv
        self.path_to_address_csv = path_to_address_csv
        self.path_to_distance_csv = path_to_distance_csv
        self.number_of_packages = 0

    # Method for converting CSV data into package objects and adding them into hash table
    # The complexity of this function is O(N) because the for loop executes the same amount of code for each package
    # in the CSV file
    def import_packages(self, load_time):

        # Create a hashmap to store the packages and add each package
        package_table = MakePackageTable()

        # Open the package csv file and add the data from each column as the packages respective attributes
        with open(self.path_to_package_csv) as packageDetails:
            package_attributes = csv.reader(packageDetails)
            for package in package_attributes:
                package_id = int(package[0])
                package_address = package[1]
                package_city = package[2]
                package_state = package[3]
                package_zip = package[4]
                package_deadline = package[5]
                package_weight = package[6]
                package_status = None

                # Create package object with attributes each column in the row
                added_package = Package(package_id, package_address, package_city, package_state, package_zip,
                                        package_deadline, package_weight, package_status)

                # Update the package's status to "in hub"
                added_package.status.append("in hub")

                # Update the time at which the package arrived in the hub
                added_package.load_time = load_time

                # Add the package to the package table
                package_table.add_package(package_id, added_package)

                # Update the number of packages that arrived in the hub
                self.number_of_packages += 1
        return package_table

    # Method to get address number
    # The complexity of this function is O(N) because the for loop executes the same amount of code for each package
    # in the CSV file
    def get_address_number(self, address):
        # Open the address csv and assign row 0 as the address number

        with open(self.path_to_address_csv) as csvfile:
            csv_address_data = csv.reader(csvfile)
            csv_address_data = list(csv_address_data)
            for row in csv_address_data:
                if address in row[2]:
                    return int(row[0])

    # Method to find distance between two addresses
    # The complexity of this function is O(1) because the most complex operation executed is the assignment of the
    # distance variable
    def find_distance(self, x_value, y_value):
        # Open the distance table and use two address numbers as x_value and y_value
        # to find the distance between two addresses
        with open(self.path_to_distance_csv) as csvfile:
            csv_distance_table = csv.reader(csvfile)
            csv_distance_table = list(csv_distance_table)
        distance = csv_distance_table[x_value][y_value]
        return float(distance)

    # Show the status of all packages at a specific time
    # The complexity of this function is O(N) because the for loop executes a block of code for each package in the
    # package_table input
    def status_of_packages(self, package_table, time):
        for packageID in range(1, self.number_of_packages):
            package = package_table.lookup_package(packageID)
            if time == "EOD":
                print("Package ID: " + str(package.package_ID), "Package address: " + str(package.address),
                      "Package City: " + str(package.city), "Package State: " + str(package.state),
                      "Package Zip: " + str(package.zip_code), "Package Deadline: " + str(package.deadline),
                      "Package weight (kg): " + str(package.weight), "Package status: " + str(package.status[-1]) +
                      " at " + str(package.package_departure_time))
            elif package.delivery_time <= time:
                print("Package ID: " + str(package.package_ID), "Package address: " + str(package.address),
                      "Package City: " + str(package.city), "Package State: " + str(package.state),
                      "Package Zip: " + str(package.zip_code), "Package Deadline: " + str(package.deadline),
                      "Package weight (kg): " + str(package.weight), "Package status: " + str(package.status[-1]) +
                      " at " + str(package.delivery_time))
            elif package.delivery_time >= time >= package.package_departure_time:
                print("Package ID: " + str(package.package_ID), "Package address: " + str(package.address),
                      "Package City: " + str(package.city), "Package State: " + str(package.state),
                      "Package Zip: " + str(package.zip_code), "Package Deadline: " + str(package.deadline),
                      "Package weight (kg): " + str(package.weight), "Package status: " + str(package.status[1]) +
                      " at " + str(package.package_departure_time))
            elif package.delivery_time >= time and package.package_departure_time >= time:
                print("Package ID: " + str(package.package_ID), "Package address: " + str(package.address),
                      "Package City: " + str(package.city), "Package State: " + str(package.state),
                      "Package Zip: " + str(package.zip_code), "Package Deadline: " + str(package.deadline),
                      "Package weight (kg): " + str(package.weight), "Package status: " + str(package.status[0]) +
                      " at " + str(package.load_time))
