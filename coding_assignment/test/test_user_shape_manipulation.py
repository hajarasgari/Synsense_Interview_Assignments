""" Pytest codes for testing user_shape_manipulation functionality """

from src.user_shape_manipulation import Point, Circle, Rectangle

def test_defining_points() -> None:
    """Test that the user is able to define a point."""
    p1 = Point(1,2)
    p2 = Point(1,5)
    assert p1.distance_to(p2) == 3

def test_a_circle_contains_a_point() -> None:
    """Test the user is able to determine whether a point is contained within a circle."""
    circle = Circle(center=Point(5,5), radius=3)
    p1 = Point(3,4)
    p2 = Point(1,1)
    assert circle.contains_point(p1) is True
    assert circle.contains_point(p2) is False

def test_a_rectangle_contains_a_point() -> None:
    """Test the user is able to determine whether a point is contained within a rectangle."""
    rectangle = Rectangle(bottom_left=Point(1,1), width=5, height=3)
    p1 = Point(3,4)
    p2 = Point(10,10)
    assert rectangle.contains_point(p1) is True
    assert rectangle.contains_point(p2) is False

def test_a_circle_has_overlaps_with_another_circle() -> None:
    """Test the user is able to determine whether a circle has overlap with another circle."""
    circle1 = Circle(center=Point(3,3), radius=2)
    circle2 = Circle(center=Point(3,7), radius=5)
    circle3 = Circle(center=Point(3,7), radius=1)
    assert circle1.overlaps_with(circle2) is True
    assert circle1.overlaps_with(circle3) is False

def test_a_circle_has_overlaps_with_a_rectangle() -> None:
    """Test the user is able to determine whether a circle has overlap with another circle."""
    circle1 = Circle(center=Point(3,3), radius=2)
    rec1 = Rectangle(bottom_left=Point(3,3), width=2, height=5)
    rec2 = Rectangle(bottom_left=Point(6,6), width=2, height=2)
    assert circle1.overlaps_with(rec1) is True
    assert circle1.overlaps_with(rec2) is False
