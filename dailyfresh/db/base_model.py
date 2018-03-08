from django.db import models

# 建立模型基类
class BaseModel(models.Model):
    """抽象模型基类"""

    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    is_delate = models.BooleanField(default=False,verbose_name='删除标记')

    class Meta:
        # 指定这个类是一个抽象模型类
        abstract = True