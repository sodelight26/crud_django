from django.db import models
from django.core.exceptions import ValidationError

class STK_USER(models.Model):
    USER_NAME = models.CharField(max_length=100)
    USER_EMAIL = models.EmailField(unique=True)
    USER_PASS = models.CharField(max_length=128)
    USER_DAT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.USER_NAME

class STK_CUS(models.Model):
    CUS_NAME = models.CharField(max_length=100)
    CUS_ADR = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.CUS_NAME}, {self.CUS_ADR}"

class STK_TYPE(models.Model):
    TYPE_NAME = models.CharField(max_length=100)

    def __str__(self):
        return "ชื่อ: " + self.TYPE_NAME

class STK_SIZE(models.Model):
    SIZE_NAME = models.CharField(max_length=100)

    def __str__(self):
        return "ชื่อ: " + self.SIZE_NAME

class STK_PRD(models.Model):
    PRD_NAME = models.CharField(max_length=100)
    TYPE_ID = models.ForeignKey(STK_TYPE, on_delete=models.CASCADE)
    SIZE_ID = models.ForeignKey(STK_SIZE, on_delete=models.CASCADE)
    PRD_NUMB = models.IntegerField(null=True)
    PRD_PRICE = models.FloatField()

    class Meta:
        unique_together = ['PRD_NAME', 'TYPE_ID', 'SIZE_ID']

    def clean(self):
        if self.PRD_NUMB and self.PRD_NUMB < 0:
            raise ValidationError("จำนวนคงเหลือต้องเป็นจำนวนเต็มบวก")
        if self.PRD_PRICE < 0:
            raise ValidationError("ราคาขายต้องเป็นจำนวนบวก")

    def __str__(self):
        return f"{self.PRD_NAME}, {self.TYPE_ID}, {self.SIZE_ID}, {self.PRD_NUMB}, {self.PRD_PRICE}"

class STK_ORD(models.Model):
    CUS_ID = models.ForeignKey(STK_CUS, on_delete=models.CASCADE)
    USER_ID = models.ForeignKey(STK_USER, on_delete=models.CASCADE)
    ORD_DAT = models.DateTimeField(auto_now_add=True)
    ORD_SUMP = models.FloatField()
    ORD_TYPESELL = models.CharField(max_length=20)
    def __str__(self):
            return f"Order #{self.pk}"
    
class STK_ORDD(models.Model):
    ORD_ID = models.ForeignKey(STK_ORD, on_delete=models.CASCADE)
    PRD_ID = models.ForeignKey(STK_PRD, on_delete=models.CASCADE)
    ORDD_NUM = models.IntegerField()
    ORDD_PRICE = models.FloatField()

    def __str__(self):
        return f"Order Detail #{self.pk}"

class STK_ADDP(models.Model):
    PRD_ID = models.ForeignKey(STK_PRD, on_delete=models.CASCADE)
    ADDP_MK = models.CharField(max_length=155)
    ADDP_DAT = models.DateTimeField(auto_now_add=True)
    ADDP_SUMP = models.FloatField()

    def __str__(self):
        return f"{self.PRD_ID}, {self.ADDP_MK}, {self.ADDP_DAT}, {self.ADDP_SUMP}"

class STK_ADDPD(models.Model):
    ADDP_ID = models.ForeignKey(STK_ADDP, on_delete=models.CASCADE)
    PRD_ID = models.ForeignKey(STK_PRD, on_delete=models.CASCADE)
    ADDPD_NUM = models.IntegerField()
    
