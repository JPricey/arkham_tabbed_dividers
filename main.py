from card_definitions import *
from dividers import generate_output

CARDS_TO_MAKE = (
    []
    + NOTZ_MISSIONS
    + NOTZ_ENCOUNTERS
    + RTNOTZ_MISSIONS
    + RTNOTZ_ENCOUNTERS
    + DUNWICH_MISSIONS
    + DUNWICH_ENCOUNTERS
    + RTDUNWICH_MISSIONS
    + RTDUNWICH_ENCOUNTERS
    + CARCOSA_MISSIONS
    + CARCOSA_ENCOUNTERS
    + DARK_MATTER_MISSIONS
    + DARK_MATTER_ENCOUNTERS
    + RTCARCOSA_MISSIONS
    + RTCARCOSA_ENCOUNTERS
    + TFA_MISSIONS
    + TFA_ENCOUNTERS
    + RTTFA_MISSIONS
    + RTTFA_ENCOUNTERS
    + TCU_MISSIONS
    + TCU_ENCOUNTERS
    + RTTCU_MISSIONS
    + RTTCU_ENCOUNTERS
    + TDE_MISSIONS
    + TDE_ENCOUNTERS
    + TIC_MISSIONS
    + TIC_ENCOUNTERS
    + EOTE_MISSIONS
    + EOTE_ENCOUNTERS
    + SCARLET_MISSIONS
    + SCARLET_ENCOUNTERS
    + FHV_MISSIONS
    + FHV_ENCOUNTERS
    + CHALLENGE_MISSIONS
    + ROUGAROU
    + CARNEVALE
    + HOTEL
    + ABYSS
    + BLOB
    + WAR
    + MACH
    + FORTUNE
    + GALA
)


def main_arkham():
    generate_output(CARDS_TO_MAKE, "icons/teutonic.ttf", "tabbed_dividers.html")


if __name__ == "__main__":
    main_arkham()
