from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Faq(models.Model):
    
    cat_choices =[
        ("0", "normal")
        ,("1", "account")
        ,("2", "etc")
    ]
    
    #질문, 카테고리, 답변, 생성자, 생성일시, 최종 수정자, 최종 수정일시
    question = models.CharField(max_length=200, verbose_name="질문")
    category = models.CharField(max_length=1, choices=cat_choices, default="0")
    comment = models.TextField(verbose_name="답변")
    writer = models.ForeignKey(to=User, verbose_name="생성자", on_delete=models.CASCADE, related_name='faq_writer')
    create_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True)
    modify_by = models.ForeignKey(to=User, verbose_name="최종수정자", on_delete=models.CASCADE, related_name='faq_modify_by')
    modify_at = models.DateTimeField(verbose_name="최종수정일시", null=True, blank=True)