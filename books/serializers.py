
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'published_year']
        read_only_fields = ['id']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Title cannot be empty."
            )
        return value

    def validate_author(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Author cannot be empty."
            )
        return value

    def validate_published_year(self, value):
        if value < 1 or value > 9999:
            raise serializers.ValidationError(
                "Enter a valid publication year."
            )
        return value
