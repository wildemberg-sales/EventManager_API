import pytest
from .eventos_link_repository import EventosLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_events_link():
    event_id = 20
    inscrito_id = 18
    event_link_repo = EventosLinkRepository()
    
    link = event_link_repo.insert(event_id, inscrito_id)
    print(f'\n{link}')

# @pytest.mark.skip("Select in DB")
def test_select_event_link():
    event_id = 20
    inscrito_id = 18
    event_link_repo = EventosLinkRepository()
    
    events_links = event_link_repo.select_events_link(event_id, inscrito_id)
    print(f"{events_links}")
