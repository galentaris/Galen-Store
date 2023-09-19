from django.test import TestCase, Client
from main.models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    #Penambahan testing diluar tutorial
    def setUp(self):
        Product.objects.create(
            name = 'Kinder Joy', 
            price = 10000, 
            amount = 1, 
            description = 'Makanan kesukaan Galasky',
        )

        Product.objects.create(
            name = 'Green Tea', 
            price = '20000', 
            amount = 5, 
            description = 'Minuman kesukaan owner',      
        )

    def test_item_1(self):
        kinder_joy = Product.objects.get(name='Kinder Joy')
        self.assertEqual(kinder_joy.name, 'Kinder Joy')
        self.assertEqual(kinder_joy.price, 10000)
        self.assertEqual(kinder_joy.amount, 1)
        self.assertEqual(kinder_joy.description, 'Makanan kesukaan Galasky')

    def test_item_2(self):
        green_tea = Product.objects.get(name='Green Tea')
        self.assertEqual(green_tea.name, 'Green Tea')
        self.assertEqual(green_tea.price, 20000)
        self.assertEqual(green_tea.amount, 5)
        self.assertEqual(green_tea.description, 'Minuman kesukaan owner')