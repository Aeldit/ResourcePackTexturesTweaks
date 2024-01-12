from PIL import Image


def main(replacements: list[tuple[int, int, int, int]], path: str, replace_positions: list[tuple[int, int]]):
    image = Image.open(path)
    size = image.size
    new_img = Image.new("RGBA", size)
    replaced = False
    colors = [image.getpixel(replace_positions[j]) for j in range(len(replace_positions))]

    for line in range(size[0]):
        for column in range(size[1]):
            for i in range(len(replacements)):
                if image.getpixel((line, column)) == colors[i] and not replaced:
                    new_img.putpixel((line, column), replacements[i])
                    replaced = True
            if not replaced:
                new_img.putpixel((line, column), image.getpixel((line, column)))
            else:
                replaced = False

    new_img.save(path)
    new_img.close()
    return 0


if __name__ == "__main__":
    r = [(69, 0, 0, 255), (129, 0, 0, 255)]
    rp_dir = ""  # Replace this with "/path/to/the/pack/assets/

    # Widgets
    """
    minecraft/textures/gui/sprites/widget/button_highlighted.png",
    "minecraft/textures/gui/sprites/widget/checkbox_highlighted.png",
    "minecraft/textures/gui/sprites/widget/checkbox_selected_highlighted.png",
    "minecraft/textures/gui/sprites/widget/slider_handle_highlighted.png",
    "minecraft/textures/gui/sprites/widget/slider_highlighted.png",
    "minecraft/textures/gui/sprites/widget/unlocked_button_highlighted.png",
    # Enchanting table
    "minecraft/textures/gui/sprites/container/enchanting_table/enchantment_slot_highlighted.png",
    # Beacon
    "minecraft/textures/gui/sprites/container/beacon/button_selected.png
    """
    vanilla_paths = [

        # Social interactions
        "minecraft/textures/gui/sprites/social_interactions/mute_button_highlighted.png",
        "minecraft/textures/gui/sprites/social_interactions/report_button_highlighted.png",
        "minecraft/textures/gui/sprites/social_interactions/unmute_button_highlighted.png"
    ]

    ctms_paths = [
        "ctms/textures/gui/controls.png",
        "ctms/textures/gui/reload.png"
    ]

    iris_path = [
        "iris/textures/gui/widgets.png"
    ]

    modmenu_paths = [
        "modmenu/textures/gui/configure_button.png",
        "modmenu/textures/gui/filters_button.png",
        "modmenu/textures/gui/mods_button.png"
    ]

    etf_paths = [
        "entity_texture_features/textures/gui/settings_focused.png"
    ]

    paths = vanilla_paths

    for a in range(len(paths)):
        main(r, rp_dir + paths[a], [(2, 2), (1, 1)])
