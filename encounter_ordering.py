# Encounter set usage from
# https://docs.google.com/spreadsheets/d/1nNLXLzIEQ4nxQqgOlGV8rsp26qAC437c88pmC5izCaQ/edit#gid=151087196

# Encounter ordering philosophy:
# 1. Encounter sets that show up earlier in the mission should be earlier in the pile
# 2. There should be minimal spacing between encounter sets used across missions
# 3. Ignore usage of the core set outside of notz
# 4. Return to replacement encounter sets should place its own campaign first, followed by core set replacements. Within each group, use the standard order for that set.

import csv
from pprint import pprint
from card_definitions import *
import itertools
import math

# PREFIX_TO_ORDER = "DUNWICH"
PREFIX_TO_ORDER = "CARCOSA"
# PREFIX_TO_ORDER = "TFA"
# PREFIX_TO_ORDER = "TCU"
# PREFIX_TO_ORDER = "EOTE"
# PREFIX_TO_ORDER = "SCARLET"

IGNORED_ENCOUNTER_SETS = {
    # TFA
    "Rainforests",  # not sure why these are not in the spreadsheet?
    "Poison",  # Put last
    # EOTE
    "Expedition Team",
    "Memorials of the Lost",
    "Tekeli-li",
}

IGNORED_MISSIONS = {
    # Dunwich
    "Armitage's Fate",
    # TFA
    "Heart of the Elders",
    # EOTE
    "Ice and Death",
    "The Heart of Madness",
}
# Correct typos in the spreadsheet
# LHS = correct name, RHS = spreadsheet name
MISSION_RENAMES = {
    # Dunwich
    "The Miskatonic Museum": "The Miskatonic University",
    # TFA
    "The Untamed Wilds": "The Untamed Wild",
    "The Doom of Eztli": "The Doom of Etzli",
    "Pillars of Judgement": "Heart of the Elders Part A",
    "K'n-yan": "Heart of the Elders Part B",
    # EOTE
    "The Crash": "Ice and Death, Part I",
    "Lost in the Night": "Ice and Death, Part II",
    "Seeping Nightmares": "Ice and Death, Part III",
    "City of the Elder Things": "The Heart of Madness, Part I",
    "The Great Seal": "City of the Elder Things (v. I)",
    "Stirring in the Deep": "City of the Elder Things (v. II)",
}

EXTRA_MISSIONS = {
    "EOTE": [
        (6, "City of the Elder Things (v. II)"),
        (7, "City of the Elder Things (v. III)"),
    ],
}

ENCOUNTER_RENAMES = {
    # EOTE
    "Shoggoths": "Shoggoth",
    # Scarlet Keys
    "Agents of the Outside": "Agents of the Ouside",
}

MISSIONS_FOR_ORDERING = eval(f"{PREFIX_TO_ORDER}_MISSIONS")
ENCOUNTERS_FOR_ORDERING = eval(f"{PREFIX_TO_ORDER}_ENCOUNTERS")


def parse_my_mission_name(name):
    if ":" in name:
        name = name.split(":")[1]
    name = name.replace("*", "")
    name = name.strip()
    return name


