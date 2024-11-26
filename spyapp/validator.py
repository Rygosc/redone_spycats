import os
import json
from django.conf import settings
from django.core.exceptions import ValidationError


_validation_breeds = None


def load_validation() -> list:
    global _validation_breeds
    if _validation_breeds is None:
        try:
            file_path = os.path.join(settings.BASE_DIR, "validator.json")
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                _validation_breeds = [breed["name"].lower() for breed in data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Error loading validation file: {e}")
    return _validation_breeds


def valid_breed(value: str):
    valid_breeds = load_validation()
    if value.lower() not in valid_breeds:
        raise ValidationError(
            f"Invalid breed: {value}. Allowed breeds are: {', '.join(valid_breeds)}"
        )
