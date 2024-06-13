from django.utils.timezone import now
from rest_framework import serializers
from imdb_app.models import WatchList,StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"
    

class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    # days_since_joined = serializers.SerializerMethodField()
  

    class Meta:
        model = WatchList
        fields = "__all__"
        
        # fields = ['id', 'name','description','active']
        # exclude = ['description']
    #     read_only_fields = ['name']
        
    # def get_len_name(self, object):
    #     length = len(object.name)
    #     return length
    # def get_days_since_joined(self, obj):
    #     return (now() - obj.date_joined).days 
        
 # Validators
    # def name_length(value):
    #     if len(value) < 4:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value
        
        

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(max_length = 100, validators=[name_length])
#     description  = serializers.CharField(max_length = 200)
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active  = validated_data.get('active ', instance.active)
#         instance.save()
#         return instance
    
    # Validation
    
    # Object-level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     return data
        
   
    # Field-level validation
    # def validate_name(self, value):
        
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value
        
   
    
    
  

    