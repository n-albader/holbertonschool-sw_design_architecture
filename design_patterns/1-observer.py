#!/usr/bin/env python3
"""Observer pattern with a news notification system."""


class NewsSubject:
    """Subject that manages news observers."""

    def __init__(self):
        """Initialize the list of observers."""
        self._observers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to specific topics."""
        self._observers.append((observer, topics))

    def unsubscribe(self, observer):
        """Remove an observer."""
        self._observers = [
            item for item in self._observers if item[0] != observer
        ]

    def notify(self, topic, data):
        """Notify observers interested in the given topic."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Observer that logs selected news topics."""

    def update(self, topic, data):
        """Print a log notification."""
        print(f"log:{topic}={data}")


class EmailObserver:
    """Observer that receives all news topics."""

    def update(self, topic, data):
        """Print an email notification."""
        print(f"email:{topic}={data}")


class SmsObserver:
    """Observer that receives SMS notifications."""

    def update(self, topic, data):
        """Print an SMS notification."""
        print(f"sms:{topic}={data}")


def main():
    """Run the observer example."""
    subject = NewsSubject()

    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)
    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
