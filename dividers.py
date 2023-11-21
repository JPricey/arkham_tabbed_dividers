from pathlib import Path
from typing import Optional
from colormap import rgb2hex, rgb2hls, hls2rgb
from airium import Airium

# CARD SIZING

# Card sleeves are 63.5mm x 88mm
CARD_WIDTH_MM = 90
CARD_HEIGHT_MM = 66
TAB_HEIGHT_MM = 7
CARD_TOT_HEIGHT_MM = CARD_HEIGHT_MM + TAB_HEIGHT_MM
PX_PER_MM = 3.7795275591
PX_PER_MM = 3.78
DIV_STROKE_WIDTH_MM = 0.5
SVG_EXTRA_MARGIN_MM = DIV_STROKE_WIDTH_MM / 2.0 - 0.01
SVG_BASE_START_MM = (SVG_EXTRA_MARGIN_MM, SVG_EXTRA_MARGIN_MM)

BEETWEEN_CARD_MARGIN_MM = 2.2

TAB_OVERLAP_MM = 0.5
TAB_DIAGONAL_MM = 2

# COLOUR HELPERS

def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


def adjust_color_lightness(r, g, b, factor):
    h, l, s = rgb2hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    s = min(s, 1.0)
    r, g, b = hls2rgb(h, l, s)
    return rgb2hex(int(r * 255), int(g * 255), int(b * 255))


def darken_color(hex, factor=0.1):
    r, g, b = hex_to_rgb(hex)
    return adjust_color_lightness(r, g, b, 1 - factor)


def get_tab_bottom_width(num_tabs):
    return (CARD_WIDTH_MM + (num_tabs - 1) * TAB_OVERLAP_MM) * 1.0 / num_tabs

def icon_path(path):
    return f"icons/{path}"

assert TAB_OVERLAP_MM <= TAB_DIAGONAL_MM

def styleize(style_dict):
    def fix_key(key):
        return key.replace("_", "-")

    elems = [f"{fix_key(k)}: {v}" for k, v in style_dict.items()]
    res = "; ".join(elems)
    return res


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

a = Airium()
a("<!DOCTYPE html>")

page_container_div_style = dict(
    display="flex",
    flex_wrap="wrap",
    page_break_after="always",
)

card_div_style = dict(
    position="relative",
    width=f"{CARD_WIDTH_MM + SVG_EXTRA_MARGIN_MM * 2}mm",
    height=f"{CARD_TOT_HEIGHT_MM + 2 * SVG_EXTRA_MARGIN_MM}mm",
    break_inside="avoid",
)

def get_tab_bottom_x(tab_number, num_tabs):
    tab_bottom_width = get_tab_bottom_width(num_tabs)
    tab_bottom_x = tab_number * (tab_bottom_width - TAB_OVERLAP_MM)
    return tab_bottom_x

def make_tab_points(num_tabs, tab_number):
    tab_bottom_width = get_tab_bottom_width(num_tabs)
    result = []
    base = (SVG_BASE_START_MM[0] * PX_PER_MM, SVG_BASE_START_MM[1] * PX_PER_MM)

    def add(point):
        point = (point[0] * PX_PER_MM + base[0], point[1] * PX_PER_MM + base[0])
        if len(result) == 0 or result[-1] != point:
            result.append(point)

    tab_bottom_x = get_tab_bottom_x(tab_number, num_tabs)

    add((0, CARD_TOT_HEIGHT_MM))
    add((0, TAB_HEIGHT_MM))

    add((tab_bottom_x, TAB_HEIGHT_MM))
    add((tab_bottom_x + TAB_DIAGONAL_MM, 0))
    add((tab_bottom_x + tab_bottom_width - TAB_DIAGONAL_MM, 0))
    add((tab_bottom_x + tab_bottom_width, TAB_HEIGHT_MM))

    add((CARD_WIDTH_MM, TAB_HEIGHT_MM))
    add((CARD_WIDTH_MM, CARD_TOT_HEIGHT_MM))

    return " ".join(f"{p[0]},{p[1]}" for p in result)


