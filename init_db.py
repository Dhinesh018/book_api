
from db import Base,engine
import models
models.Base.metadata.create_all(bind= engine)