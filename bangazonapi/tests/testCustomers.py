from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from bangazonapi.models.customers import Customer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


print("test file loaded------------------------")


class TestCustomers(TestCase):
    # used to get user auth to work
    def setUp(self):
        self.username = 'testuser'
        self.password = 'foobar'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.customer = Customer.objects.create({})
        self.token = Token.objects.create(user=self.user)

    # fetch customer from db to edit

    def test_put_customer_update(self):
        # define a customer to be sent to the API
        updated_customer_info = {
            "first_name": "Foo",
            "last_name": "Bar",
            "address": "123 Foobar St.",
            "city": "New Foo City",
            "zipcode": "12345",
            "phone": "615-123-4567",
            "user": self.user
        }

        #  Use the client to send the request and store the response
        response = self.client.put(
            reverse('customer-update_profile'), updated_customer_info, HTTP_AUTHORIZATION='Token ' + str(self.token)
        )

        # Getting 200 back because we have a success url
        self.assertEqual(response.status_code, 200)

        # Query the table to see if there's one Product Type instance in there. Since we are testing a POST request, we don't need to test whether an HTTP GET works. So, we just use the ORM to see if the thing we saved is in the db.
        self.assertEqual(Customer.objects.count(), 1)

        # And see if it's the one we just added by checking one of the properties. Here, name.
        self.assertEqual(Customer.objects.get().first_name, 'Foo')

    # def test_get_product_type(self):
    #     new_product_type = Customer.objects.create(
    #       name="Sporting Goods"
    #     )

    #     # Now we can grab all the product types (meaning the one we just created) from the db
    #     response = self.client.get(reverse('customers-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))

    #     # Check that the response is 200 OK.
    #     # This is checking for the GET request result, not the POST. We already checked that POST works in the previous test!
    #     self.assertEqual(response.status_code, 200)

    #     # response.data is the python serialised data used to render the JSON, while response.content is the JSON itself.
    #     # Are we responding with the data we asked for? There's just one product type in our dummy db, so it should contain a list with one instance in it
    #     self.assertEqual(len(response.data), 1)

    #     # test the contents of the data before it's serialized into JSON
    #     self.assertEqual(response.data[0]["name"], "Sporting Goods")

    #     # Finally, test the actual rendered content as the client would receive it.
    #     # .encode converts from unicode to utf-8. Don't get hung up on this. It's just how we can compare apples to apples
    #     self.assertIn(new_product_type.name.encode(), response.content)


if __name__ == '__main__':
    unittest.main()
