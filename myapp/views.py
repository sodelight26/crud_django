from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from myapp.models import STK_USER
from myapp.models import STK_TYPE
from myapp.models import STK_SIZE
from myapp.models import STK_PRD
from myapp.models import STK_ORD
from myapp.models import STK_ORDD
from myapp.models import STK_ADDP
from myapp.models import STK_ADDPD

from .models import STK_CUS, STK_PRD, STK_TYPE, STK_SIZE
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#---ข้อมูลPRD---
def index(request):
    all_STK_PRD = STK_PRD.objects.all()
    return render(request, "index.html", {"all_STK_PRD": all_STK_PRD})

#---แสดงข้อมูลTYPE---
def bs_type(request):
    all_STK_TYPE = STK_TYPE.objects.all()
    return render(request, "bs_type.html", {"all_STK_TYPE": all_STK_TYPE})

def fr_type(request):
   if request.method == "POST":
       # รับข้อมูล
       type_name = request.POST["type_name"]
       # บันทึกข้อมูล
       STK_TYPE.objects.create(TYPE_NAME=type_name)
       # ข้อความตอบกลับ
       messages.success(request, "บันทึกข้อมูลเรียบร้อย")
       # เปลี่ยนเส้นทาง
       return redirect("/bs_type")
   else:
       return render(request, "fr_type.html")
   
csrf_exempt
def ed_type(request, type_id):
    if request.method == "POST":
        type = STK_TYPE.objects.get(id=type_id)
        type.TYPE_NAME = request.POST["type_name"]
        type.save()
        messages.success(request, "อัพเดตข้อมูลเรียบร้อย")
        return redirect("/bs_type")
    else:
        # ดึงข้อมูลประเภท
        type = STK_TYPE.objects.get(id=type_id)
        return render(request, "ed_type.html", {"STK_TYPE": type})

csrf_exempt
def de_type(request, type_id):
    type = STK_TYPE.objects.get(id=type_id)
    type.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อย")
    return redirect("/bs_type")
    
#---แสดงข้อมูลSIZE---
def bs_size(request):
    all_STK_SIZE = STK_SIZE.objects.all()
    return render(request, "bs_size.html", {"all_STK_SIZE": all_STK_SIZE})

def fr_size(request):
    if request.method == "POST":
       
       size_name = request.POST["size_name"]

       STK_SIZE.objects.create(SIZE_NAME=size_name)

       messages.success(request, "บันทึกข้อมูลเรียบร้อย")
       return redirect("/bs_size")
    else:
       return render(request, "fr_size.html")

csrf_exempt
def ed_size(request, size_id):
    if request.method == "POST":
       size = STK_SIZE.objects.get(id=size_id)
       size.SIZE_NAME = request.POST["size_name"]
       size.save()
       messages.success(request, "อัพเดตข้อมูลเรียบร้อย")
       return redirect("/bs_size")
    else:
        size = STK_SIZE.objects.get(id=size_id)
        return render(request, "ed_size.html", {"STK_SIZE": size})

csrf_exempt
def de_size(request, size_id):
    size = STK_SIZE.objects.get(id=size_id)
    size.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อย")
    return redirect("/bs_size")
    
#---แสดงข้อมูลPRODUCT---
def bs_product(request):
    all_STK_PRD_BS = STK_PRD.objects.all()
    return render(request, "bs_product.html", {"all_STK_PRD_BS": all_STK_PRD_BS})

def fr_product(request):
    types = STK_TYPE.objects.all()
    sizes = STK_SIZE.objects.all()

    if request.method == "POST":
        prd_name = request.POST["prd_name"]
        type_id = request.POST["type_id"]
        size_id = request.POST["size_id"]
        prd_numb = request.POST.get("prd_numb", None)
        prd_price = request.POST["prd_price"]

        STK_PRD.objects.create(
            PRD_NAME=prd_name,
            TYPE_ID_id=type_id,
            SIZE_ID_id=size_id,
            PRD_NUMB=prd_numb,
            PRD_PRICE=prd_price
        )

        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
        return redirect("/bs_product")
    else:
        return render(request, "fr_product.html", {"types": types, "sizes": sizes})

csrf_exempt
def ed_product(request, product_id):
    if request.method == "POST":
        product = STK_PRD.objects.get(id=product_id)
        product.PRD_NAME = request.POST["prd_name"]
        product.TYPE_ID_id = request.POST["type_id"]
        product.SIZE_ID_id = request.POST["size_id"]
        product.PRD_NUMB = request.POST.get("prd_numb", None)
        product.PRD_PRICE = request.POST["prd_price"]
        product.save()
        messages.success(request, "อัพเดตข้อมูลเรียบร้อย")
        return redirect("/bs_product")
    else:
        product = STK_PRD.objects.get(id=product_id)
        types = STK_TYPE.objects.all()
        sizes = STK_SIZE.objects.all()
        return render(request, "ed_product.html", {"product": product, "types": types, "sizes": sizes})
    
csrf_exempt
def de_product(request, product_id):
    product = STK_PRD.objects.get(id=product_id)
    product.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อย")
    return redirect("/bs_product")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import STK_PRD, STK_ORD, STK_CUS, STK_USER

def bs_sellprd(request):
    if request.method == "POST":
        # รับข้อมูลจากฟอร์มการขายสินค้า
        cus_id = request.POST["cus_id"]
        user_id = request.POST["user_id"]
        ord_sump = request.POST["ord_sump"]
        ord_typesell = request.POST["ord_typesell"]

        # สร้างรายการการขายสินค้าใหม่
        sellprd = STK_ORD.objects.create(
            CUS_ID_id=cus_id,
            USER_ID_id=user_id,
            ORD_SUMP=ord_sump,
            ORD_TYPESELL=ord_typesell
        )

        # ทำการบันทึกรายการการขายสินค้า
        sellprd.save()

        # แสดงข้อความสำเร็จและเปลี่ยนเส้นทางไปยังหน้ารายการสินค้าที่ขาย
        messages.success(request, "บันทึกการขายสินค้าเรียบร้อยแล้ว")
        return redirect("/bs_product")
    else:
        # ดึงข้อมูลสินค้าทั้งหมดและข้อมูลลูกค้าและผู้ใช้งานทั้งหมด
        products = STK_PRD.objects.all()
        customers = STK_CUS.objects.all()
        users = STK_USER.objects.all()

        # คำนวณราคารวมสำหรับแต่ละรายการสินค้า
        for product in products:
            if product.PRD_NUMB is not None and product.PRD_PRICE is not None:
                product.total_price = product.PRD_NUMB * product.PRD_PRICE
            else:
                product.total_price = 0

        return render(request, "bs_sellprd.html", {"products": products, "customers": customers, "users": users})



   
