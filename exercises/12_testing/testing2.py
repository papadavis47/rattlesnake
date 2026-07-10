# TODO: Use unittest.mock.patch in the existing test to replace fetch_temperature.

from unittest.mock import patch


def fetch_temperature(city: str) -> int:
    raise RuntimeError(f"No weather service configured for {city}")


def weather_report(city: str) -> str:
    return f"{city}: {fetch_temperature(city)}°C"


def test_weather_report_uses_mock():
    with patch(f"{__name__}.fetch_temperature", return_value=0):
        assert weather_report("Oslo") == "Oslo: 12°C"
