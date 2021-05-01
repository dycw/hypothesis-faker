from hypothesis import settings


settings.register_profile(name="default", deadline=None, print_blob=True)
settings.load_profile("default")
