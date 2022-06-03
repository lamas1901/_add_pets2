from django.utils.text import slugify
from django.core.files.uploadedfile import UploadedFile
from django.contrib.auth.models import User

from pets.models import Pet, PetType
from json import loads
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR/'json/dogs.json') as f:
	dogs = loads(f.read())
with open(BASE_DIR/'json/cats.json') as f:
	cats = loads(f.read())

cat_pet_type = PetType.objects.get(slug='kedi')
dog_pet_type = PetType.objects.get(slug='kopek')

dog = dogs[0]

for pet in dogs:
	PET = Pet(
		name = pet['name'],
		slug = slugify(pet['name']),
		owner = User.objects.first(),
		price = 0,
		animal_type = dog_pet_type,
		age = int(bool(pet['age'])),
		sex = 'male' if pet['sex']=='Erkek' else 'female',
		breed= pet['breed'],
		city = slugify(pet['city']),
		description = pet['content'],
		special_phone = pet['owner_phone'],
		special_waphone = pet['owner_phone'],
		special_ownername = pet['owner_name']
	)
	PET.save()
	PET.slug=PET.slug+str(PET.id)
	PET.photo.save(
		slugify(pet['name'])+str(PET.id)+'.jpg',
		UploadedFile(
			file=open(BASE_DIR/f'images/{slugify(pet["name"])}.jpg','rb')
		)
	)
	PET.save()

for pet in cats:
	PET = Pet(
		name = pet['name'],
		slug = slugify(pet['name']),
		owner = User.objects.first(),
		price = 0,
		animal_type = dog_pet_type,
		age = int(bool(pet['age'])),
		sex = 'male' if pet['sex']=='Erkek' else 'female',
		breed= pet['breed'],
		city = slugify(pet['city']),
		description = pet['content'],
		special_phone = pet['owner_phone'],
		special_waphone = pet['owner_phone'],
		special_ownername = pet['owner_name']
	)
	PET.save()
	PET.slug=PET.slug+str(PET.id)
	PET.photo.save(
		slugify(pet['name'])+str(PET.id)+'.jpg',
		UploadedFile(
			file=open(BASE_DIR/f'images/{slugify(pet["name"])}.jpg','rb')
		)
	)
	PET.save()