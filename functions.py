def elevation_calculation(el):
    color = ""

    try:
        elevation = int(el)
    except ValueError:
        return "blue"
    
    elevation = int(el)
    if elevation <= 2000:
        color = "green"
    elif elevation <=3000:
        color = "orange"
    elif elevation > 3000:
        color = "red"
    else:
        color = "blue"
    
    return color
  
