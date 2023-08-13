from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index, name="index"),
    #ข้อมูลพื้นฐาน type
    path('bs_type',views.bs_type, name="bs_type"),
    path('fr_type',views.fr_type, name="fr_type"),
    path('ed_type/<int:type_id>', views.ed_type, name='ed_type'),
    path('de_type/<int:type_id>', views.de_type, name='de_type'),
    #ข้อมูลพื้นฐาน size
    path('bs_size',views.bs_size, name="bs_size"),
    path('fr_size',views.fr_size, name="fr_size"),
    path('ed_size/<int:size_id>', views.ed_size, name='ed_size'),
    path('de_size/<int:size_id>', views.de_size, name='de_size'),
    #ข้อมูลพื้นฐาน product
    path('bs_product',views.bs_product, name="bs_product"),
    path('fr_product',views.fr_product, name="fr_product"),
    path('ed_product/<int:product_id>', views.ed_product, name='ed_product'),
    path('de_product/<int:product_id>', views.de_product, name='de_product'),
    #หน้าขายสินค้า
    path('bs_sellprd',views.bs_sellprd, name="bs_sellprd"),

]
