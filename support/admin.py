from django.contrib import admin
from .models import Faq, Inquiry, Answer
# Register your models here.

class AnswerInline(admin.StackedInline):
    model = Answer
    
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'writer', 'create_at', 'modify_by', 'modify_at')
    list_filter = ('category',)
    search_fields = ('question')

@admin.register(Inquiry)    
class InquiryAdmin(admin.ModelAdmin):
    # 질문 제목, 카테고리, 생성 일시, 생성자
    list_display = ('question','category','create_at','writer')
    list_filter = ('category',)
    search_fields = ('question', 'email','phone_number')
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('content','create_at','inquiry','writer')
