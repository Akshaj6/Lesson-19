SPCMcountry_code = {'India' : '0091',
                    'Australia' : '0095',
                    'Nepal' : '0086',
                    'Japan' : '0052',
                    'Canada' : '0023',
                    'South Korea' : '0045'}
print("Country code for India - ")
print(SPCMcountry_code.get('India', 'Not Found'))
print("Country code for US - ", end= SPCMcountry_code.get('US', 'Not Found'))