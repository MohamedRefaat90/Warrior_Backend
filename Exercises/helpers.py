def upload_gif(instance, filename):
    # Access the related muscle name directly from the `muscle` ForeignKey
    muscle_name = instance.muscle.name if instance.muscle else 'default'
    return f'{muscle_name}/gifs/{filename}'

def upload_video(instance, filename):
    # Get the muscle name from the related Muscle instance if it exists
    muscle_name = instance.muscles.name if instance.muscle else 'default'
    return f'{muscle_name}/videos/{filename}'

