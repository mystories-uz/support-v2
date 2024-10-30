from django.db.models import (
    BigIntegerField,
    BooleanField,
    CharField,
    TextField,
    ForeignKey,
    CASCADE,
    DateField,
    IntegerField,
)
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Messages(AbstractBaseModel):
    user = ForeignKey(
        "BotUsers",
        on_delete=CASCADE,
        verbose_name=_("Foydalanuvchi"),
    )
    chat_id = BigIntegerField(verbose_name=_("Chat ID"))
    message_id = BigIntegerField(verbose_name=_("Message ID"))
    text = TextField(
        null=True,
        blank=True,
        verbose_name=_("Xabar"),
    )
    is_answered = BooleanField(default=False, verbose_name=_("Javob berildimi"))

    class Meta:
        db_table = "messages"
        verbose_name = _("Xabar")
        verbose_name_plural = _("Xabarlar")


class Answer(AbstractBaseModel):
    message = ForeignKey(Messages, on_delete=CASCADE, verbose_name=_("Xabar"))
    text = CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Javob"),
    )

    def __str__(self) -> str:
        return f"{self.created_at} - {self.text}"

    class Meta:
        db_table = "answers"
        verbose_name = _("Javob")
        verbose_name_plural = _("Javoblar")


class DailyMessages(AbstractBaseModel):
    user = ForeignKey(
        "BotUsers",
        on_delete=CASCADE,
        verbose_name=_("Foydalanuvchi"),
    )
    message_date = DateField(verbose_name=_("Xabarlar sanasi"))
    message_count = IntegerField(verbose_name=_("Xabarlar soni"))

    def __str__(self) -> str:
        return f"{self.created_at} - {self.message_date}"

    class Meta:
        db_table = "daily_messages"
        verbose_name = _("Kunlik xabarlar")
        verbose_name_plural = _("Kunlik xabarlar")
