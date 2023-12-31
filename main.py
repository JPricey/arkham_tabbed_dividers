from card_definitions import *
from dividers import generate_output 

CARDS_TO_MAKE = ([]
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
    + RTCARCOSA_MISSIONS
    + RTCARCOSA_ENCOUNTERS
    + TFA_MISSIONS
    + TFA_ENCOUNTERS
    + RTFA_MISSIONS
    + RTFA_ENCOUNTERS
    + EOTE_MISSIONS
    + EOTE_ENCOUNTERS
    + SCARLET_MISSIONS
    + SCARLET_ENCOUNTERS
    + CHALLENGE_MISSIONS
    + ROUGAROU
    + CARNEVALE
    + HOTEL
    + ABYSS
    + DARK_MATTER_MISSIONS
    + DARK_MATTER_ENCOUNTERS
)

def main():
    generate_output(CARDS_TO_MAKE, "tabbed_dividers.html")

if __name__ == "__main__":
    main()
