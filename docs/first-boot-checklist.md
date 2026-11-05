# Build Day and First Boot

*The order to assemble in, the checklist to run before and after you press power — and the two mistakes everyone makes exactly once.*

The parts are here. The desk is cleared. Today you turn a pile of boxes into a working computer — and an hour after that, into a machine that runs AI with the internet unplugged. This chapter is a walking-pace checklist, not a lecture: the assembly order people actually use, the checks that catch 95% of first-boot problems, and the two famous mistakes every builder makes once.

## Ground rules first (five minutes, genuinely important)

- **Unplug everything before touching inside-parts.** No exceptions, ever, mid-build. Power off ≠ unplug; do both.
- **Ground yourself.** Touching bare case metal (or a doorknob or radiator) occasionally during the build bleeds off static electricity, which can invisibly damage chips. A $10 anti-static wrist strap works too if you like gadgets. Static damage is rare, but it's the one preventable cause of "the part arrived fine and doesn't work."
- **Keep screws in their bags / a magnetic dish.** Loose screws lost in the case are the single most common "why is it making that sound," and a screw bridging two components is how circuits fail.
- **Clear pets and small kids from the room.** This is a one-time instruction, not an ongoing drama. A screwdriver tray and a closed door do the job.
- **The parts arrive in boxes — the *right* parts arrive in boxes.** Open, count, compare against your worksheet, photograph anything that looks damaged. If something's wrong, the day to find out is before assembly, not after.

## The assembly order people actually use

Most people build in an order like this, because parts tolerate being *handled* much better than being *installed twice*. Read through fully before starting; it's a one-pass job for each part.

```
1.  Put the motherboard on its cardboard box, on a clear table. NOT in the case yet.
2.  Open the CPU socket (a small latch+arm, usually labeled). Match the
    corner-arrow triangle on the CPU to the one on the socket. It drops in
    with ZERO FORCE — if you are pressing, it's misaligned. Close the latch.
3.  Seat RAM into the slots: push firmly, straight down, until both end
    clips click. (If your board has 4 and you have 2 sticks, see the tip below.)
4.  Attach the CPU cooler on top of the CPU with a small blob of thermal
    paste (pea-sized dot in the middle — it spreads itself). Plug the
    cooler fan's little cable into the header labeled "CPU_FAN."
5.  NOW put the motherboard into the case, screwed down through the standoffs.
6.  Install the power supply, fan facing down or the room-facing direction
    per the case's airflow design, then screw it in at the back panel.
7.  Install the graphics card into its long slot on the motherboard,
    snap it down, connect its power plug(s) from the PSU (there will be
    a plug or two hanging near it).
8.  Screw the SSD into the SSD bay, connect a SATA data cable to it and the
    motherboard, and a SATA power cable from the PSU. (If your drive is NVMe,
    it goes into a small M.2 slot on the motherboard instead — plug straight
    down, screw in the tiny hold-down screw.)
9.  Connect the case's front panel: the little cluster of wires (power button,
    USB ports, headphone jack). Each wire attaches to small pins on the
    motherboard's edge. There's usually a tiny printed guide by them or in
    the board's manual. The power-button pair is the only critical one;
    the USB and audio plugs only fit the one correct way.
10. Case fans: plug into "SYS_FAN" or "CHA_FAN" headers on the motherboard,
    or (some cases) directly into molex/sata power from the PSU.
```

**RAM slot tip:** check the board manual for which slots are "channel A" — paired sticks usually go in slots 2 and 4 (counting from the CPU end). All boards color-code or label the correct pairing; the manual confirms in ten seconds.

**Take breaks.** Nobody builds a computer in one flawless session, and most errors happen in the tired last twenty minutes. Walk to the kitchen and come back twice during the day.

## The two famous mistakes everyone makes once

1. **Motherboard standoffs.** In every case there are small brass or plastic towers screwing into the case floor. Your motherboard sits ON TOP of those and gets screwed to them. If a standoff sits in the wrong position, it can be touching the back of the board (short circuits and mysterious power-offs), or — the famous one — a standoff is *missing* under part of the board, so the board flexes, and something quietly doesn't make contact. The check: **the motherboard has a specific number of screw holes; every one should have a standoff underneath it, and no spares touching anything.** Two minutes with a torch, and you've skipped the classic.
2. **The power-button front-panel wires.** The tangle of tiny single-pin connectors is intimidating, and plugging them blind means the button does nothing. The fix lives in the motherboard's mini-manual (or a legend printed right beside the pins on some boards). Match the wire labeled something like `PWR_BTN` to the matching pin pair — and if the machine powers on when *unplugged-and-replugged* fails to respond, flipping the wire pair around is the classic fix. This is annoying, never dangerous, and fixable. Read once, do once, forever learned.

## The power-on checklist

Do this *before* pressing power, and then again after. It catches nearly all first-boot failures.

**Before pressing power:**

```
[ ] Every cable is plugged into BOTH ends (PSU→motherboard 24-pin, PSU→CPU
    8-pin [the one nearest the CPU — this is the single forgotten one,
    costing first-boot confusion more than anything]),
    PSU→graphics card power plugs, PSU→SSD, PSU→extra drives.
[ ] RAM clips are fully snapped on both ends.
[ ] No loose screws visibly rolling in the case (flip the case gently
    and listen).
[ ] CPU cooler is physically attached (never powered-on-bare-CPU).
[ ] The case's PC-standoffs are correct and only at board-hole positions.
[ ] Monitor cable is plugged into the GRAPHICS CARD's port, not the
    motherboard's. (The most common "black screen" of all time.)
[ ] Keyboard/mouse plugged into the direct USB ports on the case (the others
    connect late in setup).
```

**Press power.** One press. Watch, listen.

**It lights up and shows a screen:** beautiful. You may hear a single beep on some boards; that's a happy noise. Continue to setup below.

**It lights up, but shows no screen or no beep, and fans spin:** switch power off at the back of the PSU, wait, then check the standard three: RAM fully seated (re-seat both), graphics card seated, CPU-8-pin plugged in. Then press power again. Being seated properly *does* take 80% of first-boot no-screen fixes; don't skip to exotic explanations.

**Nothing lights at all, no fans:** power strip on? Wall works? PSU's back-facing switch set on? The 24-pin on the motherboard fully clicked in? All those are the standard, and they resolve nearly all "it did not begin."

## On the first real boot

- **Choose an operating system.** Whatever you already know is the right answer. (Both Linux and Windows run local AI tools; the Ollama chapter covers both install paths.) A spare USB drive and a free hour gets the OS in.
- **Install the graphics driver.** This matters more than any other single software step — the graphics card below needs its driver to reach full speed.
- **Update the OS.** Patches make the next part faster and safer.

Then one quiet last checklist, before the fun:

```
[ ] System recognizes all RAM (check the OS's system info against your sticks).
[ ] All drives show up at the size you bought.
[ ] Fans spin when the machine works, and stop (or nearly stop) at idle.
    ← If they never stop, reread the silent-vs-speed chapter's fan-curve
    tip — this is a free 20-minute fix.
[ ] Machine is audible-idle: a gentle hum, not a whine. This is the sound
    you'll live with for years; fixing it now costs nothing.
```

One last honest word on the CPU 8-pin cable: two *similar* 8-pin plugs hang near the CPU on many power supplies — one for the CPU (labeled something like "EPS") and ones for graphics cards (labeled something like "PCI-E"). They're shaped differently to help you, but the difference is subtle at beginner speed, and plugging the wrong one means the CPU never gets power — a mystery no-screen with fans sometimes still spinning. Read the tiny labels printed on the cables. Ten seconds; saves an evening.

## Celebrate, then do the smart last thing

You built a computer. Like, with your hands. Tell someone — genuinely, that's worth all the work in a phrase your grandma would love.

Then the smart last step before celebrating further: **install the local AI tool and let a model load.** That's the [Ollama install day chapter](ollama-install-day.md) — a walking-pace chain too, with honest notes on what to expect, plus a checklist at the end for wrapping up your first day as an [AI-machine owner](upkeep.md).

---

*© Asdale Dynamics, LLC. Educational content only. Unplug, ground, and never force-fit anything: those three rules prevent every beginner injury to parts and pride.*
