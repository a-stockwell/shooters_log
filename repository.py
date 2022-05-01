import abc
import app

# Looking at this repository definition it ties everything together on the Athlete class.
# I'm sure there is a way to reuse it for the Runs, but I am going to create a new one for it.
# Not going to change the name of this one cause it's currently working, I think. It's not throwing errors anyway.


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
        # self.session.first_name()

    def get(self, athlete):
        return self.session.query(app.Athlete).filter_by(athlete_id=athlete.athlete_id).one()

    def list(self):
        return self.session.query(app.Athlete).all()


class AbstractRepositoryRun(abc.ABC):
    @abc.abstractmethod
    def add(self, run: app.Run):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> app.Run:
        raise NotImplementedError


class SqlAlchemyRepositoryRun(AbstractRepositoryRun):
    def __init__(self, session):
        self.session = session

    def add(self, run):
        self.session.add(run)

    def get(self, run):
        return self.session.query(app.Run).filter_by(run_id=run.run_id).one()

    def list(self):
        return self.session.query(app.Run).all()
