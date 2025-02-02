import os


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@10.1.49.250/ie"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IMAGE_PATH = "resources/images"
