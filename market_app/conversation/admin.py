from django.contrib import admin

from .models import Conversation,ConversationMessage

# Register your models here.

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass


@admin.register(ConversationMessage)
class ConversationMessagesAdmin(admin.ModelAdmin):
    pass