# Hedge Math

Hedge trimmer honesty. The blade is measured tip to tip, the gap is
measured wide open, and the tall face was always going to take a ladder
of passes. Hedge Math turns the blade, the hedge and the teeth into the
morning.

Live: https://ilanis-agent.github.io/hedgemath/

## The three truths

1. **The blade truth** - blade inches minus the 3-inch grip norm
   (labeled) is the honest working edge; hedge height against honest
   inches is the pass count: two honest sweeps, a working rhythm, or a
   comb-over, not a haircut.
2. **The hedge truth** - passes x hedge length / your walking pace is
   the honest clock: done before the coffee cools, a working morning,
   or pack a lunch.
3. **The tooth truth** - the tooth gap x the 0.8 norm (labeled) is what
   scissors clean; your branch against the honest number: scissors
   clean, chews but finishes, or is a lopper's branch, not the blade's.

Illustrative arithmetic with labeled norms - not a measurement of your
trimmer, your hedge or your branches. Follow the manual's capacity and
safety instructions.

## Files

- `index.html` - landing page
- `app.html` - the three-truth app
- `engine.js` - pure functions (`bladePlan`, `hedgePlan`, `toothPlan`) plus renderers
- `oracle.py` - independent oracle that mirrors the engine float-for-float
- `test.js` - node tests: engine against oracle output (`node test.js`)
- `expected.json` - oracle-generated cases and renders
