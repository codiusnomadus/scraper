from django.db import models

# Create your models here.
class CustomerRecord(models.Model):
  timestamp = models.DateTimeField()
  staff_msa_id = models.TextField()
  store_name = models.TextField()
  customers_name = models.TextField()
  device_make_model = models.TextField()
  imei_number = models.TextField()
  phone_bundle_product = models.TextField()
  phone_freedom_365 = models.TextField()
  digi_pf365_postpaid_190 = models.CharField(max_length=600)
  digi_pf365_postpaid_120 = models.CharField(max_length=600)
  digi_pf365_postpaid_80 = models.CharField(max_length=600)
  digi_phone_bundle = models.TextField()
  digi_pb_postpaid_190 = models.CharField(max_length=600)
  digi_pb_postpaid_160 = models.CharField(max_length=600)
  digi_pb_postpaid_120 = models.CharField(max_length=600)
  digi_pb_postpaid_80 = models.CharField(max_length=600)
  agreement_1 = models.TextField()
  agreement_2 = models.TextField()