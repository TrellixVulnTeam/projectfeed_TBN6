import os

AWS_ACCESS_KEY_ID = 'AKIAIDWPMVTTLNVE5W6A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'projectfeed3'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'projectfeed/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'