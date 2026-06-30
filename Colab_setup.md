# Setting Up the Green AI Hackathon Notebook on Google Colab

A step-by-step guide to get `green_ai_hackathon_baseline.ipynb` running in
your browser. No installation needed on your own computer — everything
runs on Google's servers, for free.

**Your instructor will have given you either a link or a file** —
whichever one applies to you, follow that path in Step 2; everything from
Step 3 onward is identical either way.

---

## Step 1 — Open Google Colab

Go to **[colab.research.google.com](https://colab.research.google.com)**
in your browser. Sign in with a Google account if you're not already
signed in (any personal or institutional Google account works).

---

## Step 2 — Get the notebook into your own Drive

### Path A — You were given a link

When you open a shared link, you'll be viewing the *instructor's* copy —
you can't edit or run it directly, and if everyone in the room tried to
use the same copy at once, it would break for everyone. You need to make
your own copy first.

1. Open the link your instructor shared.
2. In the menu bar, click **File → Save a copy in Drive**.
3. A new tab opens with your own copy — something like
   *"Copy of green_ai_hackathon_baseline.ipynb"*. This is the one you'll
   actually work in. **Close the original tab** so you don't get confused
   about which one is yours.

(By default, your copy is saved into a folder called **"Colab Notebooks"**
at the root of your Google Drive — that's where to look if you ever need
to find it again outside of Colab itself.)

(Optional: rename your copy — click the title at the top of the page —
e.g. add your group name, so it's easy to find again later.)

### Path B — You were given the notebook file (`.ipynb`)

If your instructor shared the actual file rather than a link (e.g. emailed
it, or it's sitting in a shared folder you downloaded from), upload it
directly into Colab:

1. Make sure the `.ipynb` file is saved somewhere easy to find on your
   computer (e.g. your Downloads folder) — you don't need to unzip or
   convert anything, it's ready to use as-is.
2. Go to **[colab.research.google.com](https://colab.research.google.com)**.
   A dialog usually appears automatically; if not, click **File → Upload
   notebook** from the menu bar.
3. In that dialog, select the **Upload** tab.
4. Click **Browse** (or drag-and-drop the file into the window) and choose
   the `green_ai_hackathon_baseline.ipynb` file you saved.
5. Colab opens the notebook in a new tab. This is already your own working
   copy — no need to additionally "Save a copy in Drive," since uploading
   creates your own copy by definition.

(Optional: it's worth doing **File → Save** once near the start, so Colab
properly saves this uploaded copy into your Google Drive rather than
leaving it as a temporary, unsaved upload.)

---

## Step 3 — Turn on a GPU (recommended, not required)

A GPU makes training noticeably faster. You don't strictly need one — the
notebook works on CPU too, just more slowly — but it's worth requesting one
if it's available.

1. Click **Runtime** in the menu bar → **Change runtime type**.
2. Under "Hardware accelerator," select **T4 GPU**.
3. Click **Save**.

**If you see "GPU not available"**: this happens sometimes when many
people are requesting GPUs at once (e.g. everyone in the room doing this
in the same few minutes). Don't worry — just continue with CPU. The
notebook automatically detects this and adjusts itself (smaller dataset,
fewer epochs) so things still run in a reasonable time. You can always try
switching to GPU again later in the session if you want.

---

## Step 4 — Run the setup cells, in order, top to bottom

This is the most important rule: **run cells in order, don't skip
around.** Each cell builds on the ones before it — for example, the model
can't be created until the dataset has been loaded, and the dataset can't
load until the install cell has finished.

To run a cell:
- Click on it, then press **Shift + Enter** (runs it and moves to the
  next cell), or
- Click the **▶ play button** that appears on the left side of the cell
  when you hover over it.

Work through the notebook **section by section**:

### Section 0 — Install dependencies
Run this first. It installs the Python packages the notebook needs
(`codecarbon`, `transformers`, `datasets`). This usually takes under a
minute. You'll see some text print out — that's normal, not an error.

### Section 1 — Setup
Run every cell in this section in order. This loads the dataset, downloads
the pretrained model, and defines some functions the rest of the notebook
uses. **Do not edit anything in this section** — it needs to be identical
for everyone so results can be fairly compared later.

A couple of things you'll see here that are expected, not errors:
- The first time a model is loaded, it prints a "LOAD REPORT" — this is
  normal information about how the pretrained model is being adapted for
  this task, not a warning that something went wrong.
- If you don't have a GPU, you'll see a message saying the notebook is
  using a smaller configuration. That's the automatic adjustment mentioned
  in Step 3 — expected, not a problem.

### Section 2 — Baseline run
Run this cell and **wait for it to finish** before moving on — this is the
one cell in the whole notebook you genuinely cannot rush. It trains a
model three separate times (to get a reliable average) and prints your
group's baseline numbers: accuracy, training time, and energy used. These
are the numbers everything else in the notebook will be compared against.

**Write down or screenshot these numbers** — you'll want them later, even
though they're also saved automatically.

---

## Step 5 — Explore (Section 3)

This is the open-ended part. Run the `run_experiment()` definition cell
first, then look at the **"YOUR TURN"** cell. Running it completely
unchanged will work — it just repeats the baseline configuration with a
placeholder label — so it's a safe way to confirm the `run_experiment()`
pattern works before you change anything. Then go back, pick an idea from
the table above it (or your own), edit the model/config lines, and run it
again.

A few things worth knowing while you're in here:
- Every idea in the table above this section is just a setting to change —
  no need to write new code from scratch.
- You can run the same cell over and over with different settings — every
  attempt gets saved automatically, nothing gets overwritten.
- Add new cells (click the **+ Code** button that appears when you hover
  between cells) if you want to try several ideas without losing track of
  earlier ones.

---

## Step 6 — Compare your results (the Leaderboard and Section 4)

Once you've tried a few things, run the **Leaderboard** cell — it prints a
table comparing every attempt you've made against your baseline,
including how much the numbers vary from run to run (the "std" column).
Use this to decide which attempt is genuinely your best trade-off, not
just the first thing that looked good.

Then run **Section 4**, set `BEST_ATTEMPT_INDEX` to the attempt you want
to present, and run that cell — it prints the exact numbers to copy into
the shared results slide.

---

## Common issues

| What you see | What to do |
|---|---|
| "GPU not available" | Continue on CPU — the notebook adjusts automatically (see Step 3) |
| (Path B) The upload dialog doesn't appear automatically | Click **File → Upload notebook** from the menu bar to open it manually |
| (Path B) You're not sure if your uploaded copy is saved | Do **File → Save** (or **Ctrl+S** / **Cmd+S**) once — this writes it into your Google Drive's "Colab Notebooks" folder, same as Path A's copies |
| A cell seems stuck / spinning for a long time | The first model/dataset download can take a minute or two — this is normal the *first* time, not every time |
| `use_amp=True` doesn't seem to change anything | Expected if you're on CPU — mixed precision only works on a GPU |
| An error mentioning `model_type` when loading a different model | A data quality quirk in a specific community model on the Hub — the notebook already works around the common cases. Try one of the model names suggested in the Section 3 table |
| `ImportError: cannot import name 'VideoReader' from 'torchvision.io'` (during Section 0 or even later, mid-training) | A known library incompatibility, unrelated to anything you did — this notebook never uses video. Section 0 already blocks this from happening; if you still see it, your cells probably ran out of order. Try **Runtime → Restart session**, then run all cells again from the top, in order |
| You accidentally ran cells out of order and something looks wrong | Use **Runtime → Restart session**, then run all cells again from the top, in order |
| You want to start over completely | **Runtime → Restart session and run all** runs everything from scratch |

---

## A note on your Colab session

Your notebook only keeps running while the browser tab is open and
connected. If your connection drops or the session sits idle for a long
time, it can disconnect. Colab will usually try to reconnect you
automatically — but if the runtime itself has timed out (not just your
browser connection), reconnecting gives you a **new, empty runtime**, and
anything that existed only in memory (like `my_attempts`, or the loaded
dataset) is gone. In that case, the fix is **Runtime → Run all** to
rebuild everything from the top — it's quick since most of the heavy
downloading only happens once per runtime anyway.
