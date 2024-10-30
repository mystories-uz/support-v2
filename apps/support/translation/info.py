from modeltranslation.translator import TranslationOptions, register

from apps.support.models import Info, InfoLinks


@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ("full_name", "info")



@register(InfoLinks)
class InfoLinksTranslationOptions(TranslationOptions):
    fields = ("name",)