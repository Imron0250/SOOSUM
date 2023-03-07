from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


@api_view(["GET"])
def get_info_social(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    social_media = Social_media.objects.all()
    social_media_ser = SocialMediaSerializer(social_media, many=True)
    data = {
        "info": info_ser.data,
        "social_media": social_media_ser.data
    }
    return Response(data)

@api_view(['POST'])
def create_order(request):
    name = request.POST.get("name")
    phone = request.POST.get('phone')
    if name and phone is not None:
        if name.isalpha():
            if len(phone) == 13:
                if phone[:4] == "+998":
                    a = phone[4:6]
                    list = ["99", "98", "97", "95", "94", "93", "91", "90", "88", "33"]
                    if a in list:
                        if phone[6:].isdigit():
                            Order.objects.create(name=name, phone=phone)
                            order = Order.objects.last()
                            data = OrderSerializer(order).data
                        else:
                            data = {
                                "error": "Number must include only numbers"
                            }
                    else:
                        data = {
                            "error": "Number company not found"
                        }
                else:
                    data = {
                        "error": "Ex. +998901234567"
                    }
            else:
                data = {
                    "error": "The length of number must be 13"
                }
        else:
            data = {
                "error": "Name must include only letters"
            }
    else:
        data = {
            "error": "Name and number can't be None"
        }
    return Response(data)


@api_view(['GET'])
def get_discount(request):
    discount = Discount.objects.last()
    discount_ser = DiscountSerializer(discount)
    data = {
        "discount" : discount_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_product(request):
    product = Product.objects.all().order_by('-id')[:2]
    product_ser = ProductSerializer(product, many=True)
    data = {
        "data" : product_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_about_product(request):
    about_product = About_Product.objects.all().order_by('-id')[:3]
    about_product_ser = AboutProductSerializer(about_product, many=True)
    data = {
        "data" : about_product_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_about_company(request):
    about = About_Company.objects.last()
    about_ser = AboutCompanySerializer(about)
    data = {
        "data" : about_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_how_use(request):
    how_to_use = HowToUse.objects.last()
    how_to_use_ser = HowToUseSerializer(how_to_use)
    data = {
        "data" : how_to_use_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_fact(request):
    fact = Fact.objects.all()
    fact_ser = FactSerializer(fact, many=True)
    data = {
        "data" : fact_ser.data
    }
    return Response(data)   

@api_view(['GET'])
def get_who_user(request):
    who_user = WhoUser.objects.all()
    who_user_ser = WhoUseSerializer(who_user, many=True)
    data = {
        "data" : who_user_ser.data
    }
    return Response(data)