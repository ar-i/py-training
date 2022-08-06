#!/usr/bin/env python3
# https://codechalleng.es/bites/15/

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()
def enumerate_names_countries():
    count = 1
    for name,country in zip(names,countries):
        print(f"{count}. {name : <11}{country}")
        count += 1
        #print(f"{count}. {name : < 10}{country}")

enumerate_names_countries()
#def enumerate_names_countries():
#    """Outputs:
#       1. Julian     Australia
#       2. Bob        Spain
#       3. PyBites    Global
#       4. Dante      Argentina
#       5. Martin     USA
#       6. Rodolfo    Mexico"""
#    pass
