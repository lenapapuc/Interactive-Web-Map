def elevation_calculation(elevation):
    color = ""
    if elevation <= 2000:
        color = "green"
    elif elevation <=3000:
        color = "orange"
    elif elevation > 3000:
        color = "red"
    
    return color
  
