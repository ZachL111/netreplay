"""Executable checks for the netreplay casebook."""

from __future__ import annotations

from collections import Counter

from . import netreplay_segment_00
from . import netreplay_segment_01
from . import netreplay_segment_02
from . import netreplay_segment_03
from . import netreplay_segment_04
from . import netreplay_segment_05
from . import netreplay_segment_06
from . import netreplay_segment_07
from . import netreplay_segment_08
from . import netreplay_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from netreplay_segment_00.iter_netreplay_00()
    yield from netreplay_segment_01.iter_netreplay_01()
    yield from netreplay_segment_02.iter_netreplay_02()
    yield from netreplay_segment_03.iter_netreplay_03()
    yield from netreplay_segment_04.iter_netreplay_04()
    yield from netreplay_segment_05.iter_netreplay_05()
    yield from netreplay_segment_06.iter_netreplay_06()
    yield from netreplay_segment_07.iter_netreplay_07()
    yield from netreplay_segment_08.iter_netreplay_08()
    yield from netreplay_segment_09.iter_netreplay_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def netreplay_summary() -> dict:
    return assert_expected()
