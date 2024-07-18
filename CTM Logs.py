"""
Author: Aeldit <https://github.com/Aeldit>

This program was made to make the connected textures for each type of log :
I made the oak type by hand using gimp.
This program takes each different pixel of the oak type and replaces it with the colors of the current log type, then
saves the file to the correct directory
"""
import os
import shutil
from os.path import isfile, join, isdir

from PIL import Image
from os import listdir


def get_pixel(color: tuple[int, int, int], local_img: Image) -> tuple[int, int, int]:
    if color == (184, 148, 95, 255):
        return local_img.getpixel((1, 1))
    elif color == (126, 98, 55, 255):
        return local_img.getpixel((2, 2))
    elif color == (150, 116, 65, 255):
        return local_img.getpixel((4, 2))
    elif color == (159, 132, 77, 255):
        return local_img.getpixel((6, 2))
    elif color == (194, 157, 98, 255):
        return local_img.getpixel((3, 3))
    elif color == (175, 143, 85, 255):
        return local_img.getpixel((5, 1))
    else:
        return color


def set_borders(index: int, ref_img: Image, new_img: Image) -> None:
    if index in (1, 2, 3, 4, 5, 7, 12, 13, 14, 15, 29, 31):
        for i in range(16):
            new_img.putpixel((i, 0), ref_img.getpixel((i, 0)))

    if index in (1, 2, 3, 16, 17, 18, 36, 37, 38, 39, 40, 42):
        for i in range(16):
            new_img.putpixel((i, 15), ref_img.getpixel((i, 15)))

    if index in (1, 4, 6, 12, 13, 16, 24, 25, 28, 30, 36, 37):
        for i in range(16):
            new_img.putpixel((0, i), ref_img.getpixel((0, i)))

    if index in (3, 5, 12, 15, 17, 19, 24, 27, 36, 39, 41, 43):
        for i in range(16):
            new_img.putpixel((15, i), ref_img.getpixel((15, i)))

    # Corners
    if index in (8, 9, 17, 18, 19, 21, 22, 23, 34, 40, 43, 45, 46):
        for i in range(16):
            new_img.putpixel((0, 0), ref_img.getpixel((0, 0)))

    if index in (6, 9, 10, 16, 18, 20, 21, 22, 28, 35, 42, 44, 46):
        for i in range(16):
            new_img.putpixel((15, 0), ref_img.getpixel((15, 0)))

    if index in (5, 7, 8, 9, 11, 19, 20, 23, 31, 33, 35, 41, 46):
        for i in range(16):
            new_img.putpixel((0, 15), ref_img.getpixel((0, 15)))

    if index in (4, 6, 7, 8, 10, 11, 20, 21, 29, 30, 32, 34, 46):
        for i in range(16):
            new_img.putpixel((15, 15), ref_img.getpixel((15, 15)))
    return None


def main() -> None:
    """
    To use the program, we have to put the basic file for each log type (the texture that will be 0.png)
    The images MUST be in RGB or RGBA mode, otherwise the outputs will be fully transparent or black
    @return: None
    """
    # Replace this with "absolute/path/to/the/pack/assets
    path_to_rp = "../../Dev/MC-Resource-Packs/CTM_OF_Fabric/assets"
    modid = "biomesoplenty"
    general_path = path_to_rp + "/%s/optifine/ctm/connect/organics/" % modid

    # The directory containing the textures used to copy the pattern
    ref_dir = "oak"

    # Obtains the files that are in png format
    log_types = tuple(
        file.removesuffix(".png") for file in tuple(
            f for f in listdir(general_path) if isfile(join(general_path, f))
        )
        if file.endswith(".png")
    )

    # Creates a directory for each png file found
    # and moves the associated file inside the created dir (also renames the file to 0.png)
    for file in log_types:
        current_dir = general_path + file
        if not os.path.isdir(current_dir):
            os.mkdir(current_dir)
        shutil.move("%s/%s.png" % (general_path, file), "%s/0.png" % current_dir)

    # Creates the .properties file that will contain the ctm information
    only_dirs = [d for d in listdir(general_path) if isdir(join(general_path, d))]
    if ref_dir not in only_dirs:  # if the dir with the pattern is not present, we can't complete the program
        return None
    only_dirs.remove(ref_dir)

    for directory in only_dirs:
        with open("%s/%s/%s.properties" % (general_path, directory, directory), "w") as wf:
            wf.write(
                "matchBlocks=%s:%s\n"
                "method=ctm\n"
                "tiles=0-46\n"
                "faces=top bottom\n"
                "connect=tile"
                % (modid, directory.removesuffix("_top"))
            )

    for log_type in log_types:
        for i in range(1, 47):
            # done_image = Image.open(general_path + ref_dir + str(i) + ".png")
            done_image = Image.open("%s%s/%d.png" % (general_path, ref_dir, i))
            # local_img = Image.open(general_path + log_type + "/" + "0.png")
            local_img = Image.open("%s%s/0.png" % (general_path, log_type))
            new_img = Image.new("RGBA", (16, 16))

            for line in range(16):
                for column in range(16):
                    new_img.putpixel((line, column), get_pixel(done_image.getpixel((line, column)), local_img))
                    set_borders(i, local_img, new_img)

            new_img.save("%s%s/%d%s" % (general_path, log_type, i, ".png"))
            new_img.close()
            local_img.close()
            done_image.close()
    return None


if __name__ == "__main__":
    main()
