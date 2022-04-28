import abc
import app


class AthleteRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, athlete: app.Athlete):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> app.Athlete:
        raise NotImplementedError


class SqlAlchemyRepository(AthleteRepository):
    def __init__(self, session):
        self.session = session

    # This is what VSCode wanted to add initally
    # def add(self, athlete: app.Athlete):
    #     return super().add(athlete)
    def add(self, athlete):
        self.session.add(athlete)

    def get(self, reference):
        return self.session.query(app.Athlete).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(app.Athlete).all()
