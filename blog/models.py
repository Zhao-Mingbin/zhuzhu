from django.db import models
from DjangoUeditor.models import UEditorField
import datetime

# Create your models here.
#氢能资讯
class Article(models.Model):
    name = models.CharField(default='一个帅比',max_length=100, verbose_name='作者')
    title = models.CharField(max_length=100, verbose_name='标题')
    content = UEditorField(width=1200, height=300, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    duration = (datetime.datetime.now()-datetime.datetime(2019,8,3)).days
    class Meta:
        db_table = 'Article'
        verbose_name = '我们的故事'
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.title
#课题组新闻
