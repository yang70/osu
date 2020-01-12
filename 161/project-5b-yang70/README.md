# project-5b

Write a class named Taxicab that has three **private** data members: one that holds the current x-coordinate, one that holds the current y-coordinate, and one that holds the odometer reading (the actual odometer distance driven by the Taxicab, not the Euclidean distance from its starting point).  The class should have an init method that takes two parameters and uses them to initialize the coordinates, and also initializes the odometer to zero.  The class should have get members for each data member: get_x_coord, get_y_coord, and get_odometer.  The class does not need any set methods.  It should have a method called move_x that takes a parameter that tells how far the Taxicab should shift left or right. It should have a method called move_y that takes a parameter that tells how far the Taxicab should shift up or down.  For example, the Taxicab class might be used as follows:
```
cab = Taxicab(5, -8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odometer())
```
The file must be named: Taxicab.py
