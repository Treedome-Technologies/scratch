"""Deliberately failing test for the bot-report check; removed afterwards."""


def test_report_check_fails() -> None:
    """Fails on purpose so SquidBot reports a failed check."""
    assert 1 + 1 == 3
