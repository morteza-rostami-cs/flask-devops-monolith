from flask import Flask, request

# from typing import Any
from shared.database import GetDb


def register_users_routes(app: Flask, get_db: GetDb):

    # GET /users
    @app.get("/users")
    def findAll():

        with get_db().connection() as conn:
            rows = conn.execute("""
                select id, username, email
                from users
                order by id
            """).fetchall()

        return [
            {
                "id": row[0],
                "username": row[1],
                "email": row[2],
            }
            for row in rows
        ]

    # GET /users/:id
    @app.get("/users/<int:id>")
    def find(id: int):
        return dict(message="find user", id=id)

    # POST /users
    @app.post("/users")
    def create():
        # request body
        data = request.get_json()
        row = None

        with get_db().connection() as conn:
            row = conn.execute(
                """
                INSERT INTO users (username, email, password)
                VALUES (%s, %s, %s)
                RETURNING id, username, email
                """,
                (data["username"], data["email"], data["password"]),
            ).fetchone()

        if not row:
            return dict(message="no user returned")

        return {
            "id": row[0],
            "username": row[1],
            "email": row[2],
        }, 201

    # PUT /users/:id
    @app.put("/users/<int:id>")
    def update(id: int):
        return dict(message="update user", id=id)

    # DELETE /users/:id
    @app.delete("/users/<int:id>")
    def delete(id: int):
        return dict(message="delete user", id=id)
