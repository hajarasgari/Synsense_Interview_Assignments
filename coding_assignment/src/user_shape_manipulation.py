"""Python code for defining and manipulating two-dimensional geometric shapes."""
import math

class Point:
    """Represents a point in a 2D space."""
    def __init__(self, x: float, y: float):
        """
        Initialize a point with x and y coordinates. 

        x: The x-coordinate of the point.
        y: The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:

        """        
        Calculate the Euclidean distance between this point and another point.
        It returns the Euclidean distance as a float.
        
        other: The other point to which distance is calculated.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Shape:
    """
    Abstract base class for all shapes in 2D space.
    """
    def contains_point(self, point: Point) -> bool:
        """
        Determine if the shape contains a given point.
        It returns True if the shape contains the point, False otherwise.
        
        point: The point to be checked. 
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

    def overlaps_with(self, other: 'Shape') -> bool:
        """
        Determine if this shape overlaps with another shape.
        It returns True if the shapes overlap, False otherwise.

        other: The other shape to check for overlap.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

class Circle(Shape):
    """Represents a circle in 2D space, defined by its center point and radius."""

    def __init__(self, center: Point, radius: float):
        """
        Initialize a circle with a center point and radius.
        
        center: The center point of the circle.
        radius: The radius of the circle.
        """
        self.center = center #Point object
        self.radius = radius
    def contains_point(self, point: Point) -> bool:
        """
        Check if the circle contains a given point.
        It returns True if the point is inside the circle, False otherwise.
        
        point: The point to be checked.
        """
        return self.center.distance_to(point) <= self.radius

    def overlaps_with(self, other: Shape) -> bool:
        """
        Check if this circle overlaps with another shape.
        It returns True if the shapes overlap, False otherwise.
        
        other: The other shape to check for overlap. The other shape can be Circle or Rectangle.
        
        """
        if isinstance(other, Circle):
            # Check if the circles overlap by comparing distances between centers.
            return self.center.distance_to(other.center) <= self.radius + other.radius
        if isinstance(other, Rectangle):
            # Check for overlap with a rectangle by examining closest point
            # on the rectangle to the circle center.
            closest_x = max(other.bottom_left.x, min(self.center.x, other.bottom_left.x + other.width))
            closest_y = max(other.bottom_left.y, min(self.center.y, other.bottom_left.y + other.height))
            closest_point = Point(closest_x, closest_y)
            return self.contains_point(closest_point)
        return False

class Rectangle(Shape):
    """
    Represents a rectangle in 2D space, defined by its bottom-left corner, width, and height.
    """
    def __init__(self, bottom_left: Point, width: float, height: float):
        """
        Initialize a rectangle with a bottom-left corner, width, and height.
        
        bottom_left: The bottom-left corner of the rectangle.
        width: The width of the rectangle.
        height: The height of the rectangle.
        """
        self.bottom_left = bottom_left
        self.width = width
        self.height = height

    def contains_point(self, point: Point) -> bool:
        """
        Check if the rectangle contains a given point.
        It returns True if the point is inside the rectangle, False otherwise.
        
        point: The point to check.
        
        """
        return (self.bottom_left.x <= point.x <= self.bottom_left.x + self.width and
                self.bottom_left.y <= point.y <= self.bottom_left.y + self.height)

    def overlaps_with(self, other: Shape) -> bool:
        """
        Check if this rectangle overlaps with another shape.
        It returns True if the shapes overlap, False otherwise.
        
        other: The other shape to check for overlap.
        """
        if isinstance(other, Rectangle):
            # Check if the rectangles overlap by comparing their bounds.
            print((self.bottom_left.x > other.bottom_left.x + other.width or
                        self.bottom_left.x + self.width < other.bottom_left.x or
                        self.bottom_left.y > other.bottom_left.y + other.height or
                        self.bottom_left.y + self.height < other.bottom_left.y))
            return not (self.bottom_left.x > other.bottom_left.x + other.width or
                        self.bottom_left.x + self.width < other.bottom_left.x or
                        self.bottom_left.y > other.bottom_left.y + other.height or
                        self.bottom_left.y + self.height < other.bottom_left.y)

        if isinstance(other, Circle):
            # Check for overlap with a circle by examining the closest point
            # on the rectangle to the circle center.
            closest_x = max(self.bottom_left.x, min(other.center.x, self.bottom_left.x + self.width))
            closest_y = max(self.bottom_left.y, min(other.center.y, self.bottom_left.y + self.height))
            closest_point = Point(closest_x, closest_y)
            return other.contains_point(closest_point)
        return False
    