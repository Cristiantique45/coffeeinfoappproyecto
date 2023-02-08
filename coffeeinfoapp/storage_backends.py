from storages.backends.s3boto3 import S3Boto3Storage

#permite subir todos los archivos a 'aws' y poder guardarlos
class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'private'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'private'
    file_overwrite = False