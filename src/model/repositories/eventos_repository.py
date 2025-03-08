from src.model.configs.connection import DbConnectionHandler
from src.model.entities.eventos import Eventos
from .interfaces.eventos_repository import EventosRepositoryInterface

class EventosRepository(EventosRepositoryInterface):
    def insert(self, event_name:str) -> None:
        with DbConnectionHandler() as db:
            try:
                new_event = Eventos(nome=event_name)
                db.session.add(new_event)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
    
    def select_events(self, event_name:str) -> Eventos:
        with DbConnectionHandler() as db:
            data = (
                db.session
                .query(Eventos)
                .filter(Eventos.nome == event_name)
                .one_or_none()
            )
            return data