def main():
    raw_rows = []
    with open("encounter_sets.tsv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        for row in reader:
            raw_rows.append(row)

    def find_in_first_row(name):
        name = ENCOUNTER_RENAMES.get(name, name)
        for i, text in enumerate(raw_rows[0]):
            if name == text.strip():
                return i
        raise RuntimeError("Could not find encounter set: " + name)

    def find_mission_row(name):
        name = MISSION_RENAMES.get(name, name)
        for i in range(len(raw_rows)):
            if raw_rows[i][1].strip() == name:
                return raw_rows[i]
        raise RuntimeError("Could not find mission: " + name)

    encounter_names = [card[0].text for card in ENCOUNTERS_FOR_ORDERING]
    encounter_names = [e for e in encounter_names if e not in IGNORED_ENCOUNTER_SETS]

    mission_names = [card[0].text for card in MISSIONS_FOR_ORDERING]
    mission_names = [parse_my_mission_name(name) for name in mission_names]
    mission_names = [m for m in mission_names if m not in IGNORED_MISSIONS]

    extra_missions = EXTRA_MISSIONS.get(PREFIX_TO_ORDER, [])
    for (idx, name) in extra_missions:
        mission_names.insert(idx, name)

    print(mission_names)
    print(encounter_names)

    encounter_idx = [find_in_first_row(name) for name in encounter_names]
    print(encounter_idx)
    print(len(encounter_idx))

    encounter_map = {}
    for name, idx in zip(encounter_names, encounter_idx):
        encounter_map[idx] = name

    missions_w_encounters = []
    for mission in mission_names:
        mission_row = find_mission_row(mission)
        used_encounters = {e for e in encounter_idx if mission_row[e] != ""}
        missions_w_encounters.append((mission, used_encounters))

    pprint(missions_w_encounters)

    def grouping_loss(ordering, mission_sets, _):
        # If all encounters are touching, that's a perfect score of 0
        # Algo: Find the total spread of encounters (idx max - idx min).
        # Score is 1 per encounter misplaced from the spread
        if len(mission_sets) <= 1:
            return 0

        min_idx = 100
        max_idx = -1

        for i, e in enumerate(ordering):
            if e in mission_sets:
                min_idx = min(i, min_idx)
                max_idx = max(i, max_idx)

        score = (max_idx - min_idx + 1) - len(mission_sets)

        # Add 1 for introducing any type of gap
        if score > 0:
            score += 1

        # Squares leads to weird stuff where we force low levels into ugly spots
        return score

    def grouping_loss_v2(ordering, mission_sets, _):
        if len(mission_sets) <= 1:
            return 0

        is_counting = False
        last_is_active = False

        gap_size = 0
        num_gaps = 0

        total_gap_size = 0

        for e in ordering:
            if e in mission_sets:
                if is_counting:
                    num_gaps += 1
                    total_gap_size += gap_size
                    is_counting = False
                last_is_active = True
            else:
                if last_is_active:
                    is_counting = True
                    gap_size = 1
                else:
                    gap_size += 1
                last_is_active = False

        return num_gaps**2 + total_gap_size

    mission_centers = []
    for i in range(len(mission_names)):
        seg_size = float(len(encounter_idx)) / (2.0 * len(mission_names))
        mission_centers.append((2 * i + 1) * seg_size)
    print(mission_centers)

    def mean_dist_loss(ordering, mission_sets, mission_idx):
        # This one sucks. Grouping is more important than places
        score = 0.0
        for i, e in enumerate(ordering):
            if e in mission_sets:
                score += (i - mission_centers[mission_idx]) ** 2
        return score

    score_fn = grouping_loss_v2
    secondary_score_fn = mean_dist_loss

    def score_ordering_w_fn(ordering, fn):
        score = 0
        for i, me in enumerate(missions_w_encounters):
            m, es = me
            score += fn(ordering, es, i)
        return score

    def score_ordering(ordering):
        return score_ordering_w_fn(ordering, score_fn)

    def score_ordering_secondary(ordering):
        return score_ordering_w_fn(ordering, secondary_score_fn)

    best_orderings = []
    best_score = score_ordering(encounter_idx)

    def print_ordering(ordering):
        to_print = [encounter_map[i] for i in ordering]
        print(to_print, score_ordering(ordering), score_ordering_secondary(ordering))

    def render_ordering(ordering):
        for i, me in enumerate(missions_w_encounters):
            m, es = me
            row_str = f"{i + 1}:".rjust(3)
            for idx in ordering:
                if idx in es:
                    row_str += "X"
                else:
                    row_str += " "

            row_str += ":"
            row_str += str(score_fn(ordering, es, i))
            row_str += ":"
            row_str += str(secondary_score_fn(ordering, es, i))
            print(row_str)

    print("~~~~~~~~~", "CURRENT OUTCOME", "~~~~~~~~~")
    print_ordering(encounter_idx)
    render_ordering(encounter_idx)
    # return

    i = 0
    total = math.factorial(len(encounter_idx))
    for ordering in itertools.permutations(encounter_idx):
        i += 1
        if i % 100000 == 0:
            print(i, total, float(i * 100) / float(total))

        score = score_ordering(ordering)
        if score < best_score:
            best_score = score
            best_orderings = [ordering]
            print(score, ordering)
            print_ordering(ordering)
            render_ordering(ordering)
        elif score == best_score:
            best_orderings.append(ordering)


    print("BEST OUTCOMES", len(best_orderings))
    best_orderings = list(sorted(best_orderings, key=score_ordering_secondary))
    for i, res in enumerate(best_orderings):
        print("~~~~~~~~~", i, "~~~~~~~~~")
        print_ordering(res)
        render_ordering(res)

    print("~~~~~~~~~", "CURRENT OUTCOME", "~~~~~~~~~")
    print_ordering(encounter_idx)
    render_ordering(encounter_idx)


if __name__ == "__main__":
    main()
