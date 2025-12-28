from imutils import paths
import numpy as np
import argparse
import cv2
import os

def dhash(image, hashSize=8):
    # convert the image to grayscale and resize the grayscale image,
    # adding a single column (width) so we can compute the horizontal
    # gradient
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
    # compute # the (relative) horizontal gradient between adjacent
    # column pixels
    diff = resized[:, 1:] > resized[:, :-1]
    # convert the difference image to a hash and return it
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def compute_hashes(dataset_path, hashSize=8):
    """Compute dHash for all readable images in `dataset_path`.

    Returns a dict mapping hash -> list of file paths. Skips unreadable
    or corrupt images and prints a warning for each.
    """
    hashes = {}
    imagePaths = list(paths.list_images(dataset_path))
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        if image is None:
            print(f"[WARN] unable to read image: {imagePath}")
            continue
        try:
            h = dhash(image, hashSize=hashSize)
        except Exception as e:
            print(f"[WARN] failed to hash {imagePath}: {e}")
            continue
        hashes.setdefault(h, []).append(imagePath)
    return hashes

    # construct the argument parser and parse the arguments
def main():
    ap = argparse.ArgumentParser(
        prog="imgdedup",
        description="Find and remove visually duplicate images using perceptual hashing.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  imgdedup ./photos              # Dry-run: preview duplicates
  imgdedup ./photos --remove     # Remove all duplicate images
        """)
    ap.add_argument("path", help="path to image directory to scan")
    ap.add_argument("--dry-run", action="store_true", default=True,
                    help="preview duplicates without deleting (default: True)")
    ap.add_argument("--remove", action="store_true",
                    help="actually delete duplicate images")
    args = vars(ap.parse_args())

    # basic validation
    dataset_path = args["path"]
    if not os.path.isdir(dataset_path):
        raise SystemExit("[ERROR] dataset path does not exist or is not a directory: {}".format(dataset_path))
    
    # conflict check: if both --dry-run and --remove, prefer --remove
    is_remove_mode = args["remove"]

    # compute hashes for all readable images
    print("[INFO] computing image hashes...")
    hashes = compute_hashes(dataset_path)
    
    if not hashes:
        print("[INFO] no images found in directory")
        return
    
    print("[INFO] found {} unique image(s)".format(len(hashes)))
    
    # loop over the image hashes
    for (h, hashedPaths) in hashes.items():
        # check to see if there is more than one image with the same hash
        if len(hashedPaths) > 1:
            # check to see if this is a dry run
            if not is_remove_mode:
                # initialize a montage to store all images with the same
                # hash
                montage = None

                # loop over all image paths with the same hash
                for p in hashedPaths:
                    # load the input image and resize it to a fixed width
                    # and height; skip unreadable images
                    image = cv2.imread(p)
                    if image is None:
                        print(f"[WARN] unable to read image for montage: {p}")
                        continue
                    image = cv2.resize(image, (900, 900))

                    # if our montage is None, initialize it
                    if montage is None:
                        montage = image
                    # otherwise, horizontally stack the images
                    else:
                        montage = np.hstack([montage, image])

                # show the montage for the hash
                print("[INFO] found {} duplicates with hash: {}".format(len(hashedPaths) - 1, h))
                #cv2.imshow("Montage", montage)
                #cv2.waitKey(0)
            else:
                # remove all image paths with the same hash except
                # for the first image in the list (since we want to keep
                # one, and only one, of the duplicate images)
                print("[INFO] removing {} duplicates with hash: {}".format(len(hashedPaths) - 1, h))
                for p in hashedPaths[1:]:
                    os.remove(p)
if __name__ == "__main__":
    main()
