#!/usr/bin/env python3
"""Download all artwork from the old Wix site into ./images/ (run once, from this folder).

Usage:  python3 download_images.py
Needs only Python 3 (no extra packages). Safe to re-run: existing files are skipped.
"""
import os
import sys
import urllib.request

BASE = "https://static.wixstatic.com/media/c8326d_"

# local path -> Wix file id (original, full-resolution file)
IMAGES = {
    "images/self-portrait.png": "1efba6bdefd8451d998649e172e84daa~mv2_d_2927_2309_s_2.png",

    "images/painting/p01.jpg": "3375a4f02501490bb4cb11d7ddfea000~mv2.jpg",
    "images/painting/p02.png": "1efba6bdefd8451d998649e172e84daa~mv2_d_2927_2309_s_2.png",
    "images/painting/p03.jpg": "0e5c38053a5e4d2f972b6acb933dfc4a~mv2.jpg",
    "images/painting/p04.jpg": "4dd61ec1d0044ca596f54623fe3632fc~mv2.jpg",
    "images/painting/p05.jpg": "decbbf70b18e40caba1c781253f977e7~mv2.jpg",
    "images/painting/p06.jpg": "4a4af4cb23c54018887a518bcb96190e~mv2.jpg",
    "images/painting/p07.jpg": "ce6ae897601547ffb7e032a23d98c836~mv2.jpg",
    "images/painting/p08.jpg": "9ec074ad791f49a6a0bb2437a0ad6c8a~mv2.jpg",
    "images/painting/p09.jpg": "248dd977fc1f4c5ba33f604adcfc94d5~mv2.jpg",
    "images/painting/p10.jpg": "b839962f15d4428f865de643caad9552~mv2.jpg",
    "images/painting/p11.jpg": "a1f5af41c94b466f93b88e7b89e575c2~mv2.jpg",
    "images/painting/p12.jpg": "94120eca95424829bb66da3f69963858~mv2.jpg",
    "images/painting/p13.jpg": "829eff38c0c642e182e5d4f89845be5b~mv2.jpg",
    "images/painting/p14.jpg": "18d1a35e09824edcabeb4ce905380ac2~mv2.jpg",
    "images/painting/p15.jpg": "3ae53be7df3749d2aed1f9762decdbe9~mv2.jpg",
    "images/painting/p16.jpg": "18602edc1cad440a9c8fb59bb42fcbab~mv2.jpg",
    "images/painting/p17.jpg": "89f1192d31054f1d8392a1d3b72d9a6a~mv2.jpg",

    "images/cg/c01.png": "0f385db7204f477ab6c76888ab5512b1~mv2.png",
    "images/cg/c02.jpg": "dd83de015bbe43458eb4fea3bd8de272~mv2_d_2412_2312_s_2.jpg",
    "images/cg/c03.jpg": "c6111d1b67b9480eabd9404dc305f315~mv2_d_2412_2312_s_2.jpg",
    "images/cg/c04.png": "240a24fdab164a2dbdcbbcc001646b71~mv2.png",
    "images/cg/c05.png": "bc22920209b743c1aafed7f4be604aff~mv2_d_1668_2388_s_2.png",
    "images/cg/c06.png": "4877d1793f834375b6f2d0846de8bf6c~mv2_d_1668_2388_s_2.png",
    "images/cg/c07.png": "a9d2f38d509f42d1b2f12071c328a454~mv2_d_1763_1922_s_2.png",
    "images/cg/c08.png": "be44936b54544752b2b497bf0fcde761~mv2_d_1668_2388_s_2.png",
    "images/cg/c09.png": "f544dc9ad5284cc8a89ddafd8908858e~mv2_d_1668_2388_s_2.png",
    "images/cg/c10.png": "40f965bee446487bba79db0e5f72dcca~mv2_d_1668_2388_s_2.png",
    "images/cg/c11.png": "d3c294a7cd134f3abe8bd2459268015c~mv2_d_1434_2160_s_2.png",
    "images/cg/c12.png": "f94dda046d374bdd85965b8bd0438140~mv2_d_1668_2388_s_2.png",
    "images/cg/c13.png": "d509706f99b2435fb3ddae38bbed0f38~mv2_d_2388_1668_s_2.png",
    "images/cg/c14.jpg": "9ffde3b3e68144d7bce93c2dffb80d0f~mv2.jpg",
    "images/cg/c15.jpg": "e5bf7e0e75364c9f989a151417ae42bb~mv2.jpg",
    "images/cg/c16.jpg": "f394550c81fb48208a3e3862d7fa0f50~mv2_d_2414_2544_s_4_2.jpg",
    "images/cg/c17.jpg": "01ab0b25479f4d11976baafc795c8a4e~mv2_d_3219_3008_s_4_2.jpg",
    "images/cg/c18.jpg": "96539971aabf4f9da0f4081326be80dd~mv2_d_3960_3240_s_4_2.jpg",
    "images/cg/c19.png": "8d698fe7fa2045459c8d7160cc7143fd~mv2_d_2048_2048_s_2.png",
    "images/cg/c20.jpeg": "be3b1a2a524c4239b8b6ecd56d658f8e~mv2.jpeg",
    "images/cg/c21.png": "dee6cbb7443f4bc8a29eb97ee9df955f~mv2_d_1668_2388_s_2.png",
    "images/cg/c22.png": "2bc1d52c632e4934be9e74d0c2a80061~mv2_d_2388_1668_s_2.png",
    "images/cg/c23.png": "c45c4993b2da4d70856a9b30b4b8554a~mv2_d_1668_1591_s_2.png",
    "images/cg/c24.png": "8ab2f4bff6c546aeb5599fb5559f953a~mv2.png",
    "images/cg/c25.png": "32a90a23e1c14e968ee80d911c272e6e~mv2_d_1858_1682_s_2.png",
}

# Resume photo: the original page shows a specific crop of this file.
RESUME_URL = (
    BASE + "02929c5a3d9d402b8a09ee6850791494~mv2.jpg"
    "/v1/crop/x_22,y_259,w_581,h_320/fill/w_1080,h_669,al_c,q_90/resume.jpg"
)


def fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print("skip   ", dest)
        return True
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
            f.write(r.read())
        print("ok     ", dest)
        return True
    except Exception as e:
        print("FAILED ", dest, "-", e)
        return False


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    failed = 0
    for dest, fid in IMAGES.items():
        if not fetch(BASE + fid, dest):
            failed += 1
    if not fetch(RESUME_URL, "images/resume-photo.jpg"):
        failed += 1
    print("\nDone. %d failed." % failed)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
