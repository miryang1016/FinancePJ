from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

class ArticleListSerializer(serializers.ModelSerializer):
    class userSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    author = userSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ('pk', 'title', 'content', 'author', 'created_at', 'updated_at')

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('author',)
        

class CommentListSerializer(serializers.ModelSerializer):
    class userSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    user = userSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'article', 'comment', 'created_at')
        read_only_fields = ('user',)
