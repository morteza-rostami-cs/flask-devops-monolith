from flask import Flask


def register_users_routes(app: Flask):

    # GET /users
    @app.get("/users")
    def findAll():
        return [{"name": "ali"}]

    # GET /users/:id
    @app.get("/users/<int:id>")
    def find(id: int):
        return dict(message="find user", id=id)

    # POST /users
    @app.post("/users")
    def create():
        return dict(message="create user")

    # PUT /users/:id
    @app.put("/users/<int:id>")
    def update(id: int):
        return dict(message="update user", id=id)

    # DELETE /users/:id
    @app.delete("/users/<int:id>")
    def delete(id: int):
        return dict(message="delete user", id=id)
