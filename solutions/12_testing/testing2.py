from unittest.mock import patch


def fetch_temperature(city: str) -> int:
    raise RuntimeError(f"No weather service configured for {city}")


def weather_report(city: str) -> str:
    return f"{city}: {fetch_temperature(city)}°C"


def test_weather_report_uses_mock():
    module_name = __name__
    with patch(f"{module_name}.fetch_temperature", return_value=12) as mocked_fetch:
        assert weather_report("Oslo") == "Oslo: 12°C"
    mocked_fetch.assert_called_once_with("Oslo")
