from jinja2 import Environment, FileSystemLoader, Template



#name of the folder where index file is located.
file_loader = FileSystemLoader('templates')

#This object is needed to create a template object.
env = Environment(loader=file_loader)

#path of the HTML file reletive to the folder.
template = env.get_template('base.html')

#Data dictionary to be supplied to our HTML file.
input_dict = {
    'otp': '12313ASDSA4'}

#This function renders the data substituted HTML form.
output = template.render(input_dict)
print(output)
