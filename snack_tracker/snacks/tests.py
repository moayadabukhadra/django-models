from urllib import request, response
from django.test import TestCase
from django.urls import reverse

from snacks.models import Snack

class SnackTest(TestCase):

    def test_snack_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Snack")
    
    def test_list_page_status_code(self):
        url = reverse("snacks_list")
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_snack_detail_view(self):
    #     snack = Snack.objects.create(name="Test Snack", description="A test snack")
    #     url = reverse("snack_detail", kwargs={"pk": snack.pk})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Test Snack")
    #     self.assertContains(response, "A test snack")
    
    # def test_detail_page_status_code(self):
    #     url = reverse("snack_detail", kwargs={"pk": 1})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

  


    
    


    
    