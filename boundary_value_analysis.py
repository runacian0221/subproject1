def boundary_value(value):
    if 0.3<= value < 0.6:
        return 0.45
    elif 0.6 <= value < 0.9:
        return 0.75
    elif 0.9 <= value < 1.2:
        return 1.05
    elif 1.2 <= value < 1.5:
        return 1.35
    elif 1.5 <= value < 1.8:
        return 1.65
    elif 1.8 <= value < 2.1:
        return 1.95
    elif 2.1 <= value < 2.4:
        return 2.25
    elif 2.4 <= value < 2.7:
        return 2.55
    elif 2.7 <= value < 3.0:
        return 2.85
    elif 3.0 <= value < 3.3:
        return 3.15        
    elif 3.3 <= value < 3.6:
        return 3.45
    elif 3.6 <= value < 3.9:
        return 3.75
    elif 3.9 <= value < 4.2:
        return 4.05
    elif 4.2 <= value < 4.5:
        return 4.35
    elif 4.5 <= value < 4.8:
        return 4.65
    elif 4.8 <= value < 5.1:
        return 4.95
    else:
        return value