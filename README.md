# Hedge Math

Hedge trimmer honesty. The blade is measured tip to tip, and the tall
face was always going to take a ladder of passes. Hedge Math turns the
blade and the hedge into the morning.

Live: https://ilanis-agent.github.io/hedgemath/

## The two truths

1. **The blade truth** - blade inches minus the 3-inch grip norm
   (labeled) is the honest working edge; hedge height against honest
   inches is the pass count: two honest sweeps, a working rhythm, or a
   comb-over, not a haircut.
2. **The hedge truth** - passes x hedge length / your walking pace is
   the honest clock: done before the coffee cools, a working morning,
   or pack a lunch.

## The boundary

Hedge Math gives no cutting-capacity verdicts. What a blade can safely
cut is the manufacturer's call - follow the manual's capacity and
safety instructions.

Illustrative arithmetic with labeled norms - not a measurement of your
trimmer, your hedge or your branches.

## Files

- `index.html` - landing page
- `app.html` - the two-truth app
- `engine.js` - pure functions (`bladePlan`, `hedgePlan`) plus renderers
- `oracle.py` - independent oracle that mirrors the engine float-for-float
- `test.js` - node tests: engine against oracle output (`node test.js`)
- `expected.json` - oracle-generated cases and renders
