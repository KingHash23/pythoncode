# Define a Waypoint class to represent each waypoint.
class Waypoint:
    def __init__(self, location: str, description: str):
        """
        Initialize a new Waypoint with the given location and description.
        """
        self.location = location  # The location of the waypoint
        self.description = description  # A brief description of the waypoint
        self.next_waypoint = None  # Link to the next waypoint (initially None)
        self.previous_waypoint = None  # Link to the previous waypoint (initially None)

# Define a Route class using a singly linked list.
class Route:
    def __init__(self):
        """
        Initialize an empty route (singly linked list).
        """
        self.head = None  # The head of the linked list (initially None)

    def add_waypoint(self, location: str, description: str):
        """
        Add a new waypoint to the end of the route.
        :param location: The location of the new waypoint.
        :param description: A brief description of the new waypoint.
        """
        new_waypoint = Waypoint(location, description)

        if not self.head:
            # If the route is empty, set the new waypoint as the head.
            self.head = new_waypoint
        else:
            # Otherwise, find the last waypoint and link it to the new waypoint.
            current = self.head
            while current.next_waypoint:
                current = current.next_waypoint
            current.next_waypoint = new_waypoint

    def traverse_forward(self):
        """
        Traverse the route in a forward direction and print waypoint information.
        """
        current = self.head
        while current:
            print(f"Location: {current.location}, Description: {current.description}")
            current = current.next_waypoint

# Define a BidirectionalRoute class using a doubly linked list.
class BidirectionalRoute(Route):
    def add_waypoint(self, location: str, description: str):
        """
        Add a new waypoint to the end of the bidirectional route.
        :param location: The location of the new waypoint.
        :param description: A brief description of the new waypoint.
        """
        new_waypoint = Waypoint(location, description)

        if not self.head:
            # If the route is empty, set the new waypoint as the head.
            self.head = new_waypoint
        else:
            # Otherwise, find the last waypoint, link it to the new waypoint,
            # and update the new waypoint's previous link.
            current = self.head
            while current.next_waypoint:
                current = current.next_waypoint
            current.next_waypoint = new_waypoint
            new_waypoint.previous_waypoint = current

    def traverse_backward(self):
        """
        Traverse the bidirectional route in a backward direction and print waypoint information.
        """
        current = self.head
        while current.next_waypoint:
            current = current.next_waypoint
        while current:
            print(f"Location: {current.location}, Description: {current.description}")
            current = current.previous_waypoint

# Example usage:
route = BidirectionalRoute()
route.add_waypoint("Point A", "Starting point")
route.add_waypoint("Point B", "Scenic overlook")
route.add_waypoint("Point C", "Trailhead")
route.add_waypoint("Point D", "Fishing spot")
route.add_waypoint("Point E", "Final destination")

print("Forward traversal:")
route.traverse_forward()

print("\nBidirectional traversal:")
route.traverse_backward()