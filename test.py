
from granoclient import Grano

client = Grano(api_key='7a8badec6052a81d5')
project = client.get('openinterests')
for schema in project.schemata:
    #if schema.name == 'person':
    #    schema.label = 'Natural person'
    #    schema.save()
    print schema.label

#print project.label

#print list(client.projects)

#data = {'slug': 'foo', 'label': 'The Foo Project'}
#p = client.projects.create(data)
#p = client.get('foo')
#p.label = 'The better Foo Project'
#p.save()
#print p, p.label

for entity in project.entities:
    print entity
