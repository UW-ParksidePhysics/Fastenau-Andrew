# Defined function to convert units
def convert_units(value_to_be_converted, units_of_the_value_to_be_converted_from, units_to_be_converted_to=0):
    if units_of_the_value_to_be_converted_from == "Vol_Con":
        value_in_the_requested_units = value_to_be_converted / 6.75
    elif units_of_the_value_to_be_converted_from == "En_Con":
        value_in_the_requested_units = value_to_be_converted / 0.0735
    elif units_of_the_value_to_be_converted_from == "Blk_Con":
        value_in_the_requested_units = value_to_be_converted * 14710.
    else:
        value_in_the_requested_units = value_to_be_converted
    return value_in_the_requested_units