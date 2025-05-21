dict = {'Monday':
    {'skies' : ['Covered With Black Clouds'],
    'weather' : ['rainy'],
    'temperature' : ['20 degrees']
    },
    'Tuesday':
    {'skies' : ['As Blue As Can Be'],
    'weather' : ['sunny'],
    'temperature' : ['43 degrees']
    },
    'Wednesday':
    {'skies' : ['Covered With Grey Clouds'],
    'weather' : ['humid, with chances of rain'],
    'temperature' : ['20 degrees']
    },
    'Thursday':
    {'skies' : ['Covered With Black Clouds'],
    'weather' : ['rainy'],
    'temperature' : ['20 degrees']
    },
    'Friday':
    {'skies' : ['Covered With Grey Clouds'],
    'weather' : ['humid, with chances of rain'],
    'temperature' : ['20 degrees']
    },
    'Saturday':
    {'skies' : ['Covered With Grey Clouds'],
    'weather' : ['humid, with chances of rain'],
    'temperature' : ['20 degrees']
    },
    'Sunday':
    {'skies' : ['As Blue As Can Be'],
    'weather' : ['sunny'],
    'temperature' : ['46 degrees']
    },
}
def text_frequency(whole_weather, text_needed):
    text_found = 0
    for day in whole_weather:
        day_info = whole_weather[day]
        for category_name in day_info:
            description = day_info[category_name]
            for description_text in description:
                if description_text == text_needed:
                    text_found = text_found + 1

    return text_found
user = input("What text's frequency do you want to count in the weather report? ")
frequency_count = text_frequency(dict, user)
print(f"The text '{user}' was found {frequency_count} time(s).")