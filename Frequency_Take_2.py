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
    'temperature' : ['43 degrees']
    },
}
def count_dialogue_frequency(dialogue_dict, target_dialogue):
    frequency = 0
    for dialogue in dialogue_dict.values():
        if target_dialogue.lower() in dialogue.lower():
            frequency += 1
    
    return frequency
dialogue_dict = fetch_dialogue_dict()
if dialogue_dict:
    target_dialogue = input("Enter the dialogue that needs to be found :")
    frequency = count_dialogue_frequency(dialogue_dict, target_dialogue)
    print(f"The dialogue '{target_dialogue}' appears {frequency} times in the dictionary.")
print("\nThe dialogue {target_dialogue} appears {frequency} times in the dictionary.")