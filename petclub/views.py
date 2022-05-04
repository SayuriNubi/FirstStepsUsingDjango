# modulos de DRF
import email
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)
from .models import (
    Person,
    Pet,
)

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hola, estoy en el get", status=200) # respuesta del servicio
    
    def patch(self, request):
        return Response(data="Hola, estoy en el patch", status=200)

    def delete(self, request):
        return Response(data="Hola, estoy en el delete", status=200)

    def post(self, request):
        return Response(data="Hola, estoy en el post", status=200)

class PetListAPIView(ListAPIView):
    def get(self, request):
        return Response(data="Hola a todos estas son mis mascotas", status=200)

class PetAPIView(RetrieveAPIView):
    def get(self,request):
        return Response(data="Hola, estoy en el get del petview", status=200)

class HelloWorldRetrieve(RetrieveAPIView):
    pass 



class personAPIView(APIView):
    def get(self, request):
        persons = Person.objects.all().values()

        return Response({'data': persons}, status=200)


    def post(self, request):
        data = request.data
        if 'email' not in data.keys() or 'first_name' not in data.keys() or 'last_name' not in data.keys() or 'rut' not in data.keys():
            return Response({'error': 'Some data is wrong'})

        new_person = Person(email = data['email'], first_name = data['first_name'], last_name = data['last_name'], rut = data['rut']) #Creating new person
        new_person.save()

        person_dict = new_person.__dict__
        person_dict.pop('_state')

        return Response({'data': person_dict}, status=201)


    def patch(self, request):
        data = request.data
        if 'id' not in data.keys() or 'email' not in data.keys() or 'first_name' not in data.keys() or 'last_name' not in data.keys() or 'rut' not in data.keys():
            return Response({'error': 'Some data is wrong'}) 

        id = data['id']
        try: 
            person = Person.objects.get(id = id)
            person.email = data['email']
            person.first_name = data['first_name']
            person.last_name = data['last_name']
            person.rut = data['rut']

            person.save()

            person_dict = person.__dict__
            person_dict.pop('_state')

            return Response({'data': person_dict}, status=201)

        except Exception as e:
            print(e)

            return Response({'error': f'This ID does not belong to any person: {id}'}, status=400)

    def delete(self, request):
        data = request.data
        if 'id' not in data.keys():
            return Response({'error': f'This ID does not belong to any person: {id}'}, status=400)

        id = data['id']
        person = Person.objects.get(id=id)
        person.delete()

        return Response({'Sucess': f'The person with that ID has been deleted: {id}'}, status=200)




class petAPIView(APIView):
    def get(self, request):
        pets = Pet.objects.all().values()

        return Response({'data': pets}, status=200)


    def post(self, request):
        data = request.data
        if 'species' not in data.keys() or 'name' not in data.keys() or 'age' not in data.keys() or 'color' not in data.keys():
            return Response({'error': 'Some data is wrong'})

        new_pet = Pet(species = data['species'], name = data['name'], age = data['age'], color = data['color']) #Creating new person
        new_pet.save()

        pet_dict = new_pet.__dict__
        pet_dict.pop('_state')

        return Response({'data': pet_dict}, status=201)


    def patch(self, request):
        data = request.data
        if 'id' not in data.keys() or 'species' not in data.keys() or 'name' not in data.keys() or 'age' not in data.keys() or 'color' not in data.keys():
            return Response({'error': 'Some data is wrong'}) 

        id = data['id']
        try: 
            pet = Pet.objects.get(id = id)
            pet.species = data['species']
            pet.name = data['name']
            pet.age = data['age']
            pet.color = data['color']

            pet.save()

            pet_dict = pet.__dict__
            pet_dict.pop('_state')

            return Response({'data': pet_dict}, status=201)

        except Exception as e:
            print(e)

            return Response({'error': f'This ID does not belong to any pet: {id}'}, status=400)

    def delete(self, request):
        data = request.data
        if 'id' not in data.keys():
            return Response({'error': f'This ID does not belong to any pet: {id}'}, status=400)

        id = data['id']
        pet = Pet.objects.get(id=id)
        pet.delete()

        return Response({'Sucess': f'The pet with that ID has been deleted: {id}'}, status=200)