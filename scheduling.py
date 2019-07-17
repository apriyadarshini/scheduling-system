#!/bin/env python
import vehicle


class scheduling:
    
    def __init__(self,deliverylist,drones,cycles,proddict):
        dellist = deliverylist
        droneobj = drones
        cycleobj = cycles
        product = procdict
        
    def schedule(self):
        '''This method calls get vehicle to schedule each delivery in the list'''
        for delv in self.dellist:
            self.getvehicle(delv)
            
    def getobj(self,noofpackages,wt): #This is a factory method and it returns the right object (droneobj or cycleobj) based on the condition
        if noofpackages == 1:
           
            obj = self.droneobj
            
            if obj.isavailable() and wt<obj.weight: #check if the vehicle is available and the weight of the package is less than what drone can take
                return obj
            else:
                obj = self.cycleobj
                if obj.isavailable():
                    return obj
                else:
                    return -1
        else:
            
            obj = self.cycleobj
            while wt > obj.weight: 
            # This loop makes sure that if there are packages considered such that their total weight cannot be accomodated on a cycle, 
            #it removes one product at a time such that total weight is less than max weight a cycle can handle
                prod = self.delv_list_cur[-1]
                del self.delv_list_cur[-1]
                self.delv_list.insert(0,prod)
                wt -= product[prod]
            if obj.isavailable():
                return obj
            else:
                return -1
          
        
    def getvehicle(self,delv):
        '''This method always picks drone if number of packages is 1 and there is a drone available and the weight of the package is what the drone can accomodate. 
        If any of the above condition is not satisfied, it picks a cycle. If there are more than 4 packages, it splits and appropriate vehicles are picked to deliver all the packages'''
        
        self.delv_list = list(delv.packtup) #make the tuple mutable so that it can be deleted once considered for delivery
        
        #sort the list of products based on the weight in descending order
        
        self.delv_list_cur = None
        while self.delv_list or self.delv_list_cur: #keeps waiting till a vehicle is available
            if self.delv_list_cur is None:
                if len(self.delv_list) > 1:
                    if len(self.delv_list) <=4:
                       self.delv_list_cur = self.delv_list
                       
                    else:
                        self.delv_list_cur = self.delv_list[0:4]
                        del self.delv_list[0:4]
                else:
                    self.delv_list_cur =    self.delv_list  #delivery contains only one package
                    
                wt=0    
                for p in self.delv_list_cur:
                    wt += self.product[p] #get the total weight of the considered product from product dictionary 
            
           
            
            veh_obj = self.getobj(len(self.delv_list_cur),wt)#call the factory method with the length of list and total weight of all products considered in list
            
            if veh_obj == -1:
                print('No vehicle available for delivery at the moment')
                
            else:
                self.delv_list_cur = None
                vehno = veh_obj.getvehicle()  #get the vehicle's number plate
                distance = veh_obj.commute() #get the distance to schedule
                print('{"package":self.delv_list_cur,"vehicle":vehno,"destination":distance}') #Final result is printed on screen
                
                
        
    
    

