from api.s3.service import S3Service


service = S3Service()


def get_s3_service():
    return service
