from rest_framework import serializers

from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def validate(self, attrs):
        content = attrs.get('content', None)
        if content == "":
            content = None

        image = attrs.get('image', None)

        if content is None and image is None:
            raise serializers.ValidationError('content or image is required')
        return attrs

