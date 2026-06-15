# GitBoard 2.0 — KMK Firmware Installation Guide

This guide explains how to install and run the KMK firmware for the GitBoard 2.0, an 8‑key macro pad designed for Git workflow shortcuts. KMK runs directly on the RP2040 — no compiling, no QMK setup, and no toolchains required.

---

## Folder Structure

Your firmware folder should look like this:

gitboard2_kmk/
├── kmk/
├── code.py
└── boot.py   (optional)

---

## Requirements

You will need:

- An RP2040 board (such as a Raspberry Pi Pico or compatible)
- A USB cable
- The firmware folder shown above

---

## Flashing KMK to the RP2040

1. Hold the **BOOTSEL** button on the RP2040.
2. While holding BOOTSEL, plug the board into your computer.
3. A USB drive named **RPI-RP2** will appear.
4. Copy the following items onto the RPI-RP2 drive:

   - The entire **kmk/** folder
   - **code.py**
   - **boot.py** (optional)

5. Eject the RPI-RP2 drive.
6. Unplug and replug the RP2040 normally.

The board will reboot and run KMK automatically.

---

## Testing the GitBoard

1. Open a text editor or terminal.
2. Press each key on the GitBoard.
3. You should see the Git commands appear instantly.

Examples:
- `git add .`
- `git commit -m ""`
- `git push`
- `git pull`
- `git status`
- `git log`
- `git checkout -b `
- `git clone `

---

## Updating the Firmware

To update your code later:

1. Plug the RP2040 in normally.
2. A drive named **CIRCUITPY** will appear.
3. Replace **code.py** with your updated version.
4. The board reloads automatically.

If CIRCUITPY does not appear, repeat the BOOTSEL flashing steps.

---

## Troubleshooting

**Board does not show up as RPI-RP2**
- Hold BOOTSEL before plugging in
- Try a different USB cable (some are charge‑only)
- Try a different USB port

**Board shows CIRCUITPY but nothing happens**
- Check for syntax errors in code.py
- Delete any file named `boot_out.txt` and reboot

---

## License

This firmware is for personal use with the GitBoard 2.0.
