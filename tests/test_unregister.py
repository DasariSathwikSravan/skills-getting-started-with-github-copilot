from src.app import activities


def test_unregister_success(client):
    email = "alex@mergington.edu"

    response = client.delete("/activities/Basketball Team/participants", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Basketball Team"}
    assert email not in activities["Basketball Team"]["participants"]


def test_unregister_student_not_signed_up_returns_404(client):
    response = client.delete(
        "/activities/Basketball Team/participants",
        params={"email": "not.registered@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}


def test_unregister_activity_not_found_returns_404(client):
    response = client.delete(
        "/activities/Nonexistent Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
