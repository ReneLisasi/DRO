import math
class Node:
    def __init__(self,coordinates,distance):
        self.coordinates=coordinates
        self.distance=distance
    
    def set_distance(self,distance):
        self.distance=distance

    def lt(self,other):
        return self.distance < other.distance

def brute_force(fire_stations, starting_point):
    distances=[]
    #brute force
    for i in fire_stations:
        total_distance=math.sqrt((i.coordinates[0]-starting_point.coordinates[0])**2+(i.coordinates[1]-starting_point.coordinates[1])**2)
        i.set_distance=(total_distance)
        distances.append(i)
    minimum_point=min(distances, key=lambda x: x.distance)
    return minimum_point

inf=float('inf')
north_station=Node((33.8894627,-84.5165133),inf)
west_station=Node((33.8715290,-84.5347762),inf)
east_station=Node((33.8833968,-84.4833590),inf)
starting_point=Node((33.8802511,-845125968),0)
fire_stations=[west_station,east_station,north_station]
closest_fire_station=brute_force(fire_stations,starting_point)
print(f'Closest fire station to disaster at {starting_point.coordinates} is {closest_fire_station.coordinates}, getting directions...')