"""Unit tests for passport validation and serialization."""
import unittest

from biosensors.models import BiosensorPassport


class BiosensorPassportTests(unittest.TestCase):
    def test_valid_passport(self) -> None:
        passport = BiosensorPassport("BS-001", "TiO2", 1250.0, "2026-10-30")
        self.assertEqual(passport.identifier, "BS-001")

    def test_resistance_must_be_positive(self) -> None:
        for resistance in (0, -1):
            with self.subTest(resistance=resistance), self.assertRaises(ValueError):
                BiosensorPassport("BS-002", "ZnO", resistance, "2026-10-30")

    def test_date_must_be_iso_formatted(self) -> None:
        with self.assertRaises(ValueError):
            BiosensorPassport("BS-003", "TiO2", 500, "30.10.2026")

    def test_round_trip(self) -> None:
        passport = BiosensorPassport("BS-004", "TiO2", 500, "2026-10-30")
        self.assertEqual(BiosensorPassport.from_dict(passport.to_dict()), passport)


if __name__ == "__main__":
    unittest.main()
