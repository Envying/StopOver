from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from user.models import Account

from django.utils import timezone
import datetime

# Create your tests here.

# Test for database models

class UserDataBaseTest(TestCase):

	# Set up dummy user object
	def setUp(self):
		User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='TEST01',
							first_name='Stop', last_name='Over', email='stopover@gmail.com', is_staff=False,
							is_active=False, date_joined=timezone.now())

		user = User.objects.get(id=1)

		self.testuser = User.objects.create(username="teststop@email.com")
		self.testuser.set_password("whatisthepassword")
		self.testuser.save()


	# Test for content within created dummy object
	def test_user_content(self):
		user = User.objects.get(id=1)
		account = Account.objects.get(user_id=user.id)
		expected_password = user.password
		expected_last_login = user.last_login
		expected_is_superuser = user.is_superuser
		expected_username = user.username
		expected_first_name = user.first_name
		expected_last_name = user.last_name
		expected_email = user.email
		expected_is_staff = user.is_staff
		expected_is_active = user.is_active
		expected_date_joined = user.date_joined
		expected_book_status = account.book_status

		self.assertEquals(expected_password, 'test123')
		self.assertIsInstance(expected_last_login, datetime.date)
		self.assertEquals(expected_is_superuser, False)
		self.assertEquals(expected_username, 'TEST01')
		self.assertEquals(expected_first_name, 'Stop')
		self.assertEquals(expected_last_name, 'Over')
		self.assertEquals(expected_email, 'stopover@gmail.com')
		self.assertEquals(expected_is_staff, False)
		self.assertEquals(expected_is_active, False)
		self.assertIsInstance(expected_date_joined, datetime.date)
		self.assertEquals(expected_book_status, False)

	# Test if the length of password is less than 128 characters
	def test_password_length(self):
		# Get User of id 1
		user = User.objects.get(id=1)

		# If length is less than 128 pass true
		if len(user.password) <= 128:
			self.assertTrue(True, "Old password is less than 128 characters")
		else:
			self.assertTrue(False, "Old password is more than 128 characters")

		# Assign new password exceeding 128 characters
		new_password = 'test' * 45
		User.objects.filter(id=user.id).update(password=new_password)
		user = User.objects.get(id=1)

		# If length is more than 128 pass true
		if len(user.password) >= 128:
			self.assertTrue(True, "New password is more than 128 characters")
		else:
			self.assertTrue(False, "New password is less than 128 characters")

	# Test if the length of username is less than 150 characters
	def test_username_length(self):
		# Get User of id 1
		user = User.objects.get(id=1)

		# If length is less than 150 pass true
		if len(user.username) <= 150:
			self.assertTrue(True, "Old username is less than 150 characters")
		else:
			self.assertTrue(False, "Old username is more than 150 characters")

		# Assign new username exceeding 150 characters
		new_username = 'test' * 45
		User.objects.filter(id=user.id).update(username=new_username)
		user = User.objects.get(id=1)

		# If length is more than 150 pass true
		if len(user.username) >= 150:
			self.assertTrue(True, "New username is more than 150 characters")
		else:
			self.assertTrue(False, "New username is less than 150 characters")

	# Test if the length of first name is less than 30 characters
	def test_first_name_length(self):
		# Get User of id 1
		user = User.objects.get(id=1)

		# If length is less than 30 pass true
		if len(user.first_name) <= 30:
			self.assertTrue(True, "Old first name is less than 30 characters")
		else:
			self.assertTrue(False, "Old first name is more than 30 characters")

		# Assign new first name exceeding 30 characters
		new_first_name = 'test' * 8
		User.objects.filter(id=user.id).update(first_name=new_first_name)
		user = User.objects.get(id=1)

		# If length is more than 30 pass true
		if len(user.first_name) >= 30:
			self.assertTrue(True, "New first name is more than 30 characters")
		else:
			self.assertTrue(False, "New first name is less than 30 characters")

	# Test if the length of last name is less than 150 characters
	def test_last_name_length(self):
		# Get User of id 1
		user = User.objects.get(id=1)

		# If length is less than 150 pass true
		if len(user.last_name) <= 150:
			self.assertTrue(True, "Old last name is less than 150 characters")
		else:
			self.assertTrue(False, "Old last name is more than 150 characters")

		# Assign new last name exceeding 150 characters
		new_last_name = 'test' * 45
		User.objects.filter(id=user.id).update(last_name=new_last_name)
		user = User.objects.get(id=1)

		# If length is more than 150 pass true
		if len(user.last_name) >= 150:
			self.assertTrue(True, "New last name is more than 150 characters")
		else:
			self.assertTrue(False, "New last name is less than 150 characters")

	# Test if the length of email is less than 254 characters
	def test_email_length(self):
		# Get User of id 1
		user = User.objects.get(id=1)

		# If length is less than 254 pass true
		if len(user.email) <= 254:
			self.assertTrue(True, "Old email is less than 254 characters")
		else:
			self.assertTrue(False, "Old email is more than 254 characters")

		# Assign new email exceeding 254 characters
		new_email = 'test' * 70
		User.objects.filter(id=user.id).update(email=new_email)
		user = User.objects.get(id=1)

		# If length is more than 254 pass true
		if len(user.email) >= 254:
			self.assertTrue(True, "New email is more than 254 characters")
		else:
			self.assertTrue(False, "New email is less than 254 characters")


	def test_register_email(self):
		user = User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='wrongemail',
							first_name='Stop', last_name='Over', email='wrongemail', is_staff=False,
							is_active=False, date_joined=timezone.now())
		try:
			user.full_clean()
		except ValidationError as e:
			self.assertFalse('Email' in e.message_dict)


	def test_register_mobile(self):
		user = User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='wrongemail',
							first_name='Stop', last_name='Over', email='wrongemail', is_staff=False,
							is_active=False, date_joined=timezone.now())

		account = Account.objects.get(user_id=user.id)

		account.mobile = "043211A111"
		account.car_license_name = "Full Name"
		account.car_license = "0000000"
		account.street_name = "Required Street"
		account.street_number = "10"
		account.suburb = "Melbourne"
		account.postcode = "3000"
		try:
			account.full_clean()
		except ValidationError as e:
			self.assertFalse('Mobile' in e.message_dict)


	def test_register_car_license_number(self):

		car_user = User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='wrongemail',
							first_name='Stop', last_name='Over', email='wrongemail@email.com', is_staff=False,
							is_active=False, date_joined=timezone.now())
		account = Account.objects.get(user_id=car_user.id)

		account.mobile = "0432111111"
		account.car_license_name = "Full Name"
		account.car_license = "000000A"
		account.street_name = "Required Street"
		account.street_number = "10"
		account.suburb = "Melbourne"
		account.postcode = "3000"

		try:
			account.full_clean()
		except ValidationError as e:
			self.assertFalse('Car license' in e.message_dict)


	def test_register_street_number(self):
		user = User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='wrongemail',
							first_name='Stop', last_name='Over', email='wrongemail', is_staff=False,
							is_active=False, date_joined=timezone.now())

		account = Account.objects.get(user_id=user.id)

		account.mobile = "0432110111"
		account.car_license_name = "Full Name"
		account.car_license = "0000000"
		account.street_name = "Required Street"
		account.street_number = "ABS"
		account.suburb = "Melbourne"
		account.postcode = "3000"
		try:
			account.full_clean()
		except ValidationError as e:
			self.assertFalse('Street Number' in e.message_dict)


	def test_register_street_name(self):
		user = User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='wrongemail',
							first_name='Stop', last_name='Over', email='wrongemail', is_staff=False,
							is_active=False, date_joined=timezone.now())

		account = Account.objects.get(user_id=user.id)

		account.mobile = "0432110111"
		account.car_license_name = "Full Name"
		account.car_license = "0000000"
		account.street_name = "1equired Street"
		account.street_number = "10"
		account.suburb = "Melbourne"
		account.postcode = "3000"
		try:
			account.full_clean()
		except ValidationError as e:
			self.assertFalse('Street name' in e.message_dict)
	#
	def test_register_suburb(self):
		user = User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='wrongemail',
							first_name='Stop', last_name='Over', email='wrongemail', is_staff=False,
							is_active=False, date_joined=timezone.now())

		account = Account.objects.get(user_id=user.id)

		account.mobile = "0432110111"
		account.car_license_name = "Full Name"
		account.car_license = "0000000"
		account.street_name = "Required Street"
		account.street_number = "10"
		account.suburb = "Me0192bourne"
		account.postcode = "3000"
		try:
			account.full_clean()
		except ValidationError as e:
			self.assertFalse('Suburb' in e.message_dict)
	#
	def test_register_postcode(self):
		user = User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='wrongemail',
							first_name='Stop', last_name='Over', email='wrongemail', is_staff=False,
							is_active=False, date_joined=timezone.now())

		account = Account.objects.get(user_id=user.id)

		account.mobile = "0432110111"
		account.car_license_name = "Full Name"
		account.car_license = "0000000"
		account.street_name = "Required Street"
		account.street_number = "10"
		account.suburb = "Melbourne"
		account.postcode = "AB00"
		try:
			account.full_clean()
		except ValidationError as e:
			self.assertFalse('Postcode' in e.message_dict)

	def test_register_clean(self):
		user = User.objects.create(password='test123', last_login=timezone.now(), is_superuser=False, username='wrongemail',
							first_name='Stop', last_name='Over', email='wrongemail', is_staff=False,
							is_active=False, date_joined=timezone.now())

		account = Account.objects.get(user_id=user.id)

		account.mobile = "0432110111"
		account.car_license_name = "Full Name"
		account.car_license = "0000000"
		account.street_name = "Required Street"
		account.street_number = "10"
		account.suburb = "Melbourne"
		account.postcode = "3000"
		try:
			account.full_clean()
		except ValidationError as e:
			self.assertFalse('Mobile' in e.message_dict)


	def user_login_redirect(self):
		self.client.force_login(self.testuser)
		response = self.client.get(reverse('user'))
		self.assertEquals(response.status_code, 302)
