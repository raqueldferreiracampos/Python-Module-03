import typing
import random


def gen_event() -> typing.Generator:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "swim", "move", "climb", "use"]
    while True:
        p_choice = random.choice(players)
        a_choice = random.choice(actions)
        yield(p_choice, a_choice)


def consume_event(events: list) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    generator = gen_event()
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    events = [next(generator) for i in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()