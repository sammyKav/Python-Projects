
class Facility:  # creating facilities for a fictional company. All building have below attributes
    name = 'No Name Provided'
    country ='US'
    city = ''
    state = ''
    sqrFt = 0
    max_occupancy = 1
    phone = ''

class DC(Facility): # has attributes unqiue to a dc. 
    dock_doors = 1
    inv_ailse = 0
    hazmat_ailse = 0
    DC_manger = ''
    DC_volume_rank = 1
    

class Store(Facility): # has attributes unique to a retail store. 
    checkout_lines = 1
    merch_ailes = 0
    dock_door = 0
    store_manger = ''
    sales_volume_rank = 1
    
    


    
