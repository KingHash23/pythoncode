class Waypoint:
    def __init__(self, location, description):
        """
        Constructor to initialize a waypoint.

        :param location: The location of the waypoint.
        :type location: str
        :param description: The description of the waypoint.
        :type description: str
        """
        self.location = location
        self.description = description
        self.prev = None
        self.next = None

class Route:
    def __init__(self):
        """
        Constructor to initialize the route head.
        """
        self.head = None

    def add_waypoint(self, location, description):
        """
        Method to add a new waypoint to the route.

        :param location: The location of the new waypoint.
        :type location: str
        :param description: The description of the new waypoint.
        :type description: str
        """
        new_waypoint = Waypoint(location, description)
        if not self.head:
            self.head = new_waypoint
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_waypoint

    def insert_waypoint_after(self, target, location, description):
        """
        Method to insert a new waypoint after a target waypoint.

        :param target: The target waypoint.
        :type target: Waypoint
        :param location: The location of the new waypoint.
        :type location: str
        :param description: The description of the new waypoint.
        :type description: str
        """
        new_waypoint = Waypoint(location, description)
        current = self.head
        while current:
            if current.location == target.location:
                new_waypoint.next = current.next
                current.next = new_waypoint
                new_waypoint.prev = current
                if new_waypoint.next:
                    new_waypoint.next.prev = new_waypoint
                break
            current = current.next

    def remove_waypoint(self, location):
        """
        Method to remove a waypoint from the route.

        :param location: The location of the waypoint to remove.
        :type location: str
        """
        current = self.head
        prev = None
        while current:
            if current.location == location:
                if prev:
                    prev.next = current.next
                    if current.next:
                        current.next.prev = prev
                else:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                break
            prev = current
            current = current.next

    def next_waypoint(self):
        """
        Method to traverse to the next waypoint in the route.

        :return: The next waypoint or None if the end of the route has been reached.
        :rtype: Waypoint or None
        """
        if self.head:
            self.head = self.head.next
            return self.head

class BidirectionalRoute(Route):
    def __init__(self):
        """
        Constructor to initialize the bidirectional route head.
        """
        super().__init__()

    def previous_waypoint(self):
        """
        Method to traverse to the previous waypoint in the bidirectional route.

        :return: The previous waypoint or None if the beginning of the route has been reached.
        :rtype: Waypoint or None
        """
        if self.head and self.head.prev:
            self.head = self.head.prev
            return self.head

def print_menu():
    """
    Function to print the menu options.
    """
    print("\nMenu:")
    print("1. Add waypoint")
    print("2. Insert waypoint after")
    print("3. Remove waypoint")
    print("4. Traverse in single direction")
    print("5. Bidirectional traversal")
    print("6. Exit")

# Example usage
route = BidirectionalRoute()

# Add waypoints
route.add_waypoint("Point A")