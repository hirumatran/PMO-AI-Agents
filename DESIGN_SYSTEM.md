# Olympus-style design system (JP / VN documents)

Source: measured from the live olympus.co.jp homepage (computed styles), 2026-11-10.
Decisions by the project owner: brand blue = **#001C71** (brief) instead of the site's #001478 · yellow used as **thin lines only** · text colours **match the site**.

## 1. Tokens

```css
:root {
  /* Colour */
  --color-bg:        #FFFFFF; /* page background */
  --color-surface:   #F2F2F2; /* info panels, grey bands (site) */
  --color-surface-2: #E6E6E6; /* footer / deepest band (site) */
  --color-border:    #D6D6D6; /* 1px card and table borders (site) */
  --color-ink:       #000000; /* headings (site) */
  --color-body:      #333333; /* body text (site) */
  --color-muted:     #666666; /* captions, dates, notes (site) */
  --color-brand:     #001C71; /* Olympus blue: solid blocks, buttons, links, chevrons */
  --color-on-brand:  #FFFFFF; /* text on blue */
  --color-accent:    #EAA100; /* yellow: thin rules and markers only */

  /* Type */
  --font-sans: "Noto Sans JP", "Noto Sans", "Yu Gothic", Meiryo, sans-serif;
  --fs-hero: 40px;  --fw-hero: 700;  --lh-hero: 1.3;
  --fs-h2:   28px;  --fw-h2:   700;  --lh-h2:   1.6;  --ls-h2: 1.75px;
  --fs-h3:   18px;  --fw-h3:   700;  --lh-h3:   1.5;
  --fs-body: 16px;  --fw-body: 400;  --lh-body: 2;
  --fs-small:13px;  --fw-small:400;  --lh-small:1.5;
  --fs-label:13px;  --fw-label:700;  --ls-label: 1px;

  /* Space (8px base; steps inferred from the site's rhythm) */
  --space-1: 8px;  --space-2: 16px; --space-3: 24px;
  --space-4: 40px; --space-5: 64px;

  /* Shape */
  --radius:      2px;    /* everything rectangular */
  --radius-pill: 999px;  /* only the outlined button on a blue hero */
  --border:      1px solid var(--color-border);
  --rule-brand:  3px solid var(--color-brand);
  --rule-accent: 3px solid var(--color-accent);
  --shadow:      none;   /* site uses a soft shadow only on floating controls */

  /* Layout */
  --content-max: 1024px;
  --grid-gap:    24px;
}
```

## 2. Type scale

| Role | Size | Weight | Line height | Letter spacing | Colour |
|---|---|---|---|---|---|
| Hero (on blue only) | 40px | 700 | 1.3 | 0 | white |
| Section heading (H2) | 28px | 700 | 1.6 | 1.75px | ink #000 |
| Card / block title (H3) | 18px | 700 | 1.5 | 0 | ink #000 |
| Body | 16px | 400 | 2.0 | 0 | body #333 |
| Small / caption | 13px | 400 | 1.5 | 0 | muted #666 |
| Label / eyebrow | 13px | 700 | 1.5 | 1px | brand blue |

Japanese and Vietnamese share one family: Noto Sans JP renders kana/kanji; Noto Sans renders Vietnamese diacritics. Both are free on Google Fonts, so nothing is substituted.

## 3. Google Fonts link

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Noto+Sans:wght@400;500;700&display=swap" rel="stylesheet">
```

## 4. Layout logic

Content sits in one centred column, at most 1024px wide, on white. Sections are stacked top to bottom, and each opens with a bold black H2 on the left, never centred. Within a section, items sit in rows of three cards (or two wide grey panels), 24px apart. Full-width bands mark a change of topic: either solid Olympus blue with white text (used once, for the most important message) or light grey #F2F2F2 (for supporting information). Spacing is generous: 64px between sections, 24–40px inside them. Body text keeps double line spacing so dense Japanese text stays readable.

## 5. Signature element

**The blue chevron "›" in front of every link and card title**, paired with the **thin yellow rule** borrowed from the Olympus logo underline. The chevron tells the reader "this leads somewhere" without a button. The yellow rule appears at most once per view, under a title or as a 3px marker, never as a fill.

## 6. This design never does

- Rounded cards or soft "bubble" corners (anything over 2px, except the single pill button on a blue hero).
- Drop shadows, glows or gradients on cards and panels.
- Yellow as a background fill, yellow text, or yellow on white for anything a reader must read.
- A second accent colour (no green, red or orange decoration).
- Centred body text or centred section headings.
- Tight line spacing on body text (below 1.8).
- Coloured section backgrounds other than Olympus blue or the two greys.

## 7. Bolder options (not applied)

- Use the site's brighter blue #001478 for a closer match to olympus.co.jp.
- Pale yellow (#FDF3DC) highlight boxes for "key point" notes. They're easier to scan but drift from the Olympus look.
- A larger 56px hero heading for slide decks, which are viewed from a distance.
