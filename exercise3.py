def steigung_funktion(liste):
    x1 = liste[0]
    y1 = liste[1]
    x2 = liste[2]
    y2 = liste[3]
    
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    m = delta_y / delta_x
    
    if delta_x == 0:
        print ("Die Steigung ist nicht definiert")
    else: 
        print(m)
    
 steigung_funktion([8,3,8,4])
 