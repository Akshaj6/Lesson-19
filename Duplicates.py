student_data = {'id1':
    {'name' : ['Sara'],
     'class' : ['V'],
     'subject_intregation' : ['english, maths, science']
    },
    'id2':
    {'name' : ['David'],
     'class' : ['V'],
     'subject_intregation' : ['english, maths, science']
    },
    'id3':
    {'name' : ['Sara'],
     'class' : ['V'],
     'subject_intregation' : ['english, maths, science']
    },
    'id4':
    {'name' : ['Lars'],
     'class' : ['V'],
     'subject_intregation' : ['english, maths, science']
    },
}
result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)