""" main user for the shape manupulation"""

from src.user_shape_manipulation import Point, Circle, Rectangle

if __name__ == "__main__":
    p1 = Point(1,2)
    p2 = Point(1,4)
    print(p1.distance_to(p2))

    circle1 = Circle(center=Point(1,1), radius=2)
    print(circle1.contains_point(p1), circle1.contains_point(p2))

    rec1 = Rectangle(bottom_left=Point(1,1), width=5, height=3)
    print(rec1.overlaps_with(circle1))
    