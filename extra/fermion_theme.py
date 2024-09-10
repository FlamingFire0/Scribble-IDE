try:
    from ttkbootstrap.themes.user import USER_THEMES #the user's themes dict
except:
    USER_THEMES = {} #for the possibility that the user doesn't have a user.py file or a USER_THEMES dict
    
from ttkbootstrap.themes import user #to get the path
from json import dumps #for formatting 
from colorsys import hsv_to_rgb, rgb_to_hsv  # for hue shifting

# the theme™️
base = {
    "fermion":{
        "type": "dark",
        "colors": {
            "primary": "#8b2d74",
            "secondary": "#ea7434",
            
            
            "light": "#ff51d4",
            "dark": "#170229",
            
            "bg": "#2c0643",
            "fg": "#ffd1a7",
            
            "success": "#e7b832",
            "info": "#ff9737",
            "warning": "#f6650b",
            "danger": "#f64d0b",
            
            "selectbg": "#d745b3",
            "selectfg": "#ffffff",
            
            "inputfg": "#ffd1a7",
            "inputbg": "#2c0643",
            
            "active": "#17082E",
            "border": "#060606"
        }
    }
}




#hue_shift_amount = 69

#def split_hex_color(hex_color):
#    color = hex_color.replace("#", "")
#    
#    return (int(color[0]+color[1], 16), int(color[2]+color[3], 16), int(color[4]+color[5], 16))
#
#
#def tuple_to_hex_color(r,g,b):
#    hex_r = format(int(round(r)), '02x')
#    hex_g = format(int(round(g)), '02x')
#    hex_b = format(int(round(b)), '02x')
#    hex_color = '#' + hex_r + hex_g + hex_b
#    return hex_color
#def hue_shift(color, amount):
#    
#    h, s, v = rgb_to_hsv(*split_hex_color(color))
#    
#    if amount == 0:
#        return tuple_to_hex_color(*hsv_to_rgb(h, s, v))
#
#
#    h = (h + 360/amount) % 1
#
#    return tuple_to_hex_color(*hsv_to_rgb(h, s, v))
#
#for hue_shift_amount in range(0,1000):
#    theme = base
#    for id, color in base['colors'].items():
#        theme['colors'][id] = hue_shift(color, hue_shift_amount)
#
#
#    #print(globals()['base_'+int(hue_shift_amount)])
#
#    out = {
#        "fermion_"+str(hue_shift_amount): theme
#    }


    #if theme already exists, doesn't do anything(or updates it idek), if not adds it
USER_THEMES.update(base)




with open(str(user).replace("<module 'ttkbootstrap.themes.user' from '", '').replace("'>", ''), 'w') as f: #opens the user.py file

    f.write("USER_THEMES = "+dumps(USER_THEMES, indent=4)) # writes it to the user.py file, formatted




