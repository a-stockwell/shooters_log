import abc
import app


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, athlete: app.Athlete):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> app.Athlete:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, athlete):
        self.session.add(athlete)

    def get(self, athlete):
        return self.session.query(app.Athlete).filter_by(athlete_id=athlete.athlete_id).one()

    def list(self):
        return self.session.query(app.Athlete).all()
