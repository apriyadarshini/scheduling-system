#!/bin/env python

import json
import vehicle
import delivery
import scheduling

'''This is the driver code. Here we read input.txt which contains the sample input and deliveries are scheduled'''    
if __name__ == '__main__':
    
    drones = vehicle.drone(30,5,1,'drone') #speed,wt, number of packages,type. This can as well be hardcoded in the constructor if the value will remain the same always. 
    cycles = vehicle.cycle(15,50,4,'cycle')
    delivery_li = []
    with open('input.txt','r') as fr:
        for line in fr:
            dictt = line.split(' = ')
            delivery_dict = json.loads(dictt)[0] #loads the json string into dictionary
            delobj = delivery(delivery_dict[0],delivery_dict[1])
            delivery_li.append(delobj)
    

    #read product.json and load it into product dictionary with key as product id and value as weight
    
    with open('product.json', 'r') as myfile:
        data=myfile.read()

    # parse file
    productdict = json.loads(data)
    
    
    
    scheduleobj = scheduling(delivery_li,drones,cycles,productdict) #scheduling class is instanciated with 
    scheduleobj.schedule()
            
            
            
        
