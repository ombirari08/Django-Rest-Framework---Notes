from rest_framework import serializers
from .models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    # This line shows all comments related to a blog post.
    # It uses the related_name='comments' from the Comment model (ForeignKey to Blog).
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

