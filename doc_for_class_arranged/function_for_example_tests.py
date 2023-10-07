from typing import Union

def area_of_rectangle(width: Union[float, int], height: Union[float, int]) -> Union(float, int):
    """
    A function for calculating the area of a certain rectangle with provided width and height.
    Input 1: width, float/int;
    Input 2: height, float/int;
    Output: area of the rectangle, float/int.
    """
    area_of_rec = width * height
    return area_of_rec


def perimeter_of_rectangle(width: Union[float, int], height: Union[float, int]) -> Union[float, int]:
    """
    A function for calculating the perimeter of a certain rectangle with provided width and height.
    Input 1: width, float/int;
    Input 2: height, float/int;
    Output: perimeter of the rectangle, float/int.
    """
    perimeter_of_rec = 2 * (width + height)
    return perimeter_of_rec
