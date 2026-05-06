def test_get_activities_returns_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_existing_activity_success(client):
    email = "new.student@mergington.edu"
    activity_name = "Chess Club"

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email in participants


def test_signup_non_existent_activity_returns_404(client):
    response = client.post("/activities/NonExistent/signup", params={"email": "test@mergington.edu"})

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
