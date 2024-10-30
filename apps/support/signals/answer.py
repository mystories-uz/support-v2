import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from telebot import TeleBot

from apps.support.models import Answer

bot = TeleBot(os.getenv("BOT_TOKEN"))


@receiver(post_save, sender=Answer)
def post_save_answer(sender, instance, created, **kwargs):
    if created:
        try:
            bot.send_message(
                instance.message.chat_id,
                f"New answer received:\n\n{instance.text}",
                reply_to_message_id=instance.message.message_id,
            )
        except Exception as e:
            print(f"Error sending message: {e}")
        instance.message.is_answered = True
        instance.message.save()
        print(f"New answer created: {instance.text}")