def build_card(data):
    card, tab_number, num_tabs = data
    tab_bottom_x = get_tab_bottom_x(tab_number, num_tabs)
    tab_bottom_width = get_tab_bottom_width(num_tabs)
    top_padding_mm = 0.5
    bot_padding_mm = 0.2

    darker = darken_color(card.colour, 0.5)

    card_svg_style = dict(
        fill=card.colour,
        stroke=darker,
        stroke_width=f"{DIV_STROKE_WIDTH_MM}mm",
    )

    icon_div_style = dict(
        position="absolute",
        display="block",
        width=f"{tab_bottom_width}mm",
        min_width=f"{tab_bottom_width}mm",
        top=f"{SVG_EXTRA_MARGIN_MM}mm",
        left=f"{tab_bottom_x + SVG_EXTRA_MARGIN_MM}mm",
    )

    padding_div_style = dict(
        height=f"{top_padding_mm}mm",
    )
    placer_div_style = dict(
        display="flex",
        align_items="center",
        justify_content="center",
        background="r",
        height=f"{TAB_HEIGHT_MM-top_padding_mm-bot_padding_mm}mm",
    )
    img_style = dict(max_width="100%", max_height=f"100%")

    background_icon_div_style = dict(
        position="absolute",
        display="block",
        left=f"{SVG_EXTRA_MARGIN_MM}mm",
        top=f"{SVG_EXTRA_MARGIN_MM + TAB_HEIGHT_MM}mm",
        width=f"{CARD_WIDTH_MM}mm",
        min_width=f"{CARD_WIDTH_MM}mm",
        height=f"{CARD_HEIGHT_MM}mm",
    )

    back_img_style = dict(
        height=f"{CARD_HEIGHT_MM * 0.8}mm", max_width="80%", opacity=0.15
    )

    back_placer_div_style = dict(
        display="flex",
        align_items="center",
        justify_content="center",
        height=f"{CARD_HEIGHT_MM}mm",
    )

    text_placer_div_style = dict(
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center",
        height=f"{CARD_HEIGHT_MM}mm",
    )

    text_div_style = dict()

    with a.div(style=styleize(card_div_style)):
        with a.svg(
            height=f"{CARD_TOT_HEIGHT_MM + 2 * SVG_EXTRA_MARGIN_MM}mm",
            width=f"{CARD_WIDTH_MM + 2 * SVG_EXTRA_MARGIN_MM}mm",
        ):
            a.polygon(
                points=make_tab_points(num_tabs, tab_number),
                style=styleize(card_svg_style),
            )
        with a.div(
            style=styleize(icon_div_style),
        ):
            a.div(style=styleize(padding_div_style))
            with a.div(
                style=styleize(placer_div_style),
            ):
                a.img(
                    src=icon_path(card.tab_icon),
                    alt="BROKEN!!",
                    style=styleize(img_style),
                )

        if card.back_icon:
            with a.div(
                style=styleize(background_icon_div_style),
            ):
                with a.div(
                    style=styleize(back_placer_div_style),
                ):
                    a.img(
                        src=icon_path(card.back_icon),
                        alt="BROKEN!!",
                        style=styleize(back_img_style),
                    )
        with a.div(
            style=styleize(background_icon_div_style),
        ):
            with a.div(
                style=styleize(text_placer_div_style),
            ):
                a.div(style=styleize(dict(flex_grow=1)))
                a(card.text)
                a.div(style=styleize(dict(flex_grow=4)))


def generate_output(cards_to_make, filename):
    with a.html():
        with a.head():
            a.meta(charset="utf-8")
            with a.style():
                a(
                    f"""
                @font-face {{
                    font-family: "birmingham";
                    src: url("icons/teutonic.ttf");
                }}
                body {{
                    font-family: birmingham;
                    margin: 0;
                    padding: 0;
                }}
                @media print {{
                    @page {{
                        margin-top: 25mm;
                    }}

                    div {{
                        break-inside: avoid;
                        page-break-inside: avoid;
                    }}
                }}
                """
                )
        for chunk in divide_chunks(cards_to_make, 6):
            with a.div(style=styleize(page_container_div_style)):
                for card in chunk:
                    build_card(card)

    with open(filename, "w") as f:
        f.write(str(a))
