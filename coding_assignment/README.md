# Synsense interveiw: coding assignment

## Coding exercise 1
Design and code a set of classes in Python for defining and manipulating
two-dimensional geometric shapes. A user should be able to define points
and at least two shapes (e.g. rectangle; triangle; circle). User should be
able to determine whether an arbitrary point is contained within a shape,
and whether two shapes overlap. The classes should have a clean inheri-
tance hierarchy, and be well-documented. Methods do not need to be fully
implemented, but can exist as stubs.

### Answer
This folder contains a Python code example for a set of classes that define and manipulate two-dimensional geometric shapes. The design contains a base Shape class, along with Point, Rectangle, and Circle classes. The Rectangle and Circle classes are inheriting from Shape class. This design follows a clean inheritance hierarchy and provides a framework that can easily be extended to support additional shapes, such as triangles. The main class of the code are defined as:

**Point Class:**
        Represents a point in 2D space with coordinates (x, y).
        Includes a distance_to method to compute the distance to another point.

**Shape Class:**
        Provides an interface for geometric shapes.
        Contains methods contains_point and overlaps_with, which are meant to be overridden by the child classes.

**Rectangle Class:**
        This class inherits from Shape and represents a rectangle defined by a bottom_left corner, width, and height.
        Implements contains_point to check if a given point is within the rectangle.
        Implements overlaps_with to determine overlap with another shape (circle and rectangle).

**Circle Class:**
        Inherits from Shape and represents a circle defined by its center and radius.
        Implements contains_point to check if a given point is within the circle.
        Implements overlaps_with to determine overlap with another shape (circle and rectangle).

The structure of this project looks like this:<br>

coding_assignment<br>
    |___ src<br>
    |   |___ __init__.py<br>
    |   |___ user_shape_manipulation.py<br>
    |___ tests<br>
    |   |___ __init__.py<br>
    |   |___ test_user_shape_manipulation.py<br>
    |___ main.py<br>
    
#### Installation
```
virtualenv env_coding
source env_coding/bin/activate
pip install requirements.txt -r
```

#### Run tests
```
pytest test_user_shape_manipulation.py
```

#### Run user
```
python main.py
```
