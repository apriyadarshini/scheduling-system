#!/bin/env python
import math
class vehicle:
    '''
    This is the vehicle class. Drone and cycle classes inherit this class. 
    '''
    def __init__(self,spd,wt,noop,vehidlist,type):
        type = type
        vehicle_id = self.generaterandomid()#26 alphabets taken 2 at a time multiplied by 10 numbers taken 4 at a time 
        count = len(vehicle_id) #This is the number of the correspomding vehicle at disposal. This will be the length of the vehicle_id which is a list of number plates of all vehicles
        speed = spd #speed at which vehicle travels
        weight = wt #max weight the vehicle can take at a given time
        NoOfPackages = noop #Maximum Number of packages the vehicle can take at once
        
    def generaterandomid(self):
        li = []
        return li
        
    def commute(self):
        pass #unimplemented method that is overridden in child classes
        
    def isavailable(self):
        if self.count>0:
            return True
        else:
            return False
            
    def getvehicle(self):
        self.count -= 1 #assign the vehicle based on which child class is instanciated 
        vehno = self.vehicle_id[droneobj.count] # get the number plate of the vehicle
        del self.vehicle_id[droneobj.count] #remove it from the list and mark it unavailable
        
    def addvehicle(self,vehno):
        '''This method adds the vehicle back to the pool once the delivery is completed and the vehicle is back to the depot'''
        self.count+=1
        self.vehicle_id.append(vehno)
        
        
        
class drone(vehicle):
    def commute(self,north,east):
        '''This function defines how the drones commutes. Given two distances north and east for example, it uses pythagorus theorem to 
        get the shortest distance between depot and destination. This is multiplied by 2 considering that the drone needs to come back to depot after delivering'''
        return 2*math.sqrt(math.pow(north,2)+math.pow(east,2)) 
     
     
class cycle(vehicle):
    def commute(self,north,east):
        '''This uses a simple addition since the distances passed is aligned with road grid.This is multiplied by 2 considering that the cycle needs to come back to depot after delivering'''
        return 2*(north+east)
        
        