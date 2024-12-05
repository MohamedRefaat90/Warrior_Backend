from rest_framework import serializers

from Exercises.models import Exercise
from User.models import Users
from .models.workout_item import WorkoutItem  
from .models.workout_set import WorkoutSet



class WorkoutItemSerializer(serializers.ModelSerializer):
    exercise_id = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all(), source='exercise')
    
    class Meta:
        model = WorkoutItem
        fields = ['exercise_id', 'last_weight', 'equipment_type']

    def validate(self, data):
        # exercise = data['exercise']
        equipment_type = data['equipment_type']
        last_weight = data['last_weight']

        # Validate last_weight based on equipment type and the exercise's allowed weights
        if equipment_type == 'free_weight':
            allowed_weights = WorkoutItem.FREE_WEIGHTS
            if last_weight not in allowed_weights:
                raise serializers.ValidationError({
                    'last_weight': f"Invalid weight for free weights. Allowed weights are: {allowed_weights}"
                })
                
        elif equipment_type == 'machine':
            allowed_weights = WorkoutItem.MACHINE_WEIGHTS
            if last_weight not in allowed_weights:
                raise serializers.ValidationError({
                    'last_weight': f"Invalid weight for machine. Allowed weights are: {allowed_weights}"
                })

        return data
    
    
class WorkoutSetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all()) 
    workout_items = WorkoutItemSerializer(many=True)
    
    class Meta:
        model = WorkoutSet
        fields = '__all__'
        
    def create(self, validated_data):
        workout_items_data = validated_data.pop('workout_items')
        workout_set = WorkoutSet.objects.create(**validated_data)
        
        # Create each WorkoutItem for the WorkoutSet
        for item_data in workout_items_data:
            WorkoutItem.objects.create(workout_set=workout_set, **item_data)
        
        return workout_set
        
