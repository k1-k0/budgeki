import models
from database import engine


print("Create db models")
models.Base.metadata.create_all(engine)