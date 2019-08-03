from django.db import models

# Create your models here.
class STK_Code(models.Model):
    stk_code = models.CharField(max_length=30)
    stk_Desc = models.CharField(max_length=600)

    def __str__(self):
        return str(self.stk_code)

class STK_TrigSent(models.Model):
    stk_code = models.ForeignKey(STK_Code, on_delete=models.CASCADE)
    stk_TrigStat = models.IntegerField(default=0)
    stk_TrigDtTm = models.DateTimeField('DtTm of Change')

    def __str__(self):
        return str(self.stk_TrigStat)

class STK_Sentiment(models.Model):
    stk_code = models.ForeignKey(STK_Code, on_delete=models.CASCADE)
    stk_SentimentInd = models.IntegerField(default=0)
    stk_DtTmofChg = models.DateTimeField('DtTm of Change')

    def __str__(self):
        return str(self.stk_DtTmofChg)
