from users.models import User
from rest_framework import serializers
from .models import Profile, Post, Comment, Category


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.SerializerMethodField()
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:

        model = Post
        fields = ['id', 'title', 'body', 'owner', 'created', 'comments', 'categories']

    def get_created(self, obj):
        return obj.formatted_created()
    

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.SerializerMethodField()
    


    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post', 'created']

    def get_created(self, obj):
        return obj.formatted_created()
    

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']




class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='user-detail')

    class Meta:
        model = Profile
        fields = ['url', 'id', 'user', 'image', 'resume','phone', 'country','email', 'bio', 'education', 'years_of_experience', 'working_experience', 'additional_details', 'Address_Line1', 'Address_Line2', 'state', 'postal_code', 'profession', 'skills', 'working_hours' ]

    

class UserRegistrationSerializer(serializers.ModelSerializer):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)
    phone = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    old_password = serializers.CharField(write_only=True, required=False)
    gender = serializers.ChoiceField(choices=SEX_CHOICES, required=False)
    profile = UserProfileSerializer(read_only=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()


    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password', None)
        phone = data.get('phone', None)
        gender = data.get('gender', None)
        country = data.get('country', None)
        if request_method == 'POST':
            if password == None:
                raise serializers.ValidationError({'info': 'Please Provide your Password'})
        elif request_method == 'PUT' or request_method == 'PATCH':
            old_password = data.get('old_password', None)
            if password != None and old_password == None:
                raise serializers.ValidationError({'info': 'Please provide your old password'})
        if request_method == 'POST':
            if country == None:
                raise serializers.ValidationError({'info': 'Please Provide your country name'})
            if phone == None:
                raise serializers.ValidationError({'info': 'Please Provide your phone number'})
            if gender == None:
                raise serializers.ValidationError({'info': 'Please choose a sex'})
    
        return data


    

    
    def create(self, validated_data):
        
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user   
    
    def get_post_count(self, obj):
        return obj.posts.count()
    

    def get_comment_count(self, obj):
        return obj.comments.count()


    def update(self, instance, validated_data):
        try:
            user = instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                old_password = validated_data.pop('old_password')
                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception('old password is incorrect')
                user.save()
        except Exception as err:
            raise serializers.ValidationError({'info': err})
           
        return super(UserRegistrationSerializer, self).update(instance, validated_data)
    



    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'old_password', 
                  'country', 'gender', 'phone','profile', 'posts', 'post_count','comments','comment_count', 'categories']
