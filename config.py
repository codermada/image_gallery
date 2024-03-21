class Config:
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='sqlite:///data.db'
    BOOTSTRAP_SERVE_LOCAL=True

config = {
    'devConfig': DevConfig
}