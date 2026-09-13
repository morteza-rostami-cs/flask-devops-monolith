from flask import Flask, request
from api.src.validate import ValidationError

# from typing import Any
from shared.database import GetDb

# bad request input
# def bad_request(message: str):
#     return dict(error=message), 400


type ValidatedUser = dict[str, str]


def parse_user_payload() -> ValidatedUser:
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        raise ValidationError("request body must be a JSON object")

    required = ("username", "email", "password")
    for field in required:
        if field not in data:
            raise ValidationError(f"missing field: {field}")
        if not isinstance(data[field], str):
            raise ValidationError(f"{field} must be a string")

    if not data["username"].strip():
        raise ValidationError("username cannot be empty")
    if not data["email"].strip():
        raise ValidationError("email cannot be empty")
    if not data["password"]:
        raise ValidationError("password cannot be empty")

    return {
        "username": data["username"],
        "email": data["email"],
        "password": data["password"],
    }


def register_users_routes(app: Flask, get_db: GetDb):

    # GET /users
    @app.get("/users")
    def find_all():

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
        with get_db().connection() as conn:
            row = conn.execute(
                """
                SELECT id, username, email
                FROM users
                WHERE id = %s
                """,
                (id,),
            ).fetchone()

        if row is None:
            return {"error": "user not found"}, 404

        return {
            "id": row[0],
            "username": row[1],
            "email": row[2],
        }

    # POST /users
    @app.post("/users")
    def create():
        # validate: throw error or return data
        data = parse_user_payload()

        row = None

        try:
            with get_db().connection() as conn:
                row = conn.execute(
                    """
                    INSERT INTO users (username, email, password)
                    VALUES (%s, %s, %s)
                    RETURNING id, username, email
                    """,
                    (data["username"], data["email"], data["password"]),
                ).fetchone()
        except Exception:
            return dict(error="failed to create user"), 500
        if row is None:
            return dict(error="user was not created"), 500

        return {
            "id": row[0],
            "username": row[1],
            "email": row[2],
        }, 201

    # PUT /users/:id
    @app.put("/users/<int:id>")
    def update(id: int):
        data = parse_user_payload()

        try:
            with get_db().connection() as conn:
                row = conn.execute(
                    """
                    UPDATE users
                    SET username = %s,
                        email = %s,
                        password = %s
                    WHERE id = %s
                    RETURNING id, username, email
                    """,
                    (
                        data["username"].strip(),
                        data["email"].strip(),
                        data["password"],
                        id,
                    ),
                ).fetchone()

        except Exception:
            return {"error": "failed to update user"}, 500

        if row is None:
            return {"error": "user not found"}, 404

        return {
            "id": row[0],
            "username": row[1],
            "email": row[2],
        }

    # DELETE /users/:id
    @app.delete("/users/<int:id>")
    def delete(id: int):
        try:
            with get_db().connection() as conn:
                row = conn.execute(
                    """
                    DELETE FROM users
                    WHERE id = %s
                    RETURNING id
                    """,
                    (id,),
                ).fetchone()

        except Exception:
            return {"error": "failed to delete user"}, 500

        if row is None:
            return {"error": "user not found"}, 404

        return {"message": "user deleted"}
