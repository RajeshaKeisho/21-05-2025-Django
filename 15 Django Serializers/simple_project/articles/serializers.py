from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField(read_only=True)


    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('conntet', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
    



