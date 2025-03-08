from sqlalchemy import func, desc
from src.model.configs.connection import DbConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
    def insert(self, subscriber_infos:any) -> None:
        with DbConnectionHandler() as db:
            try:
                new_subscriber = Inscritos( 
                                        nome=subscriber_infos.name,
                                        email=subscriber_infos.email,
                                        link=subscriber_infos.link,
                                        evento_id=subscriber_infos.evento_id)
                
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
    
    def select_subscriber(self, email:str, event_id:int) -> Inscritos:
        with DbConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.email == email, Inscritos.evento_id == event_id
                )
                .one_or_none()
            )
            return data
    
    def select_subscribers_by_link(self, link:str, event_id:int) -> list:
        with DbConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.link == link, 
                    Inscritos.evento_id == event_id
                )
                .all()
            )
            return data
    
    def get_ranking(self, event_id:int) -> list:
        with DbConnectionHandler() as db:
            result = (
                db.session
                .query(
                    Inscritos.link,
                    func.count(Inscritos.id).label("total")
                )
                .filter(
                    Inscritos.evento_id == event_id,
                    Inscritos.link.isnot(None)
                )
                .group_by(Inscritos.link)
                .order_by(desc("total"))
                .all()
            )
            return result