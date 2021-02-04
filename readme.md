In this tutorial we setup a serializer for our
model. Serialization is the process of transforming
data into a format that can be transmitted. In this
case we serialize to JSON, which should be easy to
understand because of its syntactic similarity to
python. rest framework serializers inherit from the
serializers.Serializer class and help us convert
our django models back and forth from a transmissable
form. In this case we will be using JSON. JSON should
be fairly easy to understand because it has the
exact same syntax as a python dictionary.
