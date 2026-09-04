from core.worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    from .client.launch import launch_wesnoth_client

    launch(launch_wesnoth_client, name="Wesnoth Client", args=args)

    components.append(
        Component(
            "Wesnoth Client",
            func=run_client,
            game_name="Wesnoth",
            component_type=Type.CLIENT,
            supports_uri=True,
        )
    )