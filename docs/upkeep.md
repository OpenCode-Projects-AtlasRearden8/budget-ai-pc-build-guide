# Keeping It Healthy: The Five-Minute Monthly Routine

*Dust, updates, backups, temperature — the simple plan that keeps a used-parts build running for years.*

A used-parts build has one difference from a new one, and it's not performance — it's *age*. The parts are a few years old, meaning they've already lived a life, and the care that keeps them going is genuinely simple: keep them cool, keep them clean, keep the software current, and keep your files backed up. This is the shortest chapter in the guide, on purpose. Five minutes a month.

## The physical routine: dust (once a month, 2 minutes)

Dust is the only enemy that matters physically. It carpets every surface, and — insidiously — it carpets the parts that cool the insides: cooler fins, fan blades, vents. A dusty machine runs hotter, and hotter machines slow themselves and age faster.

```
[ ] Shut down and UNPLUG the machine (unplug, not just off).
[ ] Take the case side panel off (usually two thumbscrews at the back).
[ ] Desk outside or a porch, if you can: hold the can of compressed air
    upright and blow short bursts at the graphics card fans, the CPU
    cooler fins, the front intakes, and the power supply's external vent.
[ ] Wipe the vents on the case exterior with a slightly damp (not wet)
    cloth. Dry it before reassembly.
[ ] Panel back on, plug in, done.
```

Two warnings that deserve bold: **keep the can upright** (tipping it sprays freezing propellant that can frost chips — let it thaw before powering) and **never use a vacuum cleaner nozzle directly on parts** (vacuums generate static). A soft paintbrush and gentle air are the correct tools.

## The software routine: five minutes at a computer

Once a month, in order:

1. **Update the operating system.** Whatever OS you installed, run its updater. Security patches and driver fixes land there.
2. **Check drive space.** AI models accumulate like books — a few gigabytes here, ten there. Under 20% free space on the main SSD, use the tool's own commands to clear models you no longer run (`ollama list` first, `ollama rm <name>` after; every local-AI tool has an equivalent). Deleting a model is *not* risky — it can be re-downloaded identically in minutes.
3. **Glance at temperatures.** Most graphics cards show a temperature somewhere in system info or a settings screen. Under load (like actively running a model), 60–80°C is normal working warmth. Concerning: consistently 90°C+ under *any* load, for a card that used to sit in the 60s. That usually means dust (see above) or a fan that's stopped spinning — both fixable.
4. **Update the tool.** `ollama` on Windows/Mac self-updates quietly on restart; on Linux it comes with the OS's usual package updates. Same spirit for a chat interface: restart it once a month.

## Backups: the unglamorous, mandatory bit

Your machine holds two kinds of value: the parts (replaceable, insured by the used market) and **your files** (not replaceable). Hard drives and SSDs fail eventually — used ones fail *sooner* — and the only real protection is routine.

The honest minimum, per month:

```
[ ] A second drive plugged into the machine (any size), and copied onto it:
      everything in your Documents folder
```

That's it. One external or internal drive, one folder, one copy. Modern operating systems have a one-click "back up these folders" feature — find it once and the monthly check is making sure the backup *ran* (it'll show its last date). If you want to go one level fancier, a second copy at a relative's house or in a bank-safe-deposit-style spot covers fire and theft — but the single-drive copy is 90% of the protection for 10% of the effort, and covers the actual risk you own today: drive failure.

(Notice what *isn't* here: anything involving the cloud. That's a choice. If your files never leave the house, they can't leak from the house. The sync-forever lifestyle is real, but a plug-in-drive copy is the local-first philosophy's answer, and it's simpler.)

## The "when something goes wrong" flowchart

Used-parts machines occasionally behave briefly wrong. Nine times out of ten it's one of five things, in order of probability:

1. **It got dusty or hot recently** → this is dust; clean it.
2. **A driver updated badly, or the OS patched** → reboot; if it repeats, update the graphics driver again.
3. **A RAM stick has a bad contact** → power off, unplug, re-seat both sticks firmly (the rubber-slap fix for computer amnesia, honestly).
4. **A cable worked itself loose** → usually after moving the case; re-seat the power and monitor cables.
5. **The storage drive is elderly** → a drive's *slowness* (machine suddenly taking forever to boot, load, and open things) is the classic sign. Copy your files off. Then replacement is the answer — and because you built this machine with a spare slot (you did — remember the [motherboard section](parts-explained.md)), this is a $30 fix, not a crisis.

If it behaves wrong in a way that isn't those five, that's what the local friendly computer repair person and the message boards are for. Honest and low-stress.

## The yearly deeper check

Once a year — pick a month, say the month you built it — spend one longer session:

```
[ ] Full case-off clean, this time including the power supply's internal
    fan vent with short bursts of air (still upright).
[ ] Re-seat the graphics card and RAM, once each. (Removes invisible oxide
    film and refreshes contacts. Costs one screw-in, prevents mystery
    failures — real advice.)
[ ] Verify your backup drive to a second copy or verify the backup copied
    today's date.
[ ] Run a "test everything" pass: boot into the OS, confirm all RAM and
    SSD size, run one AI model to time it against last year's notes.
    25% slower than last year → clean it and re-test; 50% slower →
    look closely and consider a drive or fan.
[ ] Quiet check: listen to the machine's noise level you tuned way
    back when (see the silent-vs-speed chapter). Machines age louder (dust, aged fan bearings). Fans are
    cheap annual consumables, like printer ink but more reasonable.
```

## The mindset

Here's the honest summary of used-parts ownership: **expect perfection, accept maintenance.** A well-built budget machine should run for a good many years, and the difference between "it died" and "I replaced a $30 drive/fan in five minutes" is just this chapter's checklist, done often enough to notice a change. Keep the checklist visible — tape it inside the case panel if you like — and enjoy the machine: it's yours, paid less than anyone's new one, running AI that answers to no one.

That's the whole guide. Congratulations on building something real with your hands — now go [take a quick look at the glossary](glossary.md) and see how few words from it you still don't know.

---

*© Asdale Dynamics, LLC. Educational content only. Unplug before cleaning, keep your file the priority, and never vacuum static-vulnerable parts.*
