# person = {'name': 'Alice', 'age':  25}
# message = 'My name is {name} and I am {age} years old.'
# formatted_message = message.format_map(person)
# print(formatted_message)

class Data:
    def __init__(self, value):
        self.value = value
 
data = Data(42)
message = 'The answer is {data.value}.'
formatted_message = message.format_map(vars())
print(formatted_message)