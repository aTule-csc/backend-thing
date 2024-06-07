from sqlalchemy.orm import Session
from database import engine
import models

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)


with Session(bind=engine) as session:
    sur1=models.Survey(name="опрос1")

    que1=models.Question(question="Сколько?",option1 = '65',option2 = '20', option3='немало',surveys=sur1)
    session.add_all([sur1,que1])
    session.commit()