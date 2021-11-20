import numpy as np


def calc_solar_array_power_generation(sun_distance, effective_area, efficiency=0.28, incidence_angle=0, solar_constant=1366):
    '''
    Calculates and returns solar panel / array power generation.

    INPUTS:
    sun_distance (float, scalar, units=AU) - Distance solar panel is from the sun in Astronomical Units.
    effective_area (float, scalar, units=m^2) - Area of the solar panel that is capable of generating power.
    efficiency (float, scalar) - Efficiency of the solar panel, where 1.0 is 100% efficient.
    incidence_angle (float, scalar, units=deg) - Angle between the sun vector and line perpendicular to the solar panel surface.
    solar_constant (float, scalar, units=W/m^2) - Total energy received from the Sun per unit area, also referred to as Solar Flux. Average solar flux is 1366 W/m^2 (1 AU), value fluctuates +/- 0.1% through the 11-year solar cycles. 
    
    OUTPUT:
    power_generation (float, scalar, units=W) - Amount of power the solar panel generated.
    '''

    if sun_distance != 0:
        sun_distance_ratio = (1.0 / sun_distance**2)
        power_generation = sun_distance_ratio*solar_constant*effective_area*efficiency*np.cos(np.deg2rad(incidence_angle))

    else:
        print('[WARNING - calc_solar_array_power_generation] - Input value sun_distance cannot be 0.')
        power_generation = None

    return power_generation


def calc_panel_temperature(sun_distance, absorptivity=0.85, emissivity=0.72, solar_constant=1366):
    '''
    Returns a flat panel's equilibrium steadystate temperature as a function of sun distance and material properties.

    INPUTS:
    sun_distance (float, scalar, units=AU) - Distance solar panel is from the sun in Astronomical Units. 
    absorptivity (float, scalar) - Degree to which panel absorbs energy, where 1.0 is perfect absorbant.
    emissivity (float, scalar) - The effectiveness of emitting energy from the surface.
    solar_constant (float, scalar, units=W/m^2) - Total energy received from the Sun per unit area, also referred to as Solar Flux. Average solar flux is 1366 W/m^2 (1 AU), value fluctuates +/- 0.1% through the 11-year solar cycles. 

    OUTPUT:
    power_generation (float, scalar, units=C) - Steadystate equilibrium temperature.
    '''
    STEFAN_BOLTZMANN = 5.670374419*10**-8 # Stefan-Boltzmann constant (units = W /(m^2 * K^4))     

    if sun_distance != 0:
        solar_flux = solar_constant*(1.0/sun_distance**2)
                
        # panel equilibrium temperature in Kelvin
        panel_temperature = ((absorptivity*solar_flux) / (2*emissivity*STEFAN_BOLTZMANN))**0.25
        panel_temperature = panel_temperature * 273.15 # convert from Kelvin to Celsius
    else:
        panel_temperature = None
    
    return panel_temperature

