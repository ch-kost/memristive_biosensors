"""Command line interface for biosensor passports."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from .models import BiosensorPassport
from .storage import load_passports, save_passports

DEFAULT_DATA_PATH = Path("data/passports.json")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Паспорта мемристивых биосенсоров")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    subparsers = parser.add_subparsers(dest="command", required=True)
    add_parser = subparsers.add_parser("add", help="Добавить паспорт")
    add_parser.add_argument("identifier")
    add_parser.add_argument("material")
    add_parser.add_argument("resistance_ohm", type=float)
    add_parser.add_argument("--date", default=date.today().isoformat())
    subparsers.add_parser("list", help="Показать паспорта")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    passports = load_passports(args.data)
    if args.command == "add":
        passport = BiosensorPassport(
            identifier=args.identifier,
            material=args.material,
            resistance_ohm=args.resistance_ohm,
            created_at=args.date,
        )
        passports.append(passport)
        save_passports(args.data, passports)
        print(f"Добавлен паспорт {passport.identifier}")
        return
    if not passports:
        print("Паспорта не найдены")
        return
    for passport in passports:
        print(
            f"{passport.identifier}: {passport.material}, "
            f"{passport.resistance_ohm:g} Ом, {passport.created_at}"
        )


if __name__ == "__main__":
    main()
