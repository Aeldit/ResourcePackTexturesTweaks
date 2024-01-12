from PIL import Image


def get_pixel(color: tuple[int, int, int], local_img):
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


def set_borders(index: int, ref_img: Image, new_img: Image):
    if index in [1, 2, 3, 4, 5, 7, 12, 13, 14, 15, 29, 31]:
        for i in range(16):
            new_img.putpixel((i, 0), ref_img.getpixel((i, 0)))

    if index in [1, 2, 3, 16, 17, 18, 36, 37, 38, 39, 40, 42]:
        for i in range(16):
            new_img.putpixel((i, 15), ref_img.getpixel((i, 15)))

    if index in [1, 4, 6, 12, 13, 16, 24, 25, 28, 30, 36, 37]:
        for i in range(16):
            new_img.putpixel((0, i), ref_img.getpixel((0, i)))

    if index in [3, 5, 12, 15, 17, 19, 24, 27, 36, 39, 41, 43]:
        for i in range(16):
            new_img.putpixel((15, i), ref_img.getpixel((15, i)))

    # Corners
    if index in [8, 9, 17, 18, 19, 21, 22, 23, 34, 40, 43, 45, 46]:
        for i in range(16):
            new_img.putpixel((0, 0), ref_img.getpixel((0, 0)))

    if index in [6, 9, 10, 16, 18, 20, 21, 22, 28, 35, 42, 44, 46]:
        for i in range(16):
            new_img.putpixel((15, 0), ref_img.getpixel((15, 0)))

    if index in [5, 7, 8, 9, 11, 19, 20, 23, 31, 33, 35, 41, 46]:
        for i in range(16):
            new_img.putpixel((0, 15), ref_img.getpixel((0, 15)))

    if index in [4, 6, 7, 8, 10, 11, 20, 21, 29, 30, 32, 34, 46]:
        for i in range(16):
            new_img.putpixel((15, 15), ref_img.getpixel((15, 15)))
    return None


def main():
    path_to_rp = ""  # Replace this with "absolute/path/to/the/pack/assets
    general_path = path_to_rp + "/minecraft/optifine/ctm/connect/organics/"

    ref_dir = "oak/"
    # ref_dir = "stripped_oak/"

    log_types = ["acacia", "birch", "cherry", "crimson", "dark_oak", "jungle", "mangrove", "spruce", "warped"]

    for a in range(len(log_types)):
        log_types.append("stripped_" + log_types[a])

    for log_type in log_types:
        for i in range(1, 47):
            done_image = Image.open(general_path + ref_dir + str(i) + ".png")
            local_img = Image.open(general_path + log_type + "/" + "0.png")
            new_img = Image.new("RGBA", (16, 16))

            for line in range(16):
                for column in range(16):
                    new_img.putpixel((line, column), get_pixel(done_image.getpixel((line, column)), local_img))
                    set_borders(i, local_img, new_img)

            new_img.save(general_path + log_type + "/" + str(i) + ".png")
            new_img.close()


if __name__ == "__main__":
    main()
