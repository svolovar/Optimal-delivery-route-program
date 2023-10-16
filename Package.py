class Package:
    def __init__(self, package_ID, address, city, state, zip_code, deadline, weight, status):
        self.package_ID = package_ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = []
        self.load_time = None
        self.delivery_time = None
        self.package_departure_time = None

    def __str__(self):
        # The complexity of this function is O(1) because it executes a set number of lines of code regardless of the
        # input
        return "%s %s %s %s %s %s %s %s" % ("Package ID: " + str(self.package_ID),
                                            "\nPackage address: " +str(self.address),
                                            "\nPackage City: " + str(self.city),
                                            "\nPackage State: " +str(self.state),
                                            "\nPackage Zip: " + str(self.zip_code),
                                            "\nPackage Deadline: " + str(self.deadline),
                                            "\nPackage weight (kg): " + str(self.weight),
                                            "\nPackage status: " + str(self.status[-1]))

    # Show the tracking information based on the input time
    # The complexity of this function is O(1) because it executes a set number of lines of code regardless of the input
    def show_tracking_info(self, time):

        # Show the package information and status at EOD
        if time == "EOD":
            print("Package number " + str(self.package_ID) + " tracking report at " + str(time) + ":")
            print("Arrived in hub at: " + str(self.load_time))
            print("Out for delivery (en-route) at: " + str(self.package_departure_time))
            print("Delivered to " + "'" + str(self.address) + "'" + " at: " + str(self.delivery_time))

        # Show the status of the package when the delivery time is less than or equal to the input time (delivered)
        elif self.delivery_time <= time:
            print("Package number " + str(self.package_ID) + " tracking report at " + str(time) + ":")
            print("Arrived in hub at: " + str(self.load_time))
            print("Out for delivery (en-route) at: " + str(self.package_departure_time))
            print("Delivered to " + "'" + str(self.address) + "'" + " at: " + str(self.delivery_time))

        # If the input time is in between delivery time and departure time, show en-route status
        elif self.delivery_time >= time >= self.package_departure_time:
            print("Package number " + str(self.package_ID) + " tracking report at " + str(time) + ":")
            print("Arrived in hub at: " + str(self.load_time))
            print("Out for delivery (en-route) at: " + str(self.package_departure_time))

        # If the input time is before the departure time, and delivery time, show in-hub status
        elif self.delivery_time >= time and self.package_departure_time >= time:
            print("Package number " + str(self.package_ID) + " tracking report at " + str(time) + ":")
            print("Arrived in hub at: " + str(self.load_time))
        return

