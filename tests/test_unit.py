from src.routers.health import get_health


def test_get_health():
    response = get_health()
    assert response["status"] == "OK"
