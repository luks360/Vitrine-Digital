import requests
from django.urls import reverse
from test_main_base import MainTestBase


class MainUrlsTest(MainTestBase):
    def tearDown(self):
        return super().tearDown()

    def test_home_urls(self):
        url = reverse("main:home")
        self.assertEqual(url, "/")

    def test_requests_company_urls(self):
        url = reverse("company:requests-company")
        self.assertEqual(url, "/requests")

    def test_dashboard_urls(self):
        url = reverse("company:dashboard-company")
        self.assertEqual(url, "/dashboard")

    def test_redirect_login_urls(self):
        response = self.client.post(reverse("main:register"))
        self.assertEqual(response.status_code, 200)

    def test_login_urls(self):
        url = reverse("main:login")
        self.assertEqual(url, "/login")

    def test_shops_urls(self):
        url = reverse("main:shops", kwargs={"segment": "Alimentacao"})
        self.assertEqual(url, "/shops/Alimentacao")

    def test_about_urls(self):
        url = reverse("main:about")
        self.assertEqual(url, "/about")

    def test_contact_urls(self):
        url = reverse("main:contact")
        self.assertEqual(url, "/contact")

    def test_register_urls(self):
        url = reverse("main:register")
        self.assertEqual(url, "/register")

    def test_store_urls(self):
        url = reverse(
            "main:store", kwargs={"id": "36109a98-8c82-4589-8806-09efcd835bd3"}
        )
        self.assertEqual(url, "/store/36109a98-8c82-4589-8806-09efcd835bd3")

    def test_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("main:home"))
        self.assertEqual(200, response.status_code)

    def test_login_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("main:login"))
        self.assertEqual(200, response.status_code)

    def test_register_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("main:register"))
        self.assertEqual(200, response.status_code)

    def test_dashboard_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("company:dashboard-company"))
        self.assertEqual(200, response.status_code)

    def test_requests_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("company:requests-company"))
        self.assertEqual(200, response.status_code)

    def test_shops_view_return_status_code_200_ok(self):
        response = self.client.get(
            reverse("main:shops", kwargs={"segment": "Alimentacao"})
        )
        self.assertEqual(200, response.status_code)

    def test_about_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("main:about"))
        self.assertEqual(200, response.status_code)

    def test_logout_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("main:logout"))
        self.assertEqual(302, response.status_code)

    def test_contact_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("main:contact"))
        self.assertEqual(200, response.status_code)

    def test_register_store_returns_code_200_ok(self):
        response = self.client.post(
            reverse("main:register"),
            {
                "cnpj": "23432",
                "corporate_name": "alguma coisa",
                "email": "test@example",
                "password": "test",
                "contact": "test@example.com",
                "segment": "teste",
                "logo": "logos/",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_create_users(self):
        self.make_user(
            first_name="user123",
            last_name="name123",
            username="username123",
            password="123456123",
            email="username@email.com123",
        )

        pass

    def test_store_view_return_status_code_200_ok(self):
        response = requests.get(
            "http://127.0.0.1:8000/store/81cf826b-2277-4f53-963b-75c81db216f5"
        )
        assert response.status_code == 200
