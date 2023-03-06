import pytest

@pytest.fixture(scope="function"):
def get_data(request):
    db = connect_to_db()
    query = f"select * from {request.param}"
    result = db.execute(query)
    return result

@pytest.mark.parametrize("get_data", ["user"], indirect=True)
def test_get_user(get_data):
    db_result = get_data
    api_resones = 
