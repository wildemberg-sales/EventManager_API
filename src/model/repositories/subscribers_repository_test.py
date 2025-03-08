import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert_subscriber():
    subscriber_info = {
        "name": "Meu nome",
        "email": "email@gmail.com",
        "evento_id": 2
    }
    
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscribers():
    email = "email@gmail.com"
    event_id = 2
    
    subs_repo = SubscribersRepository()
    res = subs_repo.select_subscriber(email, event_id)
    print(f"Nome => {res.nome}")

@pytest.mark.skip("Link Ranking")
def test_ranking():
    event_id = 2
    subs_repo = SubscribersRepository()
    res = subs_repo.get_ranking(event_id)
    
    print()
    for item in res:
        print(f'Link: {item.link} - Quantidade Inscritos: {item.total}')