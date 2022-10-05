"""Constants for the Raspberry Pi GPIO integration."""

from typing import Final


DOMAIN: Final = "rpi_gpio"

CONF_GPIO: Final = "gpio"
CONF_CONFIGURED_PORTS: Final = "configured_ports"
CONF_PORTS: Final = "ports"

CONF_BOUNCETIME: Final = "bouncetime"
CONF_PULL_MODE: Final = "pull_mode"
CONF_INVERT_LOGIC: Final = "invert_logic"

PUD_DOWN: Final = "21"
PUD_UP: Final = "22"

DEFAULT_BOUNCETIME: Final = 50
DEFAULT_INVERT_LOGIC: Final = False
DEFAULT_PULL_MODE: Final = PUD_UP

GPIO_PIN_MAP: Final = {
    "0": "27",
    "1": "28",
    "2": "3",
    "3": "5",
    "4": "7",
    "5": "29",
    "6": "31",
    "7": "26",
    "8": "24",
    "9": "21",
    "10": "19",
    "11": "23",
    "12": "32",
    "13": "33",
    "14": "8",
    "15": "10",
    "16": "36",
    "17": "11",
    "18": "12",
    "19": "35",
    "20": "38",
    "21": "40",
    "22": "15",
    "23": "16",
    "24": "18",
    "25": "22",
    "26": "37",
    "27": "13",
}
