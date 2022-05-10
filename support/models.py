from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


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
    
class Inquiry(models.Model):
    
    cat_choices =[
        ("0", "normal")
        ,("1", "account")
        ,("2", "etc")
    ]
# 질문 제목, 카테고리, 생성 일시, 생성자, 이메일, 전화번호
    question = models.CharField(max_length=200, verbose_name="질문")
    category = models.CharField(max_length=1, choices=cat_choices, default="0")
    create_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True)
    writer = models.ForeignKey(to=User, verbose_name="생성자", on_delete=models.CASCADE, related_name='inquiry_writer')
    email = models.EmailField(verbose_name="이메일")
    phone_number = PhoneNumberField(verbose_name="전화번호", null = True, blank = True)
    
    
class Answer(models.Model):
#    1:1문의 모델에 인라인모델로 추가
    inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, verbose_name="생성자", on_delete=models.CASCADE, related_name='answer_writer')
    content = models.TextField(verbose_name="답변")
    create_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True)


