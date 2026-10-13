"""
module_demo.py

Topic: Using a Custom Module (Import Styles)
Covers: import module | from module import function | import module as alias
Use-case: a weekend trip planner that needs unit conversions
"""

import custom_module                              # style 1: import module
from custom_module import celsius_to_fahrenheit   # style 2: from module import function
import custom_module as uc                        # style 3: import module as alias


def main():
    # ---------------------------------------------------------
    # SECTION 1: import module (style 1) — Distance Conversion
    # ---------------------------------------------------------
    print("---- Style 1: import custom_module (Distance Conversion) ----")

    trip_distance_km = 450
    trip_distance_miles = custom_module.km_to_miles(trip_distance_km)
    print(f"Trip distance: {trip_distance_km} km = {trip_distance_miles:.2f} miles")

    # ---------------------------------------------------------
    # SECTION 2: from module import function (style 2) — Temperature Check
    # ---------------------------------------------------------
    print("\n---- Style 2: from custom_module import (Temperature Check) ----")

    destination_temp_c = 18
    destination_temp_f = celsius_to_fahrenheit(destination_temp_c)
    print(f"Destination temperature: {destination_temp_c}C = {destination_temp_f:.2f}F")

    # ---------------------------------------------------------
    # SECTION 3: import module as alias (style 3) — Luggage Weight
    # ---------------------------------------------------------
    print("\n---- Style 3: import custom_module as uc (Luggage Weight) ----")

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
    print(f"\n(Fun fact: custom_module also exposes a constant, PI = {custom_module.PI}.)")


if __name__ == "__main__":
    main()