from rest_framework import serializers

from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    image = serializers.ImageField()

    class Meta:
        model = Profile
        fields = ('username', 'image',)
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://img.icons8.com/ios-glyphs/90/000000/name.png'
