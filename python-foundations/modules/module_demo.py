"""
module_demo.py

Topic: Using a Custom Module (Import Styles)
Covers: import module | from module import function | import module as alias
Use-case: a weekend trip planner that needs unit conversions
"""

# ---------------------------------------------------------
# SECTION 1: import module — Distance Conversion
# ---------------------------------------------------------
print("---- import custom_module: Distance Conversion ----")

import custom_module

trip_distance_km = 450
trip_distance_miles = custom_module.km_to_miles(trip_distance_km)
print(f"Trip distance: {trip_distance_km} km = {trip_distance_miles:.2f} miles")


# ---------------------------------------------------------
# SECTION 2: from module import function — Temperature Check
# ---------------------------------------------------------
print("\n---- from custom_module import: Temperature Check ----")

from custom_module import celsius_to_fahrenheit

destination_temp_c = 18
destination_temp_f = celsius_to_fahrenheit(destination_temp_c)
print(f"Destination temperature: {destination_temp_c}C = {destination_temp_f:.2f}F")


# ---------------------------------------------------------
# SECTION 3: import module as alias — Luggage Weight
# ---------------------------------------------------------
print("\n---- import custom_module as uc: Luggage Weight ----")

import custom_module as uc

luggage_weight_kg = 18.5
luggage_weight_lb = uc.kg_to_pounds(luggage_weight_kg)
print(f"Luggage weight: {luggage_weight_kg} kg = {luggage_weight_lb:.2f} lb")


# ---------------------------------------------------------
# SECTION 4: Trip Summary — Combining Everything
# ---------------------------------------------------------
print("\n---- Trip Summary ----")

print(f"You're traveling {trip_distance_miles:.2f} miles to a place that's {destination_temp_f:.2f}F, "
      f"carrying {luggage_weight_lb:.2f} lb of luggage.")

# module-level constants are accessible too, not just functions
print(f"\n(Fun fact: custom_module also has PI = {custom_module.PI}, "
      f"used internally by its circle_area function.)")
