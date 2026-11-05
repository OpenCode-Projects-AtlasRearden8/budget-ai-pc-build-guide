# Glossary

*Every term this guide uses, defined once, in the order a beginner meets it. Skim it before shopping; return to it when a listing talks like a robot.*

Plain-English definitions, with a pointer to the chapter that explains each properly.

## The number and letter soup

- **GB / gigabyte** — Unit of digital stuff. One gigabyte holds roughly a couple hundred photos, or about one small AI model. RAM and storage sizes are counted in these. See [RAM and VRAM](ram-and-vram.md).
- **GB of VRAM** — The *graphics card's* private memory, counted separately from the computer's RAM. The number that decides which AI models can run. The central number of this entire guide.
- **B, as in "7B," "13B"** — "Billion parameters." Models are named by how many numbers they contain; bigger numbers usually mean smarter and hungrier. A "few billion" = small-class model; "13B" = classic midsize; "70B" = big, needs a house of VRAM.
- **GHz, like "3.2 GHz"** — CPU speed label, roughly "how many small instructions per second." Useful for *comparing CPUs nearby in age/family*, not much else. Never choose CPU by GHz alone.
- **W / watts** — Unit of power draw. CPUs and graphics cards have a "watts" rating; your **power supply** must comfortably exceed the total of everything inside (450–650 W covered in [price targets](price-targets.md)).

## The parts

- **CPU (central processing unit)** — The computer's general-purpose manager-chip. Runs the OS, browser, and everything except heavy math. In a budget AI build: buy modest, spend elsewhere. [Parts chapter](parts-explained.md).
- **GPU / graphics card / video card** — The parallel-math engine. Runs game pictures *and* AI models. **In AI builds it's the thinking engine**, the part to spend on, and its memory is the size that matters.
- **Motherboard / mainboard / "mobo"** — The big board everything connects to. Decides which CPUs, RAM generation, and slots you can use. **Match socket to CPU and DDR generation to RAM**, or buy it as a pair with the CPU and skip the guessing.
- **RAM (random access memory)** — The computer's working memory / workbench. Empties when powered off. **16–32 GB is the budget sweet spot.** Buy sticks in *matched pairs*.
- **VRAM (video RAM)** — The graphics card's own fast memory (a "private pot" separate from RAM). The model runs *in* it. **This, not gaming speed, is what you're buying.**
- **SSD (solid-state drive)** — Silent, fast storage with no moving parts. The correct main drive. 512 GB is the realistic budget target.
- **HDD (hard disk drive)** — Older spinning-disk storage: cheap, noisy, slow. Fine as a *second* archive drive; do not use as a main drive. (Frequently free on give-away boards.)
- **PSU (power supply unit)** — Converts wall power to the low-voltage food parts eat. **The one used part this guide recommends buying new.**
- **Case / tower / chassis** — The metal box. Standard "mid-tower" fits everything. **Most of the machine's *noise* lives here.**
- **CPU cooler** — The small fan and metal fin block that sits directly on the CPU. Frequently included free with a used CPU.
- **Case fans** — Small fans mounted in the case that push air through. **120+ mm "PWM" fans are the quiet pick.** [Silent vs speed](silent-vs-speed.md).

## AI and local-AI terms

- **Model / LLM / language model** — The "AI" itself: a giant table of numbers that, when run, produces text. Called LLM when it processes language. See [what running one means](index.md).
- **Ollama** — Free, open-source software that downloads models and runs them on your machine with one command. The standard entry point, used in [Ollama install day](ollama-install-day.md). Unaffiliated with this guide.
- **Model family (llama, gemma, qwen, mistral, etc.)** — The name of the *maker's* recipe; different families have different personalities. Try more than one; they're free.
- **Parameter** — One number inside a model. Models have billions. "7B" = about 7 billion parameters.
- **Pull / download a model** — Fetch the model's numbers to your drive. `ollama run <name>` does it automatically the first time.
- **Offloading** — When a model doesn't fit in VRAM, part of it lives in regular RAM instead. **The model still runs — slowly.** Why memory-first buying matters.
- **Trained / weights** — "Trained" = the long, expensive process that *made* the model somewhere else. "Weights" = the resulting numbers you download. You never train anything on a budget build; you *run* models people already trained. (This is good news: it's the cheap half.)
- **Context window** — How much of the conversation (or document) the model can "see" at once, measured in tokens. Bigger classes of models usually have bigger windows; small models get small windows.
- **Token** — Roughly "a piece of a word" — how models measure text. "4096-token context" = about 3,000 words of visible memory.
- **Inference** — The act of *running* a model to get an answer (as opposed to training). Your entire hobby is inference.
- **Local / local-first** — Running entirely on your own machine, no internet required after setup, no data leaving the house. **The point of this guide.**

## Builder's jargon

- **Socket** — The physical connector shape the CPU drops into. **CPU and motherboard must match.** Or buy both from one seller.
- **DDR3 / DDR4 / DDR5** — RAM's physical generation, each shaped differently. **Motherboard and RAM must match.** The most common used-shopping headache, fixed by one sticker photo.
- **SATA / NVMe / M.2** — Two ways an SSD connects. SATA uses a cable; NVMe plugs into a small motherboard slot (M.2). Both fine; NVMe is faster.
- **80 Plus** — A sticker meaning the power supply doesn't waste much power as heat. Any color level is fine for health; the *brand* matters more.
- **PWM (fans)** — Fans that can be *dynamically slowed down* by the motherboard. The quiet option, and standard on decent recent fans.
- **Thermal paste** — The paste (pea-sized dot) between CPU and cooler that transfers heat. Included with coolers; applied once, lasts years.
- **Standoff** — The small brass tower a motherboard sits on, above the case floor. **Every motherboard hole should have one; no extras touching anywhere.** The classic first-build mistake.
- **24-pin / 8-pin (EPS, PCI-E)** — The main power cables. 24-pin to the motherboard, the "EPS" 8-pin to the CPU (the forgotten one), "PCI-E" cables to the graphics card.
- **BIOS / UEFI** — The settings screen before your OS loads, where fan curves and boot order live. Reached by mashing Delete or F2 while booting. Don't change what you don't understand.
- **Thermal throttling** — The machine automatically slowing parts down when they overheat. Not a fault: a safety feature. If your machine does it constantly, your *cooling* is the [noise-vs-speed](silent-vs-speed.md) lesson you skipped.
- **PSU sticker / "for parts or repair" / mining card** — Three listing red flags covered in the [shopping worksheet](shopping-worksheet.md).

## Version of the golden rule

> **VRAM decides what can run. Everything else decides how comfortably.**

When in doubt all the way through this guide, return to that sentence — it resolves almost every shopping decision you'll face.

---

*© Asdale Dynamics, LLC. Educational content only — definitions in plain English for free readers, no endorsement of any specific product.*
