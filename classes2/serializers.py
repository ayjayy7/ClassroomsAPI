from rest_framework import serializers

from classes.models import Classroom


# List view API
class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'year', 'teacher',]

# detail view API

class ClassroomDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'


class ClassroomUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'subject', 'year', 'teacher']

