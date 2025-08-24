def test_create_task(client):
    response = client.post(
        "/",
        json={
            "name": "Task Creation",
            "description": "Task Creation description",
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Task Creation"
    assert data["description"] == "Task Creation description"
    assert data["status"] == "created"
    assert "id" in data


def test_get_tasks(client):
    client.post(
        "/",
        json={
            "name": "Tasks Getting",
            "description": "Tasks Getting description",
        }
    )
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_get_task(client):
    client.post(
        "/",
        json={
            "name": "Task Getting",
            "description": "Task Getting description",
        }
    )
    response = client.get("/1/")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Task Getting"
    assert data["description"] == "Task Getting description"
    assert data["status"] == "created"


def test_update_task(client):
    client.post(
        "/",
        json={
            "name": "Task Updating",
            "description": "Task Updating description",
        }
    )
    client.put(
        "/1/",
        json={
            "status": "completed",
        }
    )
    response = client.get("/1/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "completed"


def test_delete_task(client):
    client.post(
        "/",
        json={
            "name": "Task Deleting",
            "description": "Task Deleting description",
        }
    )
    response = client.delete("/1/")
    assert response.status_code == 200
    response = client.delete("/1/")
    assert response.status_code == 404
    response = client.get("/1/")
    assert response.status_code == 404
