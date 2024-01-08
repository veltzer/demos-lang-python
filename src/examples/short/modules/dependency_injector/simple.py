import dependency_injector


class UserService:
    """ service class """
    def __init__(self, user_repository):
        self.user_repository = user_repository


class UserRepository:
    """ service class """
    def get_user(self, user_id):
        # Query database
        return {"id": user_id}


class Container(dependency_injector.containers.DeclarativeContainer):  # type: ignore
    """ Container class """

    user_repository = dependency_injector.providers.Factory(UserRepository)  # type: ignore

    user_service = dependency_injector.providers.Factory(  # type: ignore
        UserService,
        user_repository=user_repository,
    )


def main():
    """ How to use everthing """
    container = Container()

    user_service = container.user_service()
    user = user_service.user_repository.get_user(123)
    print(user)


if __name__ == "__main__":
    main()
