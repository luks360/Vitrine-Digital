from django.contrib.auth.models import User
from django.test import TestCase

from apps.main.models import Stores


class MainTestBase(TestCase):
    def setUp(self) -> None:
        user = self.make_user()
        stores = self.make_store()
        # stores_id = self.make_store_id()
        return super().setUp()

    def make_user(
        self,
        first_name="user1",
        last_name="name1",
        username="username1",
        password="1234561",
        email="username@email.com1",
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_store(
        self,
        cnpj="423535",
        corporate_name="exemplo",
        email="exemplo@gmail.com",
        password="434242",
        contact="42342",
        segment="Alimentação",
        logo="logo/",
    ):
        return Stores.objects.create(
            cnpj=cnpj,
            corporate_name=corporate_name,
            email=email,
            password=password,
            contact=contact,
            segment=segment,
            logo=logo,
        )

    # def make_store_id(
    #     self,
    #     id = '36109a98-8c82-4589-8806-09efcd835bd3'
    # ):
    #     return Stores.objects.filter(
    #         id=id
    #     )
