import random
import typing


PLAYERS: tuple[str, ...] = (
    "Alex",
    "Blair",
    "Charlie",
    "Dylan",
    "Eden",
    "Finley",
    "Morgan",
    "River",
    "Taylor",
    "Jordan",
)

ACTIONS: tuple[str, ...] = (
    "run",
    "eat",
    "sleep",
    "move",
    "swim",
    "climb",
    "grab",
    "use",
    "release",
)


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index = random.randint(0, len(event_list) - 1)
        event = event_list.pop(index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()

    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(event_gen))
    print(f"Built list of 10 events: {ten_events}")

    consumed_ten_events = consume_event(ten_events)
    for current_event in consumed_ten_events:
        print(f"Got event from list: {current_event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
