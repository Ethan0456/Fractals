import math
import matplotlib.pyplot as plt
import random as rn
import numpy as np


def get_random_vertice():
    return rn.randint(0,2)

def get_coordinates_of_point_at_half_distance(x1,x2):
    return ( (x2[0]+x1[0])/2 , (x2[1]+x1[1])/2 )

if __name__ == "__main__":
    edge_length = int(input("Enter Edge Length of Equilateral Triangle : "))
    coordinates = [(0,0), (edge_length,0), (edge_length/2,edge_length)]
    area = (math.sqrt(3)/4)*(math.pow(edge_length, 2))

    generated_dots = []

    times = int(input("Enter Number of Dots : "))

    point = (edge_length/2, edge_length/2)
    while times:
        print("point :",point)
        random_vertice = coordinates[get_random_vertice()]
        print("random_vertice : ", random_vertice)
        half_point = get_coordinates_of_point_at_half_distance(point, random_vertice)
        print("half_point ", half_point)

        generated_dots.append(point)
        generated_dots.append(half_point)

        print("-"*100)

        point = half_point
        
        times -= 1

    x = [vertice[0] for vertice in generated_dots]
    y = [vertice[1] for vertice in generated_dots]

    plt.scatter(x, y, color='blue')
    # plt.xlim(-3,4)
    # plt.ylim(-3,4)
    plt.title("Sierpinski-Triangle-Fractal")
    plt.show()