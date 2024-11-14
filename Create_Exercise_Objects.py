import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WarriorProject.settings')  # Replace with your project name
django.setup()

# Import your Exercise model
from Exercises.models import Exercise, Muscle

MUSCLE = "Triceps"

# Set the folder path containing the GIFs
gifs_folder = f'B:\Fullstack Projects\Warrior Assets\Exercises\gifs\{MUSCLE}'  # Replace with the actual path

# Specify the exercise type if needed
EXERCISE_TYPE = "strength"

# Loop through each GIF file in the folder
for gif_filename in os.listdir(gifs_folder):
    if gif_filename.endswith(".gif"):
        # Extract the exercise name from the GIF filename, e.g., "bicep_curl.gif" -> "Bicep Curl"
        exercise_name = os.path.splitext(gif_filename)[0].replace('_', ' ').title()

        # Define a default or related Muscle object
        try:
            muscle = Muscle.objects.get(name=MUSCLE)  # Adjust muscle name as appropriate
        except Muscle.DoesNotExist:
            muscle = Muscle.objects.create(name=MUSCLE)

        # Path to the GIF file
        gif_path = os.path.join(f"Exercises\{MUSCLE}", f"gifs\{gif_filename}")

        # Create Exercise object with the GIF path
        exercise = Exercise.objects.create(
            name=exercise_name,
            description="An exercise for building strength.",
            gif= gif_path,  # Stores the path to the GIF
            type=EXERCISE_TYPE,
            muscle=muscle
        )

        print(f"Created Exercise: {exercise.name} with GIF {exercise.gif}")

