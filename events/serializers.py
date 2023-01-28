from rest_framework import serializers
from .models import Events, Posts


class LeadSerializer (serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('title', 'details')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('title', 'content')

