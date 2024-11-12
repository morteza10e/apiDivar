from rest_framework import serializers

from app.models import User, Post, PostLike, PostComment, UserFollow


class UserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            # bio=validated_data['bio'],
            # is_staff=validated_data['is_staff'],
            # is_active=validated_data['is_active'],
            # is_superuser=validated_data['is_superuser'],
        )


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # title = serializers.CharField()
    # description = serializers.CharField()
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault)


    # def update(self, validated_data):
    #     print(validated_data)
    #     if self.user == validated_data['user']:
    #         return super().update(**validated_data)




class PostLikeSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = PostLike
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'

    # def save(self, **kwargs):
    #     print(kwargs)
    #     self.post = kwargs["post"]
    #     return super().save(**kwargs)


class UserFollowSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # follow_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserFollow
        fields = '__all__'
