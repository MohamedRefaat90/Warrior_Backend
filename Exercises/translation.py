# gym_app/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Exercise,Muscle

class ExerciseTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class MuscleTranslationOptions(TranslationOptions):
    fields = ('name')

translator.register(Exercise, ExerciseTranslationOptions)
translator.register(Muscle, MuscleTranslationOptions)
