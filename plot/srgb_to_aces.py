import PyOpenColorIO as ocio
import matplotlib.pyplot as plt
import numpy as np

# Load OCIO config (adjust path as needed)
config = ocio.Config.CreateFromFile(r"D:\Documents\Development\Ocio\Blender_ACES\config.ocio")  # Replace with actual path

def srgb_to_acescg(r, g, b):
    processor = config.getProcessor(
        ocio.ColorSpaceTransform(src="Utility - sRGB - Texture", dst="ACEScg")
    )
    return processor.applyRGB([r, g, b])

def visualize_conversion(srgb, acescg):
    fig, axs = plt.subplots(1, 2, figsize=(6, 3))

    axs[0].imshow([[srgb]])
    axs[0].set_title("sRGB")
    axs[0].axis('off')

    # Clamp ACEScg for display (not for accurate look)
    aces_display = np.clip(acescg, 0, 1)
    axs[1].imshow([[aces_display]])
    axs[1].set_title("ACEScg (clamped)")
    axs[1].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    srgb_color = "dba142"
    srgb_color = tuple(int(srgb_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    acescg_color = srgb_to_acescg(*srgb_color)

    print("sRGB:   ", srgb_color)
    print("ACEScg: ", acescg_color)

    visualize_conversion(srgb_color, acescg_color)
