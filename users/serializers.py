from users.models import User
from rest_framework import serializers
from .models import Profile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='user-detail')

    class Meta:
        model = Profile
        fields = ['url', 'id', 'user', 'image', 'resume','phone', 'country','email', 'bio']
    

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
    sex = serializers.ChoiceField(choices=SEX_CHOICES, required=False)
    profile = UserProfileSerializer(read_only=True)



    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password', None)
        phone = data.get('phone', None)
        sex = data.get('sex', None)
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
                raise serializers.ValidationError({'info': 'Please Provide your cphone number'})
            if sex == None:
                raise serializers.ValidationError({'info': 'Please choose a sex'})
    
        return data


    

    
    def create(self, validated_data):
        
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user   


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
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'old_password', 'country', 'sex', 'phone','profile' ]