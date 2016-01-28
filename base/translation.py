__author__ = 'orion'
from modeltranslation.translator import translator, TranslationOptions
from models import Flat, FlatPhoto


class FlatTranslationOptions(TranslationOptions):
    fields = ('title', 'district', 'adress', 'description', 'short_description')


class FlatPhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Flat, FlatTranslationOptions)
translator.register(FlatPhoto, FlatPhotoTranslationOptions